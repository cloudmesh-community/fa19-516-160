# fa19-516-160
# E.Cloudmesh.Shell.3
# Task : Write a new command and experiment with docopt syntax and argument interpretation of the dict with if conditions.

#from cloudmesh.common.dotdict import dotdict
from __future__ import print_function
from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand

class shreyansCommand(PluginCommand):
  @command
  def do_shreyans(self, args, arguments):
    """
    ::
      Usage:
            shreyans -f FILE
            shreyans list
      This command does some useful things.
      Arguments:
        FILE a file name
      Options:
           -f specify the file
    """
    print(arguments)
    if arguments.FILE:
      print("You have used file: ", arguments.FILE)
    return ""

# Invoke the do_shreyans function
result = Shell.execute('cms', ['shreyans', '-f', '\"file name with spaces\"'])
print(result)