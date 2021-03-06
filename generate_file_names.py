import numpy as np

file_names = [f"{n:05d}.png" for n in range(1, 1201)]

train_names = file_names[:1000]
valid_names = file_names[1000:]

with open("train_names.txt", "w") as f:
    for name in train_names:
        f.write(f"{name}\n")

with open("valid_names.txt", "w") as f:
    for name in valid_names:
        f.write(f"{name}\n")