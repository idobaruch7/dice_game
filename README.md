# 🎲 Dice Game

A multiplayer dice game where players use their phones as controllers and view the game on a main display board. Built with Flask, Socket.IO, and HTML/CSS/JavaScript.

## 📋 Table of Contents
- [Game Description](#game-description)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
  - [Linux](#linux-installation)
  - [Windows](#windows-installation)
- [Running the Game](#running-the-game)
  - [Linux](#running-on-linux)
  - [Windows](#running-on-windows)
- [How to Play](#how-to-play)
- [Troubleshooting](#troubleshooting)

## 🎮 Game Description

This is a multi-round dice game where:
- Players connect using their phones as controllers
- A main board displays all players and their scores
- Each player rolls two dice per round
- The player with the highest total score after 3 rounds wins
- Real-time synchronization using WebSockets

## 📦 Prerequisites

You need to have Python installed on your system:
- **Python 3.7 or higher**
- **pip** (Python package installer)

### Check if Python is installed:

**Linux:**
```bash
python3 --version
```

**Windows:**
```cmd
python --version
```

If Python is not installed:
- **Linux**: `sudo apt install python3 python3-pip` (Ubuntu/Debian) or `sudo yum install python3 python3-pip` (Fedora/RHEL)
- **Windows**: Download from [python.org](https://www.python.org/downloads/)

## 🔧 Installation

### Linux Installation

1. **Clone or download the repository:**
```bash
cd ~
git clone https://github.com/idobaruch7/dice_game.git
cd dice_game
```

2. **Install required Python packages:**
```bash
pip3 install flask flask-socketio
```

3. **Verify the folder structure:**
```bash
ls -la
```
You should see:
```
dice_game/
├── server.py
└── templates/
    ├── board.html
    └── player.html
```

### Windows Installation

1. **Clone or download the repository:**
```cmd
cd C:\Users\YourUsername
git clone https://github.com/idobaruch7/dice_game.git
cd dice_game
```

Or download the ZIP file and extract it.

2. **Install required Python packages:**
```cmd
pip install flask flask-socketio
```

3. **Verify the folder structure:**
```cmd
dir
```
You should see:
```
dice_game/
├── server.py
└── templates/
    ├── board.html
    └── player.html
```

## 🚀 Running the Game

### Running on Linux

1. **Navigate to the game directory:**
```bash
cd ~/dice_game
```

2. **Start the server:**
```bash
python3 server.py
```

3. **Find your IP address** (for phone connections):
```bash
hostname -I
```
or
```bash
ip addr show
```
Look for your local IP address (usually starts with 192.168.x.x or 10.0.x.x)

4. **Access the game:**
   - **Main Board** (on computer): Open browser to `http://localhost:5000`
   - **Player Controllers** (on phones): Open browser to `http://YOUR_IP_ADDRESS:5000/player`

### Running on Windows

1. **Open Command Prompt or PowerShell**

2. **Navigate to the game directory:**
```cmd
cd C:\Users\YourUsername\dice_game
```

3. **Start the server:**
```cmd
python server.py
```

4. **Find your IP address** (for phone connections):
```cmd
ipconfig
```
Look for "IPv4 Address" under your active network adapter (usually starts with 192.168.x.x or 10.0.x.x)

5. **Access the game:**
   - **Main Board** (on computer): Open browser to `http://localhost:5000`
   - **Player Controllers** (on phones): Open browser to `http://YOUR_IP_ADDRESS:5000/player`

## 🎯 How to Play

1. **Setup:**
   - Start the server on your computer
   - Open the main board (`http://localhost:5000`) on your computer
   - Have each player open `http://YOUR_IP:5000/player` on their phones

2. **Join Game:**
   - Each player enters their name on their phone
   - Players will appear on the main board as they join

3. **Start Game:**
   - Once all players have joined, click "Start Game" on the main board
   - The game will run for 3 rounds

4. **Playing:**
   - When it's your turn, tap "ROLL DICE" on your phone
   - Your roll and score will appear on both your phone and the main board
   - Wait for all players to roll before moving to the next round

5. **Winning:**
   - After 3 rounds, the player with the highest total score wins!
   - Click "Play Again" to start a new game

## 🔧 Troubleshooting

### Server won't start

**Error: "Address already in use"**
- Another program is using port 5000
- **Linux:** `sudo lsof -i :5000` then `kill -9 <PID>`
- **Windows:** Open Task Manager and end the process using port 5000

**Error: "Module not found: flask"**
- Install dependencies: `pip install flask flask-socketio` (Windows) or `pip3 install flask flask-socketio` (Linux)

### Phones can't connect

**Make sure:**
- Your computer and phones are on the same WiFi network
- Your firewall isn't blocking port 5000
- You're using the correct IP address (not localhost on phones)

**Linux firewall:**
```bash
sudo ufw allow 5000
```

**Windows firewall:**
- Go to Windows Defender Firewall → Advanced Settings
- Create new Inbound Rule for port 5000

### Players not seeing updates

- Refresh the browser pages
- Check the terminal/command prompt for error messages
- Restart the server and reconnect

### Finding your IP address

**Linux:**
```bash
hostname -I
# or
ip addr show | grep inet
```

**Windows:**
```cmd
ipconfig | findstr IPv4
```

**Mac:**
```bash
ifconfig | grep "inet " | grep -v 127.0.0.1
```

## 📱 Network Setup

For best results:
- Connect all devices to the same WiFi network
- Use your computer's local IP (192.168.x.x or 10.0.x.x)
- Don't use "localhost" or "127.0.0.1" on phones

## 🛑 Stopping the Server

- **Linux/Mac:** Press `Ctrl + C` in the terminal
- **Windows:** Press `Ctrl + C` in Command Prompt/PowerShell

## 🎲 Game Rules

- **Number of Players:** 1 or more (2+ recommended)
- **Number of Rounds:** 3
- **Dice:** Two 6-sided dice per roll
- **Scoring:** Sum of both dice per round
- **Winner:** Highest total score after all rounds

---

**Enjoy the game! 🎉**
