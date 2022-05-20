import shutil
import os

source = ''
destination = ''

files = os.listdir(source)
shutil.copy(source, destination)

