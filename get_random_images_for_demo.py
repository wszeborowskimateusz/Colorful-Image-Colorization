import os, random, shutil
import glob

def remove_folder_content(path):
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))


files_to_pick = 10
datasets_folder = "../datasets/"

datasets = [
    f"{datasets_folder}google_landscapes", 
    f"{datasets_folder}google_landscapes",
    f"{datasets_folder}google_landscapes",
    f"{datasets_folder}google_landscapes",
    f"{datasets_folder}google_landscapes"
]

picked_datasets_indices = [0]

# First clear some folders
demo_input_path = './demo_input'
demo_output_path = './demo_output'

remove_folder_content(demo_input_path)
remove_folder_content(demo_output_path)

# Now pick some random images from dataset
random_files = []
files_per_dataset = files_to_pick // len(picked_datasets_indices) 
for index in picked_datasets_indices:
    folder_path = datasets[index]
    for _ in range(files_per_dataset):
        random_files.append(folder_path + "/" + random.choice(os.listdir(folder_path)))

for random_file in random_files:
    shutil.copy2(random_file, demo_input_path)

# Now generate names for them
import generate_demo_file_names