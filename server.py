from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
import random
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dice_game_secret'
socketio = SocketIO(app, cors_allowed_origins="*")

# Game state
game_state = {
    'players': {},
    'round': 1,
    'max_rounds': 3,
    'game_active': False,
    'winner': None
}

@app.route('/')
def board():
    """Main game board display (for computer)"""
    return render_template('board.html')

@app.route('/player')
def player():
    """Player controller (for phones)"""
    return render_template('player.html')

@socketio.on('connect')
def handle_connect():
    print('Client connected')
    emit('game_update', game_state)

@socketio.on('join_game')
def handle_join(data):
    player_name = data.get('name', f'Player{len(game_state["players"]) + 1}')
    player_id = request.sid
    
    game_state['players'][player_id] = {
        'name': player_name,
        'score': 0,
        'current_roll': None,
        'has_rolled': False
    }
    
    print(f'{player_name} joined the game')
    emit('game_update', game_state, broadcast=True)
    emit('player_joined', {'name': player_name}, broadcast=True)

@socketio.on('start_game')
def handle_start():
    if len(game_state['players']) >= 1:
        game_state['game_active'] = True
        game_state['round'] = 1
        game_state['winner'] = None
        
        # Reset all players
        for player in game_state['players'].values():
            player['score'] = 0
            player['current_roll'] = None
            player['has_rolled'] = False
        
        emit('game_update', game_state, broadcast=True)

@socketio.on('roll_dice')
def handle_roll():
    player_id = request.sid
    
    if not game_state['game_active']:
        emit('error', {'message': 'Game not started yet!'})
        return
    
    if player_id not in game_state['players']:
        emit('error', {'message': 'You are not in the game!'})
        return
    
    player = game_state['players'][player_id]
    
    if player['has_rolled']:
        emit('error', {'message': 'You already rolled this round!'})
        return
    
    # Roll two dice
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2
    
    player['current_roll'] = [dice1, dice2]
    player['score'] += total
    player['has_rolled'] = True
    
    # Check if all players have rolled
    all_rolled = all(p['has_rolled'] for p in game_state['players'].values())
    
    if all_rolled:
        # Move to next round or end game
        if game_state['round'] >= game_state['max_rounds']:
            end_game()
        else:
            game_state['round'] += 1
            # Reset rolled status for next round
            for p in game_state['players'].values():
                p['has_rolled'] = False
    
    emit('game_update', game_state, broadcast=True)

def end_game():
    game_state['game_active'] = False
    
    # Find winner
    max_score = max(p['score'] for p in game_state['players'].values())
    winners = [p['name'] for p in game_state['players'].values() if p['score'] == max_score]
    
    if len(winners) == 1:
        game_state['winner'] = winners[0]
    else:
        game_state['winner'] = ' & '.join(winners) + ' (Tie!)'
    
    emit('game_update', game_state, broadcast=True)

@socketio.on('disconnect')
def handle_disconnect():
    player_id = request.sid
    if player_id in game_state['players']:
        player_name = game_state['players'][player_id]['name']
        del game_state['players'][player_id]
        print(f'{player_name} left the game')
        emit('game_update', game_state, broadcast=True)

if __name__ == '__main__':
    print("\n" + "="*50)
    print("🎲 DICE GAME SERVER STARTING 🎲")
    print("="*50)
    print("\nInstructions:")
    print("1. Open main board: http://localhost:5000")
    print("2. Connect phones to: http://YOUR_IP:5000/player")
    print("   (Find your IP with: ipconfig on Windows or ifconfig on Mac/Linux)")
    print("\n" + "="*50 + "\n")
    
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
