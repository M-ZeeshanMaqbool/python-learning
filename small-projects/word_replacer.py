
words = ["donkey", "dog", "bitch", "monkey"]

with open("newf.txt", "r", encoding="utf-8") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#" * len(word))

with open("newf.txt", "w", encoding="utf-8") as f:
    f.write(content)

print("All specified words have been replaced!")
