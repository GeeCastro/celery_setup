import tasks
import time

print("starting task")
res = tasks.add.delay(1, 2)
time.sleep(2)
print(res.get())
