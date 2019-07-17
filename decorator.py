def plus1(f):
  def wrapper(*args,**kwargs):
    return f(*args,**kwargs)+1
  return wrapper

@plus1
def power(base,x):
  return base**x
power(4,2)


#@plus1
#def power(base,x):
#  return base**x

#上述代码与下述代码作用相同
#def power(base,x):
#  return base**x
#plus1=plus1(power)
