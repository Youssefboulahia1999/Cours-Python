#coding:utf-8
import time
import threading


def process_one():
    i = 0
    while i < 3: 
        print("oooooo")
        time.sleep(0.3)
        i+=1


def process_two():
    i = 0
    while i < 3: 
        print("xxxxxx")
        time.sleep(0.3)
        i+=1

#creeation 
th1 = threading.Thread(target=process_one)
th2 = threading.Thread(target=process_two)

#demare
th1.start()
th2.start()
#attendre quil finissent 
th1.join()
th2.join()

print("fin du programme")

#creation d'un veroul
my_lock = threading.RLock()

#myprocess herite de thread
class MyProcess(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run (self):
            i = 0
            while i < 3: 
                #le lock va faire exactement le
                # meme que le joint il fait attedre l'excution
                with my_lock:
                    letters = "ABC"
                    for lt in letters:
                        print(lt)
                        time.sleep(0.3)
                i+=1

#creeation 
th3 = MyProcess()
th4 = MyProcess()

#demare
th3.start()
th4.start()
#attendre quil finissent 
th3.join()
th4.join()

print("fin du programme")