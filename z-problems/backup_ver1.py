import os
import time

# 1. The files and directories to be backed up are specified in a list.
source = ['/home/marisa/zzzzzz/source/1/one.txt', '/home/marisa/zzzzzz/source/1/two.txt']

# 2. The backup must be stored in a main backup directory
destination = '/home/marisa/zzzzzz/destination/'

# 3. The files are backed up into a zip file.
# 4. The name of the zip archive is the current date and time
target = destination + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

# 5. We use the zip command to put the files in a zip archive
zip_command = 'zip -qr {0} {1}'.format(target, ''.join(source))

# Run the backup
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')