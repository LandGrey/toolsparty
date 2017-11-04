#!/usr/bin/env python
# coding:utf-8
# Build by LandGrey 2017-11-04

import os
import re
import sys


def unique(seq, idfun=None):
    if idfun is None:
        def idfun(x): return x
    seen = {}
    results = []
    for item in seq:
        marker = idfun(item)
        if marker in seen:
            continue
        seen[marker] = 1
        results.append(item)
    return results


def get_subdir_path(directory, only_file_path=True):
    dirpaths = []
    filepaths = []
    for rootpath, subdirsname, filenames in os.walk(directory):
        dirpaths.extend([os.path.abspath(os.path.join(rootpath, _)) for _ in subdirsname])
        filepaths.extend([os.path.abspath(os.path.join(rootpath, _)) for _ in filenames])
    if only_file_path:
        return filepaths
    else:
        return dirpaths, filepaths


def walk_all_files(directory):
    contents = []
    for _ in get_subdir_path(directory):
        with open(_, 'r') as f:
            for line in f.readlines():
                if line.strip() != '':
                    contents.append(line.strip())
    return unique(contents)


def run(line, limit=False):
    mail_matches = mail_pattern.findall(line)
    mails.extend([mm[0] for mm in mail_matches] if not limit else [d[0] for d in mail_matches if d[0].endswith(limit)])
    domain_matches = domain_pattern.findall(line)
    domains.extend([dm[0] for dm in domain_matches] if not limit else [d[0] for d in domain_matches if d[0].endswith(limit)])
    internal_ip_matches = internal_ip_pattern.findall(line)
    if internal_ip_matches:
        internal_ip.extend([im[0] for im in internal_ip_matches])
    else:
        external_ip_matches = common_ip_pattern.findall(line)
        external_ip.extend([em[0] for em in external_ip_matches])


if __name__ == "__main__":
    if not (len(sys.argv) == 2 or len(sys.argv) == 3):
        exit("[*] python filter.py file_or_dir [domain_limit]")
    if len(sys.argv) == 2:
        strict = False
    else:
        strict = sys.argv[2]

    mails = []
    domains = []
    internal_ip = []
    external_ip = []

    common_ip_pattern = re.compile('((\d{1,3}\.){3}\d{1,3}(/\d{2})?)')
    domain_pattern = re.compile('((((\d|\w)*)\.)+[a-zA_Z]{2,})')
    mail_pattern = re.compile('(.*?@((((\d|\w)*)\.)+[a-zA_Z]{2,}))')
    internal_ip_pattern = re.compile(r'(^10\.((\d){1,3}\.){2}(\d){1,3}(/\d{2})?)|'
                                     r'(^127\.((\d){1,3}\.){2}(\d){1,3}(/\d{2})?)|'
                                     r'(^172\.([1][6-9]|[2][0-9]|[3][0-1])\.(\d){1,3}\.(\d){1,3}(/\d{2})?)|'
                                     r'(^192\.168\.(\d){1,3}\.(\d){1,3}(/\d{2})?)')
    if os.path.isdir(sys.argv[1]):
        for row in walk_all_files(sys.argv[1]):
            run(row, strict)
    elif os.path.isfile(sys.argv[1]):
        with open(sys.argv[1], 'r') as f:
            for row in f.readlines():
                run(row.strip(), strict)
    print("[+]        mails       (%s)" % len(unique(mails)))
    for m in unique(mails):
        print(m)
    print("\n[+]        domains     (%s)" % len(unique(domains)))
    for d in unique(domains):
        print(d)
    print("\n[+]        internal ip (%s)" % len(unique(internal_ip)))
    for ip in unique(internal_ip):
        print(ip)
    print("\n[+]        external ip (%s)" % len(unique(external_ip)))
    for ip in unique(external_ip):
        print(ip)
