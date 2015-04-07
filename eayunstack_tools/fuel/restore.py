# @file restore.py
import logging
from utils import restore_backup


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
     (stat, out) = restore_backup(id)                              
     if stat != 0:
         LOG.error('%s', out)            
     else:
         LOG.info('Restore successfully completed!\n')


