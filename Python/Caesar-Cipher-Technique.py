# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 14:00:32 2020

@author: SethHarden
"""

#A python program to illustrate Caesar Cipher Technique 
def encrypt(text,s): 
    result = "" 
  
    # traverse text 
    for i in range(len(text)): 
        char = text[i] 
  
        # Encrypt uppercase characters 
        if (char.isupper()): 
            #result += chr((ord(char) + s-65) % 26 + 65) 
            result += chr((ord(char) + s)) 
  
        # Encrypt lowercase characters 
        else: 
            result += chr((ord(char) + s)) 
  
    return result 
  
#check the above function 
text = "Aa"
s = 4
print ("Text  : " + text) 
print ("Shift : " + str(s))
print ("Cipher: " + encrypt(text,s))





import math
# Add any extra import statements you may need here
"""

Accept a string and a rotation factor

encryptThis(string, factor)

Encrypt the string

Setup our encryption methods.

First, lets traverse through our "string"
Create a for loop that attaches the range(len(text)) objects to it.

for i in range(len(text))

Setup an object and attach text[i] (the current letter we are encrypting)

We need to make sure we are looking at a character not another symbol. We can check this with the .isalpha() 

So BEFORE we run the encrption method we need to check 

We need to devide the number

Now lets run our encryption on that letter!

cipher += 

        
        







Return the encypted string

"""

# Add any helper functions you may need here


def rotationalCipher(input, rotation_factor):
  # Write your code here
  output = ""
  factor = int(rotation_factor)
  #traverse the input
  for i in range(len(input)):
    char = input[i]
    
    if (char.isupper()) and (char.isalpha()):
      output += chr((ord(char) + factor - 65) % 26 + 65) 
    elif (char.islower()) and (char.isalpha()):
      output += chr((ord(char) + factor - 97) % 26 + 97)
    elif (char.isdigit()):
      output += chr((ord(char) + factor - 48) % 10 + 48)
    else:
      output += char
    
  return output





# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom, but they are otherwise not editable!

def printString(string):
  print('[\"', string, '\"]', sep='', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  result = False
  if expected == output:
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printString(expected)
    print(' Your output: ', end='')
    printString(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  input_1 = "All-convoYs-9-be:Alert1."
  rotation_factor_1 = 4
  expected_1 = "Epp-gsrzsCw-3-fi:Epivx5."
  output_1 = rotationalCipher(input_1, rotation_factor_1)
  check(expected_1, output_1)

  input_2 = "abcdZXYzxy-999.@"
  rotation_factor_2 = 200
  expected_2 = "stuvRPQrpq-999.@"
  output_2 = rotationalCipher(input_2, rotation_factor_2)
  check(expected_2, output_2)

  # Add your own test cases here
  