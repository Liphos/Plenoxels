import glob
import os
import zipfile

from opt.scripts.ingp2nsvf import convert


def replace_word_in_file(file_path, old_word, new_word):
    try:
        with open(file_path, "r") as file:
            file_data = file.read()

        # Replace the old word with the new word
        file_data = file_data.replace(old_word, new_word)

        with open(file_path, "w") as file:
            file.write(file_data)

        print(f"Word '{old_word}' replaced with '{new_word}' in {file_path}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def unzip_file(zip_file_path, extract_to_path):
    try:
        with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
            zip_ref.extractall(extract_to_path)
        print(f"File '{zip_file_path}' successfully extracted to '{extract_to_path}'")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


path_to_zip = "./Assets/"
filename = "mva_logo"
files_extension = ["training", "validation", "testing"]
output_extension = ["train", "val", "test"]
output_folder = "./Datasets/" + filename + "/"

for incr, file_ext in enumerate(files_extension):
    path_to_folder = path_to_zip + filename + "_" + file_ext
    file = path_to_folder + ".zip"
    unzip_file(file, path_to_folder)
    for entry in os.listdir(path_to_folder):
        current_file = path_to_folder + "/" + entry
        if os.path.isfile(current_file) and current_file.endswith(".json"):
            # open the json file to remove .png extension and change the name of the folder the photos are in
            replace_word_in_file(
                current_file,
                "train",
                output_extension[incr],
            )
            replace_word_in_file(
                current_file,
                ".png",
                "",
            )

        elif os.path.isdir(current_file):
            pass
        else:
            raise Exception(
                "There are something else than the json and the folder in the data folder provided"
            )

        new_file = path_to_folder + "/" + entry.replace("train", output_extension[incr])
        os.rename(current_file, new_file)

    # Convert to a more suitable format
    convert(path_to_folder, output_folder)
