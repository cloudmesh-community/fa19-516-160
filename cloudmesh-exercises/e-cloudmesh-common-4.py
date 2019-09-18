# fa19-516-160
# E.Cloudmesh.Common.4
# Task :  Develop a program that demonstrates the use of cloudmesh.common.Shell.

from cloudmesh.common.Shell import Shell

# Check Python Version
version = Shell.check_python()
print(version)

working_dir = Shell.execute('pwd')
print(working_dir)

#Code reference Introduction to python : Gregor von Laszewski.: section 6.5