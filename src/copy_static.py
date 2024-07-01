import os


def copy_static():
    dir = input('Enter dir name: ')
    if not os.path.exists(dir):
        raise ValueError('Path does not exist')

    print(os.listdir(dir))
