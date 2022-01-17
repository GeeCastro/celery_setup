import tasks
import time

print("--- starting task")
res = tasks.add.delay(1, 2)
print(f"--- sleep 2 sec")
time.sleep(2)
print(f"--- task result 1+2={res.get()}")
