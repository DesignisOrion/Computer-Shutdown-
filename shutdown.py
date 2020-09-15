# App allows you to shut down your computer via python

import os
shutdown = input('Do you wish to SHUTDOWN your computer ? (Yes/No)')
if shutdown == 'no':
    exit()

else:
    os.system('shutdown /s /t 1')
