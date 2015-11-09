a = []
def hs(n):
   if (n == int(n) and (n > 0)):
    while (n != 1):
     a.append(n)
     if (n % 2 == 0):
        n = (n//2)
     else:
        n = (3*n + 1)
    if (n == 1):
     a.append(1)
     a.append(str(len(a)))
     return a
   else:
    return "n is not a valid input"
