 def reverseS(s):
  # revS = ""
  revS = []
  # revS leh
  # iterate over string
  for i in range(len(s)):
    # prepend the value to a new variable
    revS.append(s[len(s)-(i+1)])
  return ''.join(revS)
print(reverseS("hi, codepath"))
