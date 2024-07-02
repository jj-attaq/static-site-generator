import os


def copy_static(dir='.'):
    current_path = dir
    contents = os.listdir(current_path)
    for el in contents:
        if os.path.isfile(el):
            print(el)
            continue
        else:
            new_path = os.path.join(current_path, el)
            if os.path.isfile(new_path):
                print(new_path)
            else:
                copy_static(new_path)
