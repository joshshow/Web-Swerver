#!/bin/python
import subprocess
subprocess.call(["ls"])
print
print
print

#subprocess.call(["sudo","apachectl","start"])
subprocess.call(["sudo","apachectl","restart"])
