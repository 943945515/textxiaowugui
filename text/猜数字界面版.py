import tkinter as tk
from tkinter import messagebox
import random
import time
from PIL import Image, ImageTk  # 需要安装 Pillow 库（pip install pillow）

# 主窗口设置
root = tk.Tk()
root.title("猜数字游戏 🎲")
root.geometry("500x550")
root.resizable(False, False)

# 设置窗口背景色（渐变效果）
root.configure(bg="#e6f7ff")

# 加载字体（现代风格）
font_title = ("Segoe UI", 24, "bold")
font_label = ("Arial", 16)
font_button = ("Arial", 14, "bold")
font_icon = ("Segoe UI", 16)

# 加载图标（可选）
icon_path = "icon.png"  # 替换为你的图标路径
try:
    icon = Image.open(icon_path)
    icon = icon.resize((32, 32))
    icon = ImageTk.PhotoImage(icon)
except:
    icon = None

# 游戏变量
number_to_guess = random.randint(1, 100)
attempts = 0
max_attempts = 7

# 动画效果（猜对时的闪烁）
def flash_result_label():
    result_label.config(bg="#90ee90", fg="black")
    root.after(300, lambda: result_label.config(bg="#e6f7ff", fg="blue"))

# 创建界面元素
label_title = tk.Label(
    root,
    text="猜一个 1-100 的数字：",
    font=font_title,
    bg="#e6f7ff",
    fg="#004080",
    padx=10,
    pady=10
)
label_title.pack(pady=15)

entry = tk.Entry(
    root,
    font=font_label,
    width=10,
    bd=2,
    relief=tk.RAISED,
    bg="#ffffff",
    fg="#004080",
    justify="center"
)
entry.pack(pady=10)

result_label = tk.Label(
    root,
    text="",
    font=font_label,
    bg="#e6f7ff",
    fg="blue",
    wraplength=450,
    justify="center"
)
result_label.pack(pady=10)

# 按钮样式（圆角、悬停效果）
def on_enter(e):
    button.config(bg="#0078d4", fg="white", relief=tk.FLAT)

def on_leave(e):
    button.config(bg="#005ea7", fg="white", relief=tk.RAISED)

button = tk.Button(
    root,
    text="猜 一下",
    font=font_button,
    bg="#005ea7",
    fg="white",
    relief=tk.RAISED,
    bd=2,
    command=lambda: check_guess(),
    activebackground="#003d80",
    activeforeground="white"
)
button.bind("<Enter>", on_enter)
button.bind("<Leave>", on_leave)
button.pack(pady=15)

# 重置按钮（绿色）
def reset_game():
    global number_to_guess, attempts
    number_to_guess = random.randint(1, 100)
    attempts = 0
    entry.delete(0, tk.END)
    result_label.config(text="", fg="blue")
    entry.config(state="normal")
    button.config(state="normal")
    reset_button.config(state="disabled")
    root.after(200, lambda: reset_button.config(state="normal"))

reset_button = tk.Button(
    root,
    text="重新开始",
    font=font_button,
    bg="#8fbc8f",
    fg="white",
    relief=tk.RAISED,
    bd=2,
    command=reset_game,
    state="disabled"
)
reset_button.pack(pady=5)

# 检查猜测逻辑
def check_guess():
    global attempts
    guess = entry.get()

    if not guess.isdigit():
        result_label.config(text="⚠️ 请输入一个有效的数字！", fg="red")
        return
    guess = int(guess)

    if guess < 1 or guess > 100:
        result_label.config(text="⚠️ 数字范围必须在 1-100 之间！", fg="red")
        return

    attempts += 1
    if guess == number_to_guess:
        result_label.config(text=f"🎉 恭喜！你猜中了！答案是 {number_to_guess}！", fg="green")
        entry.config(state="disabled")
        button.config(state="disabled")
        flash_result_label()
    elif guess < number_to_guess:
        result_label.config(text=f"❌ 太小了！剩余尝试次数：{max_attempts - attempts}", fg="red")
    else:
        result_label.config(text=f"❌ 太大了！剩余尝试次数：{max_attempts - attempts}", fg="red")

    if attempts == max_attempts:
        result_label.config(text=f"😭 游戏结束！正确答案是 {number_to_guess}。", fg="red")
        entry.config(state="disabled")
        button.config(state="disabled")
        reset_button.config(state="normal")

# 添加图标（可选）
if icon:
    icon_label = tk.Label(root, image=icon, bg="#e6f7ff")
    icon_label.pack(pady=10)

# 运行主循环
root.mainloop()
'''

---

### 🎨 **界面精美化设计说明**
1. **渐变背景**：使用浅蓝色（`#e6f7ff`）营造清新感。
2. **圆角按钮**：通过 `relief=tk.RAISED` 和 `bd=2` 实现立体按钮效果。
3. **悬停动画**：按钮悬停时颜色和样式变化（`on_enter`/`on_leave`）。
4. **图标支持**：通过 `Pillow` 库加载图标（需安装 `Pillow`）。
5. **动画效果**：猜对时的标签闪烁（`flash_result_label`）。
6. **字体与排版**：使用现代字体（`Segoe UI`/`Arial`）提升可读性。

---

### 📌 **运行方法**
1. **安装依赖**：
   ```bash
   pip install pillow
   ```
2. **保存代码**：将代码保存为 `guess_number_gui.py`。
3. **在 VS Code 中运行**：
   - 打开文件，点击右上角的运行按钮（绿色三角）或使用快捷键 `Ctrl + F5`。
4. **游戏功能**：
   - 输入数字并点击“猜一下”。
   - 系统会提示“太大”、“太小”或“恭喜猜中”。
   - 点击“重新开始”可重置游戏。

---

### 🧩 **可扩展功能建议**
1. **音效提示**：添加成功/失败的音效（使用 `winsound` 或 `pygame`）。
2. **历史记录**：保存用户猜测历史（使用 `tkinter` 的 `Listbox`）。
3. **难度级别**：增加不同范围（如 1-50/1-200）。
4. **动画过渡**：使用 `tkinter` 动画库（如 `tkinter.ttk`）实现更复杂的动画。

---

通过以上设计，游戏界面将更加现代、直观且吸引人，同时保持代码的清晰性和可维护性。'''