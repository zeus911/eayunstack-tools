# @file restore.py
import logging
import utils
<<<<<<< HEAD
from utils import restore_backup
=======
>>>>>>> 42b547ea12cf5a27d9c1f2c7707d2fe1482895ab


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
         check = """
     * The Fuel version is the same release as the backup.
     * There are no deployments running.
     * At least 11GB free space in /var.
         """
         LOG.error('Unexpected Error')
         LOG.error('Please check the information below:\n %s', check)
     else:
         LOG.info('Restore successfully completed!\n')


