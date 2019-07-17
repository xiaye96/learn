#返回值加1，装饰器实现
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

#多个装饰器堆叠实用
# @plus1
# @plus1
# @plus1
# def root(x):
#   return x**0.5

# root(4) #返回5

#装饰器只能接收一个参数，若想返回值加2，就需要创建另一个装饰器。
#因为没有机制能参数化装饰器，让其添加n，而不是固定的添加1，装饰器工厂能够实现这一个功能。
#def plus_n(n):
#     def dec(f):
#       def wrapper(*args,**kwargs):
#         return f(*args,**kwargs)+1
#       return wrapper
#     return dec
#装饰器工厂返回装饰器dec()的结果，而装饰器dec返回一个封装函数
#@plus_n(6)
#def root(x):
# return x**0.5

#root(4) #返回值为8
