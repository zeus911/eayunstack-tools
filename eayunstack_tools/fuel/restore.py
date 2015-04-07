# @file restore.py
import logging
from utils import backup_list


LOG = logging.getLogger(__name__)

def restore(parser):
    if parser.ID:
        restore_bck(parser.ID)

def make(parser):
    '''Fuel Restore'''
    parser.add_argument(
        '-i',
        '--id',
        action = 'store',
        dest = 'ID',
        type = int,
        help = 'Specify the ID you want to restore'
    )
    parser.set_defaults(func=restore)

def restore_bck(id):
    LOG.info('Starting Restore ...')
    LOG.info('It will take about 30 minutes, Please wait ...\n')
    backup_list()
    if id in file_list.keys():
        backup_file = BACKUP_DIR + '/' + dir_list[id] + '/' + file_list[id]
        (stat, out) = commands.getstatusoutput('dockerctl restore %s' % (backup_file))
        if stat != 0:
            LOG.error('%s', out)            
        else:
            LOG.info('Restore successfully completed!\n')


