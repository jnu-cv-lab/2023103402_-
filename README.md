# 计算机视觉实验二：OpenCV 图像基础操作、调试（多文件版本）

## 实验环境
- 操作系统：Ubuntu / WSL2
- 开发工具：VS Code
- 编程语言：Python 3.x
- 依赖库：opencv-python, matplotlib, numpy

## 项目结构
2023103402_孙勇超/
├── .vscode/               
│   ├── tasks.json          # 运行/调试任务
│   ├── launch.json         # 调试配置
├── src/                    # 代码目录（多文件拆分）
│   ├── main.py             # 主程序入口
│   ├── image_utils.py      # 工具函数（拆分的多文件）
├── data/                   # 放你的图片
│   └── _20231211070702.jpg # 你的原图
├── output/                 # 生成的图片
└── README.md               

## 多文件编译/运行说明
1.  将图像读取、信息输出、格式转换等功能封装到 `image_utils.py`，主程序 `main.py` 调用工具函数，实现代码解耦。
2. 通过 `.vscode/tasks.json` 和 `.vscode/launch.json` 实现一键运行（`Ctrl+Shift+B`）和一键调试（`F5`）。
3.  运行步骤：
    ```bash
    # 1. 安装依赖
    pip install -r requirements.txt
    # 2. 运行程序
    python3 src/main.py

## 学生信息
作者：孙勇超  
学号：2023103402