
word = "donkey"

with open("newf.txt", "r", encoding="utf-8") as f:
    content = f.read()

new_content = content.replace(word, "######")

with open("newf.txt", "w", encoding="utf-8") as f:
    f.write(new_content)

print("Word replaced successfully!")
