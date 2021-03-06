def max(x,y) : return x if x>y else y
def min(x,y) : return x if x<y else y

class Num:
  def __init__(i,name):
    i.mu,i.n,i.m2,i.up,i.lo,i.name = 0,0,0,-10e32,10e32,name
  def add(i,x):
    i.n += 1
    x = float(x)
    if x > i.up: i.up=x
    if x < i.lo: i.lo=x
    delta = x - i.mu
    i.mu += delta/i.n
    i.m2 += delta*(x - i.mu)
    return x 
  def sub(i,x):
    i.n   = max(0,i.n - 1)
    delta = x - i.mu
    i.mu  = max(0,i.mu - delta/i.n)
    i.m2  = max(0,i.m2 - delta*(x - i.mu))
  def sd(i):
    return 0 if i.n <= 2 else (i.m2/(i.n - 1))**0.5
  def show(i):
    print i.name + " - Mean: " + str(i.mu) + "; Standard Deviation: " + str(i.sd())
    