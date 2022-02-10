def gcd(a, b):
  if a<b:
    t = b
    b = a
    a = t
  m = a % b
  while m != 0:
    a = b
    b = m
    m = a % b
  return b

def ZmZ(m):
  print("ℤ/"+str(m)+"ℤ")
  s = "|  +  ||"
  t = "––––––||"
  u = "––––––––"
  for i in range (0, m):
    s += str(i).rjust(3) + " |"
    t += "–––––"
    u += "–––––"
  print(u)
  print(s)
  print(t)
  for j in range (0, m):
    s = "| "+ str(j).rjust(2)+"  ||"
    for i in range (0, m):
      x = (i+j) % m
      s += str(x).rjust(3)+" |"
    print(s)
  print(u)

  s = "|  x  ||"
  t = "––––––||"
  for i in range (0, m):
    s += str(i).rjust(3) + " |"
    t += "–––––"
  print(s)
  print(t)
  for j in range (0, m):
    s = "| "+ str(j).rjust(2)+"  ||"
    for i in range (0, m):
      x = (i*j) % m
      s += str(x).rjust(3)+" |"
    print(s)
  print(u)

  print("(ℤ/"+str(m)+"ℤ)* =")
  rslt = []
  for a in range (1, m):
    if (gcd(a, m) == 1):
      rslt.append(a)
  print(rslt)
  s = "|  .  ||"
  t = "––––––||"
  u = "––––––––"
  ln = len(rslt)
  for i in range (0, ln):
    s += str(rslt[i]).rjust(3) + " |"
    t += "–––––"
    u += "–––––"
  print(u)
  print(s)
  print(t)
  for j in range (0, ln):
    s = "| "+ str(rslt[j]).rjust(3)+" ||"
    for i in range (0, ln):
      x = (rslt[i]*rslt[j]) % m
      s += str(x).rjust(3)+" |"
    print(s)
  print(u)
  return rslt

#def fastpow(x, exp, m):
#  if (exp == 1): return x
#  elif (exp % 2):
#    return (x * fastpow(x, exp - 1, m)) % m
#  else:
#    return fastpow((x * x) % m, exp / 2, m)

def blocks(x):
  i = 0
  rslt = []
  while (x > 0):
    if (x % 2):
      rslt.append(i)
    i += 1
    x = int(x / 2)
  return rslt

def fastpow(x, exp, m):
  b = blocks(exp)
  sum = 1
  j = len(b)
  for i in range (0, j):
    #p2 = pow(2, b[i])
    #p3 = pow(x, p2)%1000
    #print("b = " + str(b[i]) + ", p2 = " + str(p2) + ", p3 = " + str(p3))
    sum *= pow(x, pow(2, b[i]))%1000
  return sum%1000

def primeFactors(n):
  counts = {}
  i = 2
  while i<=n:
    if n%i == 0:
      n= n/i
      counts[i] = counts.get(i, 0)+1
    else:
      i+=1
  return counts





if __name__ == '__main__':
  test = gcd(2024, 748) == 44
  if test:
    print("GCD: pass")
  else:
    print("GCD: fail")
  expected = [1, 5, 7, 11, 13, 17, 19, 23]
  test = ZmZ(24)
  if test == expected:
    print("ZmZ: pass")
  else:
    print("ZmZ: fail")
  test = fastpow(3,218,1000) == 489
  if test:
    print("fastpow: pass")
  else:
    print("fastpow: fail")
  test = primeFactors(1728) == {2: 6, 3: 3}
  if test:
    print("primeFactors: pass")
  else:
    print("primeFactors: fail")
