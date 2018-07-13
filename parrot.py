#-*-coding:utf-8-*-
message = input("Tell me something, and I will repeat it back to you: ")
print(str(message))

name = input("Please enter your name: ")
print("Hello, " + str(name) + "!")

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print("\nHello, " + str(name) + "!")

age = input("How old are you? ")
print(age)