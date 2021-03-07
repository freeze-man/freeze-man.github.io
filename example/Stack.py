class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()


s = Stack()
while True:
    print('push<value>')
    print('pop')
    print('quit')
    do = input('What would you like to do? ').split()
    operation = do[0].strip().lower()
    if operation == 'push':
        s.push(int(do[1]))
    elif operation == 'pop':
        if s.is_empty():
            print('Stack is empty')
        else:
            print('Popped value:', s.pop())
    elif operation == 'quit':
        break

"""
from queue import LifoQueue
s = LifoQueue()
  
s.put('eat')
s.put('sleep')
s.put('code')
  
>>> s
<queue.LifoQueue object at 0x108298dd8>
  
>>> s.get()
'code'
>>> s.get()
'sleep'
>>> s.get()
'eat'
  
>>> s.get_nowait()
queue.Empty
  
>>> s.get()
# Blocks / waits forever...
"""
