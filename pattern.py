#printing pattern getting values from the user

from __future__ import print_function #python3 to python2 compatibility
rows = int(input("Enter the number:"))
for i in range(1,rows+1):
    for j in range(1,i+1):
	print(i, end='')
    print()
    
