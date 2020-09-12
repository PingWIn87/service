import os
import argparse
import pprint

def parse_args ():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--source', dest='source_folder', required=True)
    args = parser.parse_args()
    return args

def get_file_names(folder, extensions):
    files = []
    dir_items = os.listdir(folder)
    for item in dir_items:
        if os.path.isfile(os.path.abspath('{0}/{1}'.format(folder,item))) and item.endswith(extensions):
            files.append(item)
    return files

def remove_extensions(file_names_list):
    for i in range(0,len(file_names_list)):
        file_names_list[i] = os.path.splitext(file_names_list[i])[0]
    return file_names_list

def remove_bad_photos(source_folder, file_names_list, removed_extention):
    src_file_list = get_file_names(source_folder, (removed_extention))
    src_file_list = remove_extensions(src_file_list)
    files_to_remove = list (set(src_file_list)-set(file_names_list))
    for removed_file in files_to_remove:
        removed_file_path = os.path.abspath('{0}/{1}.{2}'.format(source_folder, removed_file, removed_extention))
        print('Remove: {0}'.format(removed_file_path))
        os.remove(removed_file_path)

def main():
    args = parse_args()
    extensions = ('.jpg', '.jpeg', '.JPG', '.JPEG')
    files = get_file_names(folder='{0}/jpeg'.format(args.source_folder), extensions=extensions)
    files = remove_extensions(files)
    remove_bad_photos(args.source_folder,files,'raf')


main()