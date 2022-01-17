import tasks
import time
from service import Service

if __name__ == "__main__":
    print("--- starting tasks")
    task_add = tasks.add.delay(1, 2)
    service = Service(2)
    task_multiply = tasks.multiply.delay(service=service, y=2)
    print(f"--- sleep 2 sec")
    time.sleep(2)
    print(f"--- task add: {task_add.get()}")
    print(f"--- task multiply: {task_multiply.get()}")
