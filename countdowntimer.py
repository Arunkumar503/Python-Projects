
import time
minutes=float(input("enter the time in minutes:"))
seconds=int(minutes*60)
while seconds:
    min,sec=divmod(seconds,60)
    timer=f"{min:02d}:{sec:02d}"
    time.sleep(1)
    seconds-=1
    print(timer)
print("time's up")