import os

os.mkdir("new_directory")
import time

time.sleep(5)
os.rename('new_directory','old_directory')

time.sleep(10)
os.rmdir('old_directory')