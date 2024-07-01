import os


def main():
    current = os.listdir('.')

    for dir in current:
        if os.path.isfile(f'{dir}'):
            print(dir)
            continue
        print(os.listdir(f'{dir}'))


main()
