def isPalindrome(s):
  print(len(s))
  left = 0
  right = len(s)-1
  # iterrate through the string from left and right
  while left < right:
    if not s[left].isalpha() and not s[right].isalpha():
      left += 1
      right -= 1
    elif not s[right].isalpha():
      right -= 1
    elif not s[left].isalpha():
      left += 1
    elif s[left].lower() == s[right].lower():
        left += 1
        right -= 1
    else:
      return 0
  return 1
# left: 0
# right: 30

# print(isPalindrome("A man, a plan, a canal, Panama."))
print(len(""))
print(len(" "))
