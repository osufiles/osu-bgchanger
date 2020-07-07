import os
import re
import shutil


def get_background_name(file_object):
    for (num, line) in enumerate(file_object, 1):
        if ".jpg" in line or ".png" in line or ".jpeg" in line:
            print(f"\t\tFound background entry at line {num}")
            file_object.close()
            return str(re.findall(r"\"(.+?)\"", line))[2:-2]
    return 0


def replace(filename):
    root = os.listdir(".")
    for entry in root:
        if not os.path.isfile(entry):
            print(f'Found folder "{entry}"')
            for file in os.listdir(entry):
                image_name_lookup = []
                if file.endswith(".osu"):
                    print(f'\tFound .osu file "{file}"')
                    cwd = os.getcwd() + "\\" + entry + "\\"
                    image_name = get_background_name(open(cwd + file, "r",encoding="utf-8",errors="ignore"))
                    if image_name == 0:
                        print("\t\tUnable to find a background entry, skipping")
                        continue
                    image_name_lookup.append(image_name)
                    try:
                        os.rename(cwd + image_name, cwd + image_name + ".bak")
                        print(f"\t\tSuccessfully backed up {image_name}")
                    except (WindowsError, OSError) as e:
                        if image_name in image_name_lookup:
                            print(
                                f'\t\tFile "{image_name}" is already backed up, no need to do it again!'
                            )
                        continue
                    if shutil.copy2(os.getcwd() + "\\" + filename, cwd + image_name):
                        print("\t\tFailed to copy new background, missing?")
                    else:
                        print("\t\tSuccessfully copied new background!")
            print("\n")
        else:
            print("Found file, ignoring")
    print("\nCompleted!")


def revert():
    root = os.listdir(".")
    for entry in root:
        if not os.path.isfile(entry):
            print(f"Found folder ({entry})")
            for file in os.listdir(entry):
                if file.endswith(".bak"):
                    print(f'\tFound .bak file "{file}"')
                    cwd = os.getcwd() + "\\" + entry + "\\"
                    if os.path.isfile(cwd + file):
                        os.remove(cwd + file[:-4])
                        os.rename(cwd + file, cwd + file[:-4])
                        print(f"\t\tSuccessfully reverted backgroud image {file}")
                    else:
                        print("\t\tFailed to revert!")
            print("\n")
        else:
            print("Found file, ignoring")
    print("\nCompleted!")


def main():
    print("(1) Replace standard backgrounds with custom image")
    print("(2) Revert background change")
    c = input(" > ")
    if c == "1":
        print("Enter image name, eg. background.jpg")
        c = input(" > ")
        if os.path.isfile(c):
            replace(c)
        else:
            print("Not an image!")
    elif c == "2":
        revert()


if __name__ == "__main__":
    main()
