# -*- coding: utf-8 -*-

import argparse
import os
import re

def execute(cmd):
    return os.system(cmd) == 0

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
    if execute('gitbook epub {} {}'.format(dir_input,dir_input+'/docs/Android-Learningnotes.epub')):
        print('GitBook created epub ...:', dir_input, end = ' ')

    if execute('./KindleGen_Mac_i386_v2_9/kindlegen {}/docs/Android-Learningnotes.epub'.format(dir_input)):
        print('GitBook convert mobi:', dir_input, end = ' ')

    # if overwrite:
    #     print('--overwrite', end = ' ')
    # if append and os.path.exists(os.path.join(dir_input, 'SUMMARY.md')): 
    #     #append: read former SUMMARY.md
    #     print('--append', end = ' ')
    #     global former_summary_list
    #     with open(os.path.join(dir_input, 'SUMMARY.md')) as f:
    #         former_summary_list = f.readlines()
    #         f.close()
    # print()
    # output to flie
    # if (overwrite == False and 
    #     os.path.exists(os.path.join(dir_input, 'SUMMARY.md'))):
    #     # overwrite logic
    #     filename = 'SUMMARY-GitBook-auto-summary.md'
    # else:
    #     filename = 'SUMMARY.md'
    # output = open(os.path.join(dir_input, filename), 'w')
    # output.write('# Summary\n\n')
    # output.write('* [README](./README.md)\n')
    # output_markdown(dir_input, dir_input, output, append)
    # output.close()
    # print('GitBook auto summary finished:) ')
    return 0

if __name__ == '__main__':
    main()