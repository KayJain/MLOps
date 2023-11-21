def check(word):
  if word == word[::-1]:
    return True
  else:
    return False

# test 
check("apple")
