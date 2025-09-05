import time

a = int(input("enter time in sec:"))
for x in reversed(range(1, a + 1)):
    sec = x % 60
    min = int((x / 60)) % 60
    hrs = int((x / 3600)) % 60
    print(f"{hrs:02}:{min:02}:{sec:02}")
    time.sleep(1)
print("...........time's up............")
