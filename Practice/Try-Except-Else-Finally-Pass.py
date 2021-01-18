# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 20:08:14 2021

@author: SethHarden
"""

try:
    f = open("corrupt_file.txt")
    if f.name == "corrupt_file.txt":
        raise Exception
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print("Error!")
else:
    print(f.read())
    f.close()
finally:
    print("Executing Finally...")