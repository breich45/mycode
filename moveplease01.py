#!/usr/bin/env python3

import shutil
import os

os.chdir("/home/student/mycode") #change to correct dir
shutil.move('raynor.obj', 'ceph_storage/') #mv obj into new dir

xname = input("What is the new name for the kerrigan.obj?") #get new name for object
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname) #rename object my moving to new name

