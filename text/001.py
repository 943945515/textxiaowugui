import tkinter as tk
import random

# 初始化窗口
root = tk.Tk()
root.title("弹跳球体")
root.geometry("600x400")
root.resizable(False, False)

# 定义球体参数
ball = tk.Canvas(root, width=600, height=400, bg="black")
ball.pack()

# 球体初始位置和速度
x = 300
y = 200
dx = 3
dy = 3
radius = 20

# 绘制球体
def draw_ball():
    ball.delete("all")
    ball.create_oval(x - radius, y - radius, x + radius, y + radius, fill="cyan", outline="white")
    root.after(50, move_ball)

# 移动球体
def move_ball():
    global x, y, dx, dy
    x += dx
    y += dy

    # 碰撞检测（左右边界）
    if x - radius <= 0 or x + radius >= 600:
        dx = -dx
    # 碰撞检测（上下边界）
    if y - radius <= 0 or y + radius >= 400:
        dy = -dy

    draw_ball()

# 启动动画
draw_ball()
root.mainloop()