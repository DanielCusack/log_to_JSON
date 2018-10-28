#!/usr/bin/env python3
import sys
import json
import os
import re
import math

class ConverterLog2JSON:
    '''
    Class to convert Apache Common Log Format files to a JSON report.
    Arguments:
    logpath; str; path to the log file
    reportdir; str; path to report directory

    '''
    def __init__(self, logpath, reportdir):
        self.logpath = logpath
        self.reportdir = reportdir
        self.logdict = {}
        self.create_report()
    
    #def create_path(self, path_string):
    #    path_items = path_string.split('/')
    #    if path_string[0] == '/':
    #        return os.path.join('/',*path_items)
    #    else:
    #        return os.path.join(*path_items)

    def file_exists(self):
        return os.path.isfile(self.logpath)

    def directory_exists(self):
        return os.path.isdir(self.reportdir)

    def convert_log(self):
        '''Converts the Apache Common Log Format to a dictionary'''
        #I think this conversion could be done better using regular expressions.
        #Didn't have time to learn them though.
        with open(self.logpath, 'r') as logfile:
            for line in logfile:
                line_list = line.replace('[', '').replace(']', '').replace('\n','').split(' ')
                date = line_list[3].split(':')[0].split('/')
                month = date[1]
                year = date[2]
                month_year = month + '/' + year
                language = line_list[6].split('/')[1]
                byte_size = int(line_list[-1])
                if month_year in self.logdict:
                    self.logdict[month_year].append([language, byte_size])
                else:
                    self.logdict[month_year] = [[language, byte_size]]
    
    def prepare_data(self):
        for month, files in self.logdict.items():
            file_size_dict = dict()
            for f in files:
                if f[0] in file_size_dict:
                    file_size_dict[f[0]].append(f[1])
                else:
                    file_size_dict[f[0]] = [f[1]]
            self.logdict[month] = file_size_dict

    def create_report(self):
        if self.file_exists:
            self.convert_log()
            self.prepare_data()
        else:
            raise FileNotFoundError
        
        
        
        


    




if __name__ == '__main__':
    path_args = sys.argv[1:]
    if len(path_args) != 2:
        raise IndexError('Must give two arguments.')

    converter = ConverterLog2JSON(*path_args)
    print(converter.logdict)

    