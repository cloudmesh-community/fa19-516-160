# fa19-516-156 E.Cloudmesh.Common.5
# Develop a program that demonstartes the use of cloudmesh.common.StopWatch.

from cloudmesh.common.StopWatch import StopWatch
from time import sleep
StopWatch.start("test")
sleep(2)

from cloudmesh.common.console import Console
from cloudmesh.common.util import banner, HEADING
from cloudmesh.common.util import HEADING
from cloudmesh.common.debug import VERBOSE
from cloudmesh.common.variables import Variables

banner("Cloud Programming")

mesg = "console test"

# test Console
Console.ok(mesg)
Console.msg(mesg)

## Print the Heading, with ###
HEADING("Heading")

##VERBOSE
variables = Variables()

variables['debug'] = True
variables['trace'] = True
variables['verbose'] = 10

m = dict(key1="value1", key2="value2", key3="value3")
VERBOSE(m)

## one more timer sleep
sleep(1)

StopWatch.stop("test")
print (StopWatch.get("test"))

## Clear timer variable
StopWatch.clear()
print (StopWatch.get("test"))