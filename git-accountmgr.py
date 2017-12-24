#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ConfigParser
import subprocess



class GitConfig(object):

    def __init__(self):
        self.__config = ConfigParser.RawConfigParser()
        
    def call_git(self, params):
        
        # https://stackoverflow.com/questions/2473655/how-to-make-a-call-to-an-executable-from-python-script
        popen = subprocess.Popen(params, stdout=subprocess.PIPE)
        popen.wait()
        output = popen.stdout.read()
        
        return {
            "returncode": popen.returncode
            ,"stdout": output
        }


    def get_local_user_config(self):
        
        self.call_git('config --local user.name')



def main():
    pass


if __name__ == '__main__':
    main()

