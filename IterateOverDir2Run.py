#!/usr/bin/python

import os, sys,re,time
from fileRename import renameFile

path = str(os.getcwd())

for file in os.listdir(path):
  if re.match('.*txt$', file):
      renameFile(file)
      time.sleep(1)
      #print file