# @file utils.py
import os
import commands
from prettytable import PrettyTable
import logging

LOG = logging.getLogger(__name__)

BACKUP_DIR = '/var/backup/fuel'

dir_list = {}
file_list = {}


def backup_list():
    backup_dirs = os.listdir(BACKUP_DIR + '/')
    backup_dirs.sort(compare)
    i = 1
    t = PrettyTable(['ID', 'Create Time', 'File Name'])
    # when taking restore, there will be dirs named 'restore'. will not list 'restore' dir.
    not_backup = 'restore'
    for backup_dir in backup_dirs:
        if not_backup in backup_dir:
            continue
        elif os.path.isfile(BACKUP_DIR + '/' + backup_dir):
            file_split = backup_dir.split('_', 4)
            c_date = file_split[2]
            c_time = file_split[3].split('.', 1)[0][:2] + ':' + file_split[3].split('.', 1)[0][2:]
            backup_file = backup_dir
            dir_list[i] = ''
            file_list[i] = backup_file
        else:
            file_split = backup_dir.split('_', 2)
            c_date = file_split[1]
            c_time = file_split[2][:2] + ':' + file_split[2][2:]
            backup_file = os.listdir(BACKUP_DIR + '/' + backup_dir + '/')
            dir_list[i] = backup_dir
            file_list[i] = backup_file[0]
        # Put the result in a dictory, every sub-dir has only one backup file
        t.add_row([i, c_date + ' ' + c_time, file_list[i]])
        i += 1
    return t


# Sort the file, the file of most recent content modification will located at the end of the table
def compare(x, y): 
    stat_x = os.stat(BACKUP_DIR + '/' + x)
    stat_y = os.stat(BACKUP_DIR + '/' + y)
    if stat_x.st_mtime > stat_y.st_mtime:
        return 1
    elif stat_x.st_mtime < stat_y.st_mtime:
        return -1
    else:
        return 0

