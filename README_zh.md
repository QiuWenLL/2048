# 2048游戏 - Python实现

![游戏截图](assets/screenshot.png)

使用Python和Pygame实现的经典2048游戏完整版本。

## ✨ 功能特点

- 经典2048游戏机制
- 使用Pygame实现的流畅方块动画
- 实时分数记录
- 胜利/失败检测
- 键盘控制含重启选项
- 响应式UI与彩色方块

## 🛠️ 安装指南

### 环境要求
- Python 3.6或更高版本
- pip包管理器

### 逐步安装

1. 克隆仓库：
```bash
git clone https://github.com/QiuWenLL/2048.git
cd 2048
```

2. 创建并激活虚拟环境(推荐)：
```bash
python -m venv venv
# Windows系统：
venv\Scripts\activate
# macOS/Linux系统：
source venv/bin/activate
```

3. 安装依赖：
```bash
pip install -r requirements.txt
```

## 🎮 游戏指南

### 运行游戏
```bash
python main.py
```

### 详细控制
| 按键 | 操作 |
|-----|--------|
| ↑ (上箭头) | 所有方块向上移动 |
| ↓ (下箭头) | 所有方块向下移动 |
| ← (左箭头) | 所有方块向左移动 |
| → (右箭头) | 所有方块向右移动 |
| R | 重新开始游戏 |
| Q | 退出游戏 |

### 游戏规则
1. 使用方向键将所有方块向指定方向滑动
2. 当两个相同数字的方块接触时，它们会合并为一个
3. 每次移动后，一个新的方块(2或4)会出现在随机空白位置
4. 合成2048方块即可获胜！
5. 当棋盘已满且无法移动时游戏结束

## 📊 游戏记录

游戏分数会自动保存到`scores.json`文件中，包含：
- 得分
- 日期时间
- 最终棋盘状态

### 查看记录：
1. **在GitHub上查看**：
   - 访问仓库：https://github.com/QiuWenLL/2048
   - 点击`scores.json`
   - 点击"Raw"查看原始数据或"History"查看历史版本

2. **本地查看**：
```bash
# 查看记录
cat scores.json

# 格式化输出(需要安装jq)：
jq '.' scores.json
```

## 🌟 技巧提示
- 尝试将最大数字保持在角落
- 提前规划创建合并链
- 不要随机移动 - 要有策略！

## 🚨 故障排除

### 常见问题
1. **找不到Pygame**：
   ```bash
   pip install pygame --upgrade
   ```

2. **出现黑屏**：
   - 确保终端支持图形显示
   - 尝试使用不同的Python版本运行

3. **控制无效**：
   - 确保键盘连接正常
   - 检查是否有其他应用程序拦截了按键

## 🏗️ 项目结构
```
2048/
├── assets/          # 游戏资源(图片、音效)
├── game.py          # 核心游戏逻辑
├── display.py       # Pygame显示实现
├── main.py          # 主游戏循环
├── requirements.txt # 依赖项
└── README.md        # 文档
```

## 🤝 参与贡献
欢迎贡献！请按以下步骤操作：
1. Fork本仓库
2. 创建特性分支 (`git checkout -b feature/你的特性`)
3. 提交更改 (`git commit -m '添加某个特性'`)
4. 推送到分支 (`git push origin feature/你的特性`)
5. 发起Pull Request

## 📜 许可证
本项目采用MIT许可证 - 详见[LICENSE](LICENSE)文件

## 🙏 致谢
- 原版2048游戏由Gabriele Cirulli开发
- Pygame库开发者