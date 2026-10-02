import time
import os
os.system(r"title v1.0.0")
while True:
    try:
        n=int(input(f"请你输入你要在考拉兹猜想里计算的数字:"))
        N=[]
        while True:
            print(f"现在是{n}")
            N.append(n)
            if n==1:
                break
            elif n & 1:
                n=3*n+1
            else:
                n=n//2
        print(N)
        print(f"算好了")
        time.sleep(1)
        while True:
            a=input(f"你还要继续吗?(Y/N)").strip().lower()
            if a=="y":
                break
            elif a=="n":
                print(f"ok")
                exit()
            else:
                pass
    except ValueError:
        print(f"输入无效,请输入一个整数")