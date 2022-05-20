import shutil
import os

source = ''
destination = ''

files = os.listdir(source)
shutil.move(source, destination)

