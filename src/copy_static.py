import os
import shutil


def copy_static(dir='.', dest='./public/'):
    # delete ./public
    # shutil.rmtree(dest)
    current_path = dir
    contents = os.listdir(current_path)
    for el in contents:
        if os.path.isfile(el):
            print(el)
            shutil.copy(el, dest)
            continue
        else:
            new_path = os.path.join(current_path, el)
            if os.path.isfile(new_path):
                new_dest = dest + '/' + el
                shutil.copy(new_path, new_dest)
                print(new_path)
            else:
                new_dest = dest + el
                os.mkdir(new_dest)
                copy_static(new_path, new_dest)
