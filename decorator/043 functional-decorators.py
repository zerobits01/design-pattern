import time

def time_it(func):
  def wrapper():
    start = time.time()
    result = func()
    end = time.time()
    print(f'{func.__name__} took {int((end-start)*1000)}ms')
  return wrapper

# why did we add this as deco but not in the function?
# this is because the responsibilty of this function is unique
# and this is a repeated job which is not the function itself responsability


@time_it
def some_op():
  print('Starting op')
  time.sleep(1)
  print('We are done')
  return 123

if __name__ == '__main__':
  # some_op()
  # time_it(some_op)()
  some_op()