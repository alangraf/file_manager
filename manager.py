import os.path
import shutil
from random import randint
from os import listdir, rename
from os.path import isfile, join
from extensions import FILE_EXTENSIONS


class FileManager:

    def __init__(self, dir_roots: list, target_root: str, logger):
        self.dir_roots = dir_roots
        self.target_root = target_root
        self.logg = logger

    @staticmethod
    def get_all_files(root_dir: str):
        only_files = [f for f in listdir(root_dir) if isfile(join(root_dir, f)) and not f.startswith('.') and not f.startswith('~')]
        return only_files

    def cleaner(self, files: list, source_root: str):
        for filename in files:
            ext_of_file = filename.split('.')[1]

            if ext_of_file in FILE_EXTENSIONS['pdf']:
                self.move_file_to_folder(source_root, filename, 'PDF')

            elif ext_of_file in FILE_EXTENSIONS['image']:
                self.move_file_to_folder(source_root, filename, 'Image')

            elif ext_of_file in FILE_EXTENSIONS['video']:
                self.move_file_to_folder(source_root, filename, 'Video')

            elif ext_of_file in FILE_EXTENSIONS['shell']:
                self.move_file_to_folder(source_root, filename, 'Shell')

            elif ext_of_file in FILE_EXTENSIONS['word']:
                self.move_file_to_folder(source_root, filename, 'Word')

    def move_file_to_folder(self, source_root: str, filename: str, foldername: str):
        self.create_dir_if_not_exist(foldername)

        if not self.check_if_filename_exists(filename, join(self.target_root, foldername)):
            shutil.move(join(source_root, filename), join(self.target_root, foldername))
            self.logg.info(f"{foldername} file moved")
        else:
            self.logg.info(f"{filename} already exists in {foldername} folder")
            filename = self.rename_file(filename, source_root)
            self.logg.info(f"Renamed to {filename} and moved to {foldername} folder")

    @staticmethod
    def rename_file(filename: str, source_root: str):
        name, extension = filename.split(".")
        new_filename = join(source_root, name + '_.' + extension)
        rename(join(source_root, filename), new_filename)

        return new_filename

    def create_dir_if_not_exist(self, folder_name):
        if not os.path.exists(join(self.target_root, folder_name)):
            self.logg.info(f"{folder_name} folder created")
            os.makedirs(join(self.target_root, folder_name))

    def check_if_filename_exists(self, filename: str, folder_path: str):
        if filename in self.get_all_files(folder_path):
            return True

        return False

    def run(self):
        for dir_root in self.dir_roots:
            files = self.get_all_files(dir_root)

            if files:
                self.cleaner(files, dir_root)
