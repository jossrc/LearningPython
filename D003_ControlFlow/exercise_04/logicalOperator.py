p = True
q = False

result = p and q
print("Result : " + str(result))
  
result = not ((p and q) or (not p or q))
print("Result : " + str(result))
