import os

demo_names = []

for file in os.listdir("demo_input"):
    if file.endswith(".png") or file.endswith(".jpg"):
        print(f"Found file {file}. Adding it to list")
        demo_names.append(file)

with open("demo_names.txt", "w") as f:
    for name in demo_names:
        f.write(f"{name}\n")