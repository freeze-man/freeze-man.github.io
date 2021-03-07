import time

while True:
  localtime = time.localtime()
  result = time.strftime("%I:%M:%S %p", localtime)
  print(result, end="", flush=True)
  print("\r", end="", flush=True)
  time.sleep(1)

# while True:
#  localtime = time.localtime()
#  result = time.strftime("%I:%M:%S %p", localtime)
#  print(result)
#  time.sleep(1)