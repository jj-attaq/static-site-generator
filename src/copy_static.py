import os
import shutil


# def copy_static(dir, dest):
#     current_path = dir
#     contents = os.listdir(current_path)
#     for el in contents:
#         if os.path.isfile(el):
#             print(el)
#             shutil.copy(el, dest)
#             continue
#         else:
#             new_path = os.path.join(current_path, el)
#             if os.path.isfile(new_path):
#                 new_dest = dest + '/' + el
#                 shutil.copy(new_path, new_dest)
#                 print(new_path)
#             else:
#                 new_dest = dest + el
#                 os.mkdir(new_dest)
#                 copy_static(new_path, new_dest)
def copy_files_recursive(source_dir_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    for filename in os.listdir(source_dir_path):
        from_path = os.path.join(source_dir_path, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        print(f" * {from_path} -> {dest_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            copy_files_recursive(from_path, dest_path)
