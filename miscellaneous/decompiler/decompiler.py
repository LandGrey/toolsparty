#!/usr/bin/env python
# coding: utf-8
# -**- Author: LandGrey -**-

import os
import sys
import time
import zipfile
import argparse
import subprocess
import shutil
from distutils.dir_util import copy_tree

save_dir = None


def command_exec(lib_path):
    global save_dir
    if isinstance(lib_path, list):
        for lib_file in lib_path:
            command = "java -jar fernflower.jar -hes=0 -hdc=0 {} {}".format(lib_file, save_dir)
            execute = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = execute.communicate()
            print("[+] decompile {} complete !".format(lib_file))
    else:
        command = "java -jar fernflower.jar -hes=0 -hdc=0 {} {}".format(lib_path, save_dir)
        execute = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = execute.communicate()
        print("[+] decompile {} complete !".format(lib_path))


def get_dir_files_path(directory, extension_limit=None, keyword_limit=None):
    file_paths = []

    def check_extension(name):
        for extension in extension_limit:
            if name.endswith(extension):
                return True
        return False

    def check_keyword(name):
        for keyword in keyword_limit:
            if keyword in name:
                return True
        return False

    for root_path, subdirs_name, file_names in os.walk(directory):
        for file_name in file_names:
            going_on = False
            if extension_limit and keyword_limit:
                if check_extension(file_name) and check_keyword(file_name):
                    going_on = True
            elif extension_limit:
                if check_extension(file_name):
                    going_on = True
            elif keyword_limit:
                if check_keyword(file_name):
                    going_on = True
            else:
                going_on = True
            if going_on:
                file_paths.append(os.path.abspath(os.path.join(root_path, file_name)))
    return list(set(file_paths))


def run(_source_dir, save_dir, _extension_limit, _keyword_limit, merge_package, delete_package):
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
    source_files = get_dir_files_path(_source_dir, extension_limit=_extension_limit, keyword_limit=_keyword_limit)
    print("[+] decompile {} files ...".format(len(source_files) if len(source_files) > 0 else 1))
    if len(os.listdir(_source_dir)) == len(source_files):
        command_exec(_source_dir)
    else:
        if os.path.isdir(_source_dir):
            command_exec(source_files)
        else:
            command_exec(_source_dir)
    package_dirs = []
    for p in os.listdir(save_dir):
        fp = os.path.join(save_dir, p)
        if fp.endswith(".zip") or fp.endswith(".jar"):
            if os.path.isfile(fp):
                with zipfile.ZipFile(fp, 'r') as zip_ref:
                    package_dir = os.path.join(save_dir, "java_package", p[:-4])
                    package_dirs.append(package_dir)
                    zip_ref.extractall(package_dir)
                os.remove(fp)
    if merge_package:
        merge_dir = os.path.join(save_dir, "java")
        for package_dir in package_dirs:
            copy_tree(package_dir, merge_dir)
        if delete_package:
            shutil.rmtree(os.path.join(save_dir, "java_package"))
    print("[+] Cost      {} seconds".format(str(time.time() - start_time)[:5]))


if __name__ == "__main__":
    start_time = time.time()
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-s', dest='source_dir', default='', help='source dir/single-file')
    parser.add_argument('-d', dest='save_dir', default='', help='save dir')
    parser.add_argument('-e', dest='extension_limit', default='', help='extension limit, such as: [.jar,.java]')
    parser.add_argument('-k', dest='keyword_limit', default='', help='keyword limit, such as: [xx1,xx2]')
    parser.add_argument('--merge', dest='merge_package', default='',  action="store_true", help='merge "java package" to "java source"')
    parser.add_argument('--delete', dest='delete_package', default='',  action="store_true", help='delete "java package"')

    if len(sys.argv) == 1:
        sys.argv.append('-h')
    args = parser.parse_args()
    source_dir = args.source_dir
    save_dir = args.save_dir
    merge_package = args.merge_package
    delete_package = args.delete_package
    extension_limit = args.extension_limit.split(",")
    keyword_limit = args.keyword_limit.split(",")
    run(source_dir, save_dir, extension_limit, keyword_limit, merge_package, delete_package)
