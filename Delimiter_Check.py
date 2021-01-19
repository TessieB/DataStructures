import sys # for sys.argv, the command-line arguments
from Stack import Stack

def delimiter_check(filename):
  check = Stack()
  k = open(filename, "r")
  char = list(k.read())
  for i in range(len(char)):
    if char[i] is '(' or char[i] is '[' or char[i] is '{':
      check.push(char[i])
    elif char[i] is ')' or char[i] is ']' or char[i] is '}':
      l = check.pop()
      if l is '(':
        if char[i] is not ')':
          return False
      elif l is '[':
        if char[i] is not ']':
          return False
      elif l is '{':
        if char[i] is not '}':
          return False
      elif len(check) == 0:
        return False
  if len(check) > 0:
    return False
  return True


if __name__ == '__main__':
  # The list sys.argv contains everything the user typed on the command 
  # line after the word python. For example, if the user types
  # python Delimiter_Check.py file_to_check.py
  # then printing the contents of sys.argv shows
  # ['Delimiter_Check.py', 'file_to_check.py']
  if len(sys.argv) < 2:
    # This means the user did not provide the filename to check.
    # Show the correct usage.
    print('Usage: python Delimiter_Check.py file_to_check.py')
  else:
    if delimiter_check(sys.argv[1]):
      print('The file contains balanced delimiters.')
    else:
      print('The file contains IMBALANCED DELIMITERS.')


