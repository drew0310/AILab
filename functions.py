#this file contains all boolean function... and other utilities
def NOT(a):
  if a == "1":
    return "0"
  elif a == "0":
    return "1"

def AND(a,b):
  if a=="1" and b=="1":
    return "1"
  else:
    return "0"


def OR(a,b):
  if a == "0" and b == "0":
    return "0"
  else: 
    return "1"
def IM(b,a):
  return OR(NOT(a),b)
def BI(a,b):
  return AND(IM(a,b),IM(b,a))

def genBNos(n):
  res = [""] * (2**n)
  count = 0
  bit = "0"
  freq = 1
  while(count<n):
    for i in range(0,len(res)):
      if((i+1)%freq==0):
        if bit == "0": 
          bit = "1"
        else:
          bit = "0"
        #print("i: ",i+1,"Bit: ",bit)
      res[i] = bit + res[i]
    freq = freq*2
    count = count + 1
  return res

def genSyms(exp):
  dict = {}
  count = 0
  for char in exp:
    if char.isalpha() and char not in dict:
        dict[char] = count
        count = count + 1
  return dict

def genExps(exp):
  SymList = genSyms(exp)
  NoList = genBNos(len(SymList))
  for i in range(len(NoList)):
    temp = NoList[i]
    NoList[i] = exp
    for ele in SymList:
      NoList[i] = NoList[i].replace(ele, temp[SymList[ele]])
  return NoList

def isTaut(RS):
  for rs in RS:
    if rs == "0":
      return False
  return True