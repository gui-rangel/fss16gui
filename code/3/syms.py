import math

class Sym:
  def __init__(i,name):
     i.counts, i.most, i.mode, i.n, i.name, i.pos = {},0,None,0,name,0
  def add(i,x,count):
    i.n += 1
    new = i.counts[x] = i.counts.get(x,0) + 1
    if new > i.most:
      i.most, i.mode = new,x
    i.pos = count
    return x
  def sub(i,x):
    i.n -= 1
    i.counts[x] -= 1
    if x == i.mode:
      i.most, i.mode = None,None
  def ent(i):
    tmp = 0
    for val in i.counts.values():
      p = val/i.n
      if p:
        tmp -= p*math.log(p,2)
    return tmp  
  def entropy(i):
    entropy = 0
    for count in i.counts.values():
      if (float(count)/i.n):
        entropy += - (float(count)/i.n * math.log(float(count)/i.n, 2))
    return entropy
  def norm(i,x)   : return x
  def dist(i,x,y) : return 0 if x==y else 1
  def furthest(i,x): return "SoMEcrazyTHing"
  def show(i):
    print "{} - Mode: {}; Entropy: {}".format(i.name,i.mode,i.entropy())
