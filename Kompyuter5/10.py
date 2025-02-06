import os
import time

def ocurmek():
    wagt = int(input("Nace sekuntdan: "))
    os.system(f"shutdown /s /t {wagt}")
    for i in range(wagt, 0, -1):
        print(f"Shutting down in {i} seconds...")
        time.sleep(1)

def restart():
    wagt = int(input("Nace sekuntdan: "))
    os.system(f"shutdown /r /t {wagt}")
    print(f"Kompyuter {wagt} sekuntdan son restart bolar!")
    for i in range(wagt, 0, -1):
        print(f"Shutting down in {i} seconds...")
        time.sleep(1)
    
def buyrugy_yzyna_almak():
    os.system("shutdown /a")
    print("Buyruk yzyna alyndy!")
    

def main():
    while True:
        print("1. Shut down\n2. Restart\n3. Return\n4. Exit")
        choice = input("Saylan: ")
        if choice == '1':
            ocurmek()
        elif choice == '2':
            restart()
        elif choice == '3':
            buyrugy_yzyna_almak()
        elif choice == '4':
            print("Programmany ulalanynyz ucin sagbolun!")
            break
        else:
            print("Yalnys buyruk!")

main()