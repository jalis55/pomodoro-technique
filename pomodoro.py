import time
import winsound

def countdown(t,status,beep=False):
    t1=t-10
    while t:
        if beep:
            if t<10:
                winsound.Beep(500,400)
            if t>t1:
                winsound.Beep(100,200)
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(status,timer, end="\r")
        time.sleep(1)
        t -= 1

def main():
    total_working_hour=int(input("Enter total hours to work:"))
    total_working_hour=total_working_hour*3600
    current_time=time.time()
    current_time=current_time+total_working_hour
    curr=time.ctime(current_time)
    print("Work will finish at:",curr)
    print(f"total working times:{total_working_hour}")
    while total_working_hour:
        countdown(1500,'Please Work till:')
        countdown(180,'Please take rest till:',beep=True)
        total_working_hour=total_working_hour-(1500+180)
        print("remains:",total_working_hour)

main()