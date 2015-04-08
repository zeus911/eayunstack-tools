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
    """List all the backup file"""
    lines = read_db()
    i = 1
    t = PrettyTable(['ID', 'Backup Time', 'Backup File'])
    for line in lines:
        # Delete the '\n' at the end of the line
        line = line.strip('\n')
        id = line.split(' ')[0]
        backup_file = line.split(' ')[1]
        file_split = backup_file.split('_', 4)
        # Get the backup time from filename
        c_date = file_split[2]
        c_time = file_split[3].split('.', 1)[0][:2] \
                 + ':' + \
                 file_split[3].split('.', 1)[0][2:]
        t.add_row([i, c_date + ' ' + c_time, backup_file])
        i += 1
    return t


def read_db():
    """Get Lines as List"""
    if not os.path.exists('/tmp/tools.db'):
        os.mknod('/tmp/tools.db')
    db = open('/tmp/tools.db')
    lines = db.readlines()
    db.close()
    return lines

def backup_dict():
    # Use sorted() method to sort by filename
    backup_dirs = sorted(os.listdir(BACKUP_DIR + '/'))
    not_backup = 'restore'
    for backup_dir in backup_dirs:
        if not_backup in backup_dir:
            continue
        elif os.path.isfile(BACKUP_DIR + '/' + backup_dir):
            backup_file = backup_dir
            dir_list[i] = ''
            file_list[i] = backup_file
        else:
            backup_file = os.listdir(BACKUP_DIR + '/' + backup_dir + '/')
            dir_list[i] = backup_dir
            file_list[i] = backup_file[0]
    return file_list

def write_db():
    # append
    db = open('/tmp/tools.db', 'a')
    backup_dict()
    id = file_list.keys()[-1]
    backup_file = file_list[id]
    db.writelines('%s' % id + ' ' + '%s\n' % backup_file)
    db.close()


