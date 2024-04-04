from queue import Queue

k = Queue(maxsize=3)  # unbounded queue
k.put('a') 
k.put('b')  
k.put('c')   
print(k.qsize())
print(list(k.queue))