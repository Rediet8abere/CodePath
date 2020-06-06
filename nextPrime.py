# Input: 2
# Output: 5
# prime number is only divisible by 1 and itself
def nextPrime(num):
  # keep looping until a number is only divisible by 1 and itself by adding 2
  # when it is divisible by 1 and itself return the number
  # addTwo = num + 2 #25
  # addFour = num + 4 #27
  is_next_prime = False
  next_prime = num + 1
  # 3, 5, 7, 9
  while not is_next_prime:
    for i in range(2, 10):
      if next_prime == i:
        continue
      else:
        if next_prime%i == 0:
          next_prime += 1
          break
    if i == 9:
      is_next_prime = True
      return next_prime
print(nextPrime(109))
