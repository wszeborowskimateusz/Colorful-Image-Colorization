import os

demo_names = []

for file in os.listdir("demo_input"):
    if file.endswith(".png") or file.endswith(".jpg"):
        demo_names.append(file)

with open("demo_names.txt", "w") as f:
    for name in demo_names:
        f.write(f"{name}\n")