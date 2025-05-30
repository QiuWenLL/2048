# 2048 Game - Python Implementation

![Game Screenshot](assets/screenshot.png)

A complete implementation of the classic 2048 game using Python and Pygame.

## ✨ Features

- Classic 2048 gameplay mechanics
- Smooth tile animations with Pygame
- Real-time score tracking
- Win/lose detection
- Keyboard controls with restart option
- Responsive UI with colorful tiles

## 🛠️ Installation Guide

### Prerequisites
- Python 3.6 or higher
- pip package manager

### Step-by-Step Installation

1. Clone the repository:
```bash
git clone https://github.com/QiuWenLL/2048.git
cd 2048
```

2. Create and activate virtual environment (recommended):
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## 🎮 How to Play

### Running the Game
```bash
python main.py
```

### Detailed Controls
| Key | Action |
|-----|--------|
| ↑ (Up Arrow) | Move all tiles upward |
| ↓ (Down Arrow) | Move all tiles downward |
| ← (Left Arrow) | Move all tiles left |
| → (Right Arrow) | Move all tiles right |
| R | Restart the game |
| Q | Quit the game |

### Game Rules
1. Use arrow keys to slide all tiles in the chosen direction
2. When two tiles with the same number touch, they merge into one
3. After each move, a new tile (either 2 or 4) appears in a random empty spot
4. Reach the 2048 tile to win!
5. Game ends when the board is full and no more moves are possible

## 📊 Game Records / 游戏记录

Game scores are automatically saved to `scores.json` file, containing:
- Score (得分)
- Date & time (日期时间) 
- Final board state (最终棋盘状态)

### Viewing Records (查看记录):
1. **On GitHub (在GitHub上查看)**:
   - Visit repo: https://github.com/QiuWenLL/2048
   - Click `scores.json`
   - Click "Raw" to view raw data or "History" for versions

2. **Locally (本地查看)**:
```bash
# View records (查看记录)
cat scores.json

# Pretty-print (格式化输出，需要安装jq):
jq '.' scores.json
```

## 🌟 Tips & Tricks
- Try to keep your highest number in a corner
- Plan ahead to create chains of merges
- Don't just move randomly - have a strategy!

## 🚨 Troubleshooting

### Common Issues
1. **Pygame not found**:
   ```bash
   pip install pygame --upgrade
   ```

2. **Black screen appears**:
   - Make sure your terminal supports graphical display
   - Try running on a different Python version

3. **Controls not working**:
   - Ensure keyboard is connected properly
   - Check if another application is intercepting key presses

## 🏗️ Project Structure
```
2048/
├── assets/          # Game assets (images, sounds)
├── game.py          # Core game logic
├── display.py       # Pygame display implementation
├── main.py          # Main game loop
├── requirements.txt # Dependencies
└── README.md        # Documentation
```

## 🤝 Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository
2. Create your feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a pull request

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments
- Original 2048 game by Gabriele Cirulli
- Pygame library developers