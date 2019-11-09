#Method 1
def reverse(string):
    string = string[::-1]
    return string

#Method 2
def reverse(string):
  str = ""
  for i in string:
    str = i + str
  return str