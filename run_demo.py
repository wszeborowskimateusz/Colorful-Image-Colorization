import os, random, shutil
import glob
import string
import generate_demo_file_names

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
    f"{datasets_folder}celebryci",
    f"{datasets_folder}kwiatki",
    f"{datasets_folder}landscape",
    f"{datasets_folder}ptaki"
]

demo_input_path = './demo_input'
demo_output_path = './demo_output'

def run_demo(picked_datasets_index):
    # First clear some folders
    remove_folder_content(demo_input_path)
    remove_folder_content(demo_output_path)

    # Now pick some random images from dataset
    random_files = []
    folder_path = datasets[picked_datasets_index]
    for _ in range(files_to_pick):
        random_files.append(folder_path + "/" + random.choice(os.listdir(folder_path)))

    for random_file in random_files:
        shutil.copy2(random_file, demo_input_path)

    # Now generate names for them
    generate_demo_file_names.main()

    import demo
    demo.main()

    # Now save results with renamed name to results folder
    results_folder = '../results'
    N = 10
    file_index = 0
    for file in os.listdir(demo_output_path):
        # 0 - gt
        # 1 - black and white
        # 2 - out
        file_extension = file.split('.')[-1]
        if file_index % 3 == 0:
            dataset_name = datasets[picked_datasets_index].split('/')[-1]
            random_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
            gt = f"{random_name}_gt.{file_extension}"
            bandw = f"{random_name}_black_and_white.{file_extension}"
            out = f"{random_name}_out.{file_extension}"

            shutil.copy2(f"{demo_output_path}/{file}", f"{results_folder}/{dataset_name}/{gt}")
        elif file_index % 3 == 1:
            # Black and white
            shutil.copy2(f"{demo_output_path}/{file}", f"{results_folder}/{dataset_name}/{bandw}")
        else:
            # out
            shutil.copy2(f"{demo_output_path}/{file}", f"{results_folder}/{dataset_name}/{out}")

        file_index += 1

for i in range(len(datasets)):
    run_demo(i)

remove_folder_content(demo_input_path)
remove_folder_content(demo_output_path)