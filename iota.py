print "Obtain unloaded 6-sided dice."
print "It is your responsibility to ensure the evenness and fairness of these dice."
print "Enter your rolls (1-6). Do this 64 * 4 times to create a private key."
print "Each letter in the private key ranges from A-Z + 9 (27 character range)."
print "Each letter is determined by a 3 digit number in a ternary system (0,1,2)."
print "Each digit is determined by the roll of the dice, minus 1, mod 3."

hexes = []

def get_hex(bits, sum):
  if bits == 3:
    return sum
  
  print "> enter roll result (1-6)"
  x = int(raw_input())
  if x < 1 or x > 6:
    print "ERROR: Bad roll"
    return get_hex(bits, sum)

  x = x - 1
  value = x % 3
  return get_hex(bits + 1, sum + ((3 ** bits) * value))

lookup = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "9"];

while len(hexes) < 81:
  num = get_hex(0, 0)    
  hexes.append(lookup[num])

print(hexes)
