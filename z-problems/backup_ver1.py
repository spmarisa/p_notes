import os
import time

# The files and directories to be backed up are specified in a list.
source = ['/home/marisa/z/source/1.txt', '/home/marisa/z/source/2.txt']

# The backup must be stored in a main backup directory
target_dir = '/home/marisa/z/destination'

# The files are backed up into a zip file.
today = target_dir + os.sep + time.strftime('%Y%m%d')
# The current time is the name of the zip archive
now = time.strftime('%H%M%S')


# Take a comment from the user to create the name of the zip file
comment = input('Enter a comment --> ')
if len(comment) == 0: # check if a comment was entered
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + comment.replace(' ', '_') + '.zip'




# Create the subdirectory if it isn‚t already there
if not os.path.exists(today):
    os.mkdir(today)  # make directory
    print('Successfully created directory', today)

# The name of the zip file
target = today + os.sep + now + '.zip'

# We use the zip command to put the files in a zip archive
zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))


# Run the backup
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup failed')