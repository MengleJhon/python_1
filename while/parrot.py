prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\n(Enter 'quit' to end the program.)"

# 第一版
# message = ""
# while message != 'quit':
#     message = input(prompt)
#
#     if message != 'quit':
#         print(message)

# 第二版：使用flag
# active = True
# while active:
#     message = input(prompt)
#
#     if message == 'quit':
#         active = False
#     else:
#         print(message)

# 使用break
while True:
    message = input(prompt)

    if message == 'quit':
        break
    else:
        print(message)