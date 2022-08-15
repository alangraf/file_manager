import os.path
import shutil
from os import listdir
from random import randint
from os.path import isfile, join


class FileManager:

    def __init__(self, dir_roots: list, target_root: str):
        self.dir_roots = dir_roots
        self.target_root = target_root

    @staticmethod
    def get_all_files(root_dir: str):
        only_files = [f for f in listdir(root_dir) if isfile(join(root_dir, f)) and not f.startswith('.') and not f.startswith('~')]
        return only_files

    def cleaner(self, files: list, source_root: str, target_root: str):
        for filename in files:
            if filename.endswith('.pdf'):
                self.create_dir_if_not_exist('PDF')
                shutil.move(os.path.join(source_root, filename), join(target_root, 'PDF'))

            elif filename.endswith('.svg') or filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
                self.create_dir_if_not_exist('Image')
                shutil.move(os.path.join(source_root, filename), join(target_root, 'Image'))

            elif filename.endswith('.mp4'):
                self.create_dir_if_not_exist('Video')
                shutil.move(join(source_root, filename), join(target_root, 'Video'))

            elif filename.endswith('.sh'):
                self.create_dir_if_not_exist('Shell')
                shutil.move(os.path.join(source_root, filename), join(target_root, 'Shell'))

    def create_dir_if_not_exist(self, folder_name):
        if not os.path.exists(join(self.target_root, folder_name)):
            os.makedirs(join(self.target_root, folder_name))

    @staticmethod
    def rename_file_if_exists(current_path: str, target_path: str):
        if os.path.exists(target_path):
            os.rename(target_path, current_path + str(randint(0, 1000)))

    def run(self):
        for dir_root in self.dir_roots:
            files = self.get_all_files(dir_root)

            if files:
                self.cleaner(files, dir_root, self.target_root)
