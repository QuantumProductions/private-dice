print "Obtain 6-sided dice."
print "It is your responsibility to ensure the evenness and fairness of these dice."
print "Enter your rolls (1-6). Do this 64 * 4 times to create a private key."
print "Each letter in the private key ranges from 0-F, determined by the odd or evenness in a sequence of 4 dice using binary math."

hexes = []

def get_hex(bits, sum):
  if bits == 4:
    return sum
  
  print "> enter number"
  x = int(raw_input())
  if x < 1 or x > 6:
    print "ERROR: Bad roll"
    return get_hex(bits, sum)
  if x % 2 == 0:
    return get_hex(bits + 1, sum + (2 ** bits))
  else:
    return get_hex(bits + 1, sum)

lookup = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]

while len(hexes) < 4:
  num = get_hex(0, 0)    
  hexes.append(lookup[num])

print(hexes)

