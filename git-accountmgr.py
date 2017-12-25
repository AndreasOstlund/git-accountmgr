#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ConfigParser
import subprocess
import sys
import os



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
cmdparser = argparse.ArgumentParser(description='...')
    cmdparser.add_argument('add', nargs="?", help='Adds an account')
    cmdparser.add_argument('change', nargs="?", help='Chages account setting')
    cmdparser.add_argument('set', nargs="?", help='Sets the account to use')

    cmdargs = cmdparser.parse_args()

'''


def main(argv):
    print len(argv)
    print argv
    print os.path.basename(argv[0])

    called_as = os.path.basename(argv[0]).lower()

    if called_as == 'git-accountmgr':
        pass
    elif called_as == 'pre-commit':
        pass

        gitconf = GitConfig()
        gitconf.get_local_user_config()

        print gitconf.username
        print gitconf.useremail

        if gitconf.username and gitconf.useremail:
            sys.exit(os.EX_OK)
        else:
            print "No account specified "
            sys.exit(os.EX_NOPERM)



if __name__ == '__main__':
    main(sys.argv)

