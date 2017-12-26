#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ConfigParser
import subprocess
import sys
import os
import argparse


class GitConfig(object):

    def __init__(self):
        self.__config = ConfigParser.RawConfigParser()
        
    def call_git(self, params):
        
        if type(params) is str:
            params = tuple(params.split(' '))

        # https://stackoverflow.com/questions/2473655/how-to-make-a-call-to-an-executable-from-python-script
        popen = subprocess.Popen( ('/usr/bin/git',)+params, stdout=subprocess.PIPE)
        popen.wait()
        output = popen.stdout.read().strip()
        
        return {
            "returncode": popen.returncode
            ,"stdout": output
        }


    def get_local_user_config(self):
        
        output = self.call_git( 'config --local user.name' )
        if output['returncode'] == 0:
            self.username = output['stdout']
        else:
            self.username = ''

        output = self.call_git( 'config --local user.email' )
        if output['returncode'] == 0:
            self.useremail = output['stdout']
        else:
            self.useremail = ''




'''
    cmdparser = argparse.ArgumentParser(description='Add host to OLL virt-who config')
    cmdparser.add_argument('config', help='Full path to config file')
    cmdparser.add_argument('hostname', help='FQDN of the server to add')
    cmdparser.add_argument('uuid', help='uuid of the server to add')
    cmdparser.add_argument('environment', help='which environment to add the server to. PROD or TEST')
    cmdparser.add_argument('comment', nargs="?", help='optional comment to add to the json data. This parameter needs to be specified last. To use spaces add string in quotes')

    cmdargs = cmdparser.parse_args()
'''

def git_cmd_accountmgr_add():
    cmdparser = argparse.ArgumentParser(description='...')
    cmdparser.add_argument('user.name','-u', type=str, help='...', required=True)
    cmdparser.add_argument('user.email','-e', type=str, help='...', required=True)

    cmdargs = cmdparser.parse_args()

def git_cmd_accountmgr_change():
    pass

def git_cmd_accountmgr_set():
    pass


def git_cmd_accountmgr_main():
    
    if len(sys.argv) > 0:
        cmd = sys.argv[1].lower()

        if cmd == "add":
            git_cmd_accountmgr_add()
        elif cmd == "change":
            git_cmd_accountmgr_change()
        elif cmd == "set":
            git_cmd_accountmgr_set()
        else:
            print "error"
    else:
        print "error"



def git_hook_pre_commit():

    gitconf = GitConfig()
    gitconf.get_local_user_config()

    print gitconf.username
    print gitconf.useremail

    if gitconf.username and gitconf.useremail:
        sys.exit(os.EX_OK)
    else:
        print "No account specified "
        sys.exit(os.EX_NOPERM)



def main():

    argv = sys.argv

    print len(argv)
    print argv
    print os.path.basename(argv[0])

    called_as = os.path.basename(argv[0]).lower()

    if called_as == 'git-accountmgr':
        git_cmd_accountmgr_main()
    elif called_as == 'pre-commit':
        git_hook_pre_commit()




if __name__ == '__main__':
    main()

