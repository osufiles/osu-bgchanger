#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import re
import shutil

from distutils.core import setup
import py2exe


def getBackgroundName(file_object):
    for (num, line) in enumerate(file_object, 1):
        if '.jpg' in line or '.png' in line or '.jpeg' in line:
            print '\t\tFound background entry at line {0}'.format(num)
            file_object.close()
            return str(re.findall(r'\"(.+?)\"', line))[2:-2]
    return 0


def replace(filename):
    root = os.listdir('.')
    for entry in root:
        if not os.path.isfile(entry):
            print 'Found folder "{0}"'.format(entry)
            for file in os.listdir(entry):
                imageName_lookup = []
                if file.endswith('.osu'):
                    print '\tFound .osu file "{0}"'.format(file)
                    cwd = os.getcwd() + '\\' + entry + '\\'
                    imageName = getBackgroundName(open(cwd + file, 'r'))
                    if imageName == 0:
                        print '\t\tUnable to find a background entry, skipping'
                        continue
                    imageName_lookup.append(imageName)
                    try:
                        os.rename(cwd + imageName, cwd + imageName
                                  + '.bak')
                        print '\t\tSuccessfully backed up {0}'.format(imageName)
                    except (WindowsError, OSError), e:
                        if imageName in imageName_lookup:
                            print '\t\tFile "{0}" is already backed up, no need to do it again!'.format(imageName)
                        continue
                    if shutil.copy2(os.getcwd() + '\\' + filename, cwd
                                    + imageName):
                        print '\t\tFailed to copy new background, missing?'
                    else:
                        print '\t\tSuccessfully copied new background!'
            print '\n'
        else:
            print 'Found file, ignoring'
    print '\nCompleted!'


def revert():
    root = os.listdir('.')
    for entry in root:
        if not os.path.isfile(entry):
            print 'Found folder ({0})'.format(entry)
            for file in os.listdir(entry):
                if file.endswith('.bak'):
                    print '\tFound .bak file "{0}"'.format(file)
                    cwd = os.getcwd() + '\\' + entry + '\\'
                    if os.path.isfile(cwd + file):
                        os.remove(cwd + file[:-4])
                        os.rename(cwd + file, cwd + file[:-4])
                        print '\t\tSuccessfully reverted backgroud image {0}'.format(file)
                    else:
                        print '\t\tFailed to revert!'
            print '\n'
        else:
            print 'Found file, ignoring'
    print '\nCompleted!'


def main():
    print '(1) Replace standard backgrounds with custom image'
    print '(2) Revert background change'
    c = raw_input(' > ')
    if c == '1':
        print 'Enter image name, eg. background.jpg'
        c = raw_input(' > ')
        if os.path.isfile(c):
            replace(c)
        else:
            print 'Not an image!'
    elif c == '2':
        revert()


if __name__ == '__main__':
    main()

			