# import time

# def timerCounter(func):
#     def wrapper(*args):
#         start=time.time()
#         result=func(*args)
#         timing=time.time()-start
#         print("Time ",timing)
#         return result
#     return wrapper

# @timerCounter
# def add(x,y):
#     return x+y

# add(5,10)

# class CountTime:
#     def __init__(self,func):
#         self.func=func
#         self.num_calls = 0

#     def __call__(self):
#         self.num_calls += 1
#         print(f"This is executed {self.num_calls} times")
#         return self.func()
# @CountTime
# def say_hello():
#     print("Hello")


# say_hello()
# say_hello()
# say_hello()
# say_hello()

def XD():
    while 0>-1:
        print("XD")

XD()