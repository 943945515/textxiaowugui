import random

# 设置游戏参数
number_to_guess = random.randint(1, 100)
attempts = 0
max_attempts = 7

# 游戏提示
print("🎉 欢迎来到猜数字游戏！")
print("我会随机生成一个 1 到 100 的数字，你有 7 次机会猜中它！")

while attempts < max_attempts:
    try:
        guess = int(input(f"\n第 {attempts + 1} 次尝试：请输入你的猜测（1-100）："))
        attempts += 1

        if guess < number_to_guess:
            print("❌ 太小了！")
        elif guess > number_to_guess:
            print("❌ 太大了！")
        else:
            print(f"🎉 恭喜！你猜中了！答案是 {number_to_guess}！")
            break
    except ValueError:
        print("⚠️ 请输入一个有效的数字！")

# 如果未猜中
if attempts == max_attempts:
    print(f"\n😭 游戏结束！你没猜中。正确答案是 {number_to_guess}。")
'''

---

### 📌 **运行方法**
1. **保存代码**：将上述代码保存为 `guess_number.py`。
2. **在 VS Code 中运行**：
   - 打开文件，点击右上角的运行按钮（绿色三角）或使用快捷键 `Ctrl + F5`。
3. **效果**：程序会提示你输入猜测的数字，并根据你的输入给出提示，直到猜中或尝试次数用完。

---

### 🧠 **代码说明**
- **随机生成数字**：使用 `random.randint(1, 100)` 生成 1 到 100 的随机数。
- **尝试次数限制**：设置 `max_attempts = 7`，玩家有 7 次机会。
- **错误处理**：使用 `try-except` 捕获用户输入非数字的情况，避免程序崩溃。
- **提示信息**：根据猜测值大小给出“太大”或“太小”的提示，帮助玩家调整策略。

---

### 🎁 **扩展建议**
如果想让游戏更有趣，可以尝试以下改进：
1. **增加难度**：扩大数字范围（如 1-1000）或减少尝试次数。
2. **记录历史分数**：保存玩家的最高分。
3. **添加音效或动画**：使用 `pygame` 库增加互动性（需额外安装）。

---

### 📌 **注意事项**
- 确保已安装 Python 3，并在 VS Code 中配置了 Python 解释器。
- 如果遇到输入错误（如输入字母），程序会提示重新输入，不会直接崩溃。

希望这个小游戏能让你在学习 Python 的过程中感受到乐趣！如果有其他需求，可以随时告诉我 😊'''