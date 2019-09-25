# fa19-516-160 E.Cloudmesh.Common.1
# Task :  Develop a program that demonstrates the use of banner, HEADING, and VERBOSE.

from cloudmesh.common.variables import Variables
# Import CM console package

from cloudmesh.common.console import Console

# Check types of CM logs messages
tstmsg = "This is my test message"

Console.ok(tstmsg) # prints a green message
Console.error(tstmsg) # prints a red message proceeded with ERROR
Console.msg(tstmsg) # prints a regular black message

# Error message traceback in the output
Console.error(tstmsg, prefix=True, traceflag=True)

# ---------- # ---------------#

# Import Cloud Mesh utility package to display banner in console
from cloudmesh.common.util import banner

# Create Banner
banner("Engineering Cloud Computing E516 | Shreyans Jain | fa19-516-160")

# ---------- # ---------------#

# Import Cloud Mesh utility package to display heading in console
from cloudmesh.common.util import HEADING

# Create Heading
HEADING()
print ("Engineering Cloud Computing E516 | Shreyans Jain | fa19-516-160")

# ---------- # ---------------#

# Import Cloud Mesh  debug package to  import VERBOSE for print logs
from cloudmesh.common.debug import VERBOSE

# Create sample verbose log output

m = { "key1": "value1" }
VERBOSE(m)

#---------------------------#


