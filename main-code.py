print("wtf?")

import balance
print("WTF??")
import sys

print("check...")

if len(sys.argv) < 2:
    print("argument required")
    exit()
    
test = Balance('(', ')')

test_value = test.match(sys.argv[1])

print("HI")

if test_value:
    print("input has balanced tokens")

else:
    print("input DOES NOT HAVE balanced tokens")
