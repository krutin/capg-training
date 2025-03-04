import time
import queue
import threading

# def single_task():
#     print("task started")
#     time.sleep(2)
#     print("task completed")

# thread = threading.Thread(target=single_task)
# thread.start()
# thread.join()
# print("main thread execution completed")
#______________________________________________________________________

# def task1():
#     for i in range(1,10,2):
#         print("odd number : ",i)
#         time.sleep(1)

# def task2():
#     for i in range(2,10,2):
#         print("even number : ",i)
#         time.sleep(1)

# thread1 = threading.Thread(target=task1)
# thread2 = threading.Thread(target=task2)

# thread1.start()

# thread2.start()

# thread1.join()

# thread2.join()
#______________________________________________________________________


# def download_file(file_name):
#     print(f"starting download: {file_name}")
#     time.sleep(3)
#     print(f"Download complete: {file_name}")

# files = ["file1.zip", "file2.zip", "file3.zip"]
# threads = []

# for file in files:
#     thread = threading.Thread(target=download_file, args=(file,))
#     threads.append(thread)
#     thread.start()

# for thread in threads:
#     thread.join()


# print("all downloads complete.")
#______________________________________________________________________


# def prodeucer(q):
#     for i in range(5):
#         time.sleep(1)
#         q.put(i)
#         print(f"Produced: {i}")

# def consumer(q):
#     while True:
#         item = q.get()
#         if item is None:
#             break
#         print(f"Consumed : { item}")
#         time.sleep(2)
# q = queue.Queue()
# prodeucer_thread = threading.Thread(target=prodeucer,args = (q,))
# consumer_thread = threading.Thread(target=prodeucer,args = (q,))

# prodeucer_thread.start()
# consumer_thread.start()

# prodeucer_thread.join()
# q.put(None)
# consumer_thread.join()

#______________________________________________________________________

# class TicketBooking:
#     def __init__(self,available_tickets):
#         self.available_tickets = available_tickets
#         self.lock = threading.Lock()

#     def book_ticket(self,name):
#         print(f"{name} is trying to book a ticket..")
#         with self.lock:
#             if self.available_tickets > 0:
#                 time.sleep(1)
#                 self.available_tickets -= 1
#                 print(f"{name} successfully booked a ticket .Remaining: {self.available_tickets}")
#             else:
#                 print(f"Sorrry {name}, no tickets available")
    
# booking_system = TicketBooking(1)

# threads = []

# users = ["Alice", "Bob"]
# for user in users:
#     t = threading.Thread(target=booking_system.book_ticket, args=(user,))
#     threads.append(t)
#     t.start()

# for t in threads:
#     t.join()
#______________________________________________________________________

# def background_task():
#     for i in range(5):
#         print(f"daemon thread running {i}")
#         time.sleep(2)

# t = threading.Thread(target = background_task,daemon = True)
# t.start()

# print("Main program exits, daemon thread will be klled automatically")
#______________________________________________________________________




