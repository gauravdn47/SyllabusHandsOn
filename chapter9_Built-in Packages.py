# Writing a multi-threaded countdown timer program
import threading
import time

exitFlag = 0

class my_thread (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
   def run(self):
      print("Starting " + self.name)
      print_time(self.name, 5, self.counter)
      print("Exiting " + self.name)

def print_time(threadName, counter, delay):
   while counter:
       if exitFlag:
           threadName.exit()
       time.sleep(delay)
       print("%s: %s" % (threadName, time.ctime(time.time())))
       counter -= 1

thread1 = my_thread(1, "Thread-1", 1)
thread2 = my_thread(2, "Thread-2", 2)

# Start new Threads
thread1.start()
thread2.start()

print("Exiting Main Thread")



