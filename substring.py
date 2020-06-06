# Examples:
# Input: laboratory, rat
# Output: true

# have two pointers
# keep looping over the string until substring at index 0 matches a char from string
# when it matches go to the next char
# string : laboraory
#                ^
# sub: rat
#        ^
def subString(string, subString):

  lenSubS = len(subString)
  lenS = len(string)
  if lenS < lenSubS:
    return 0

  j = 0
  count = 0
  for i in range(lenS):
    if string[i] == subString[j]:
      j += 1
    elif j < lenSubS and string[i] != subString[j]:
      j = 0
    if j == lenSubS:
      count += 1
      j = 0
  return count

# cat, meow
print(subString("cat", "abra"))
