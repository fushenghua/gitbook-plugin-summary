# -*- coding: utf-8 -*-

import argparse
import os
import re
import json

def execute(cmd):
    return os.system(cmd) == 0

def mkdir(dirPath):
    if not os.path.exists(dirPath):
        os.makedirs(dirPath)
        print("mkdir",dirPath) 

def readTitle(dirPath):
    f = open(dirPath+'/book.json', encoding='utf-8') 
    book = json.load(f)
    return book['title']     

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--overwrite', 
                        help='overwrite on SUMMARY.md', 
                        action="store_true")
    parser.add_argument('-a', '--append', 
                        help='append on SUMMARY.md', 
                        action="store_true")
    parser.add_argument('directory', 
                        help='the directory of your GitBook root')
    args = parser.parse_args()
    overwrite = args.overwrite
    append = args.append
    dir_input = args.directory

    # print information
    
    if execute('python3 gitbook-plugin-summary.py -o {}'.format(dir_input)) :
        print('create summary file:', dir_input, end = ' ')

    print('GitBook create start epub:')
    mkdir(dir_input+'/docs')
    try:
        title=readTitle(dir_input)
    except:
        title ='book'

    print (title)    
    if execute('gitbook epub {} {}'.format(dir_input,dir_input+'/docs/'+title+'.epub')):
        print('*************************************************************')
        print('GitBook created epub ...:', dir_input, end = ' ')
        print('*************************************************************')

    if execute('./KindleGen_Mac_i386_v2_9/kindlegen {}'.format(dir_input+'/docs/'+title+'.epub')):
        print('GitBook convert mobi:', dir_input, end = ' ')

    print('GitBook generated mobi finished:) ')
    return 0

if __name__ == '__main__':
    main()