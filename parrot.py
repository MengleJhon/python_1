message = input("Tell me something, and I will repeat it back to you: ")
print(message)

name = input("Please enter your name: ")
print("Hello, " + name + "!")

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print("\nHello, " + name + "!")

age = input("How old are you? ")
print(age)
print(int(age))
# print(age >= 18) # 错误
print(int(age) >= 18)
# print("His age is " + int(age) + ".") # 错误
print("His age is " + age + ".")