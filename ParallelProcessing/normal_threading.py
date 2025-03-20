import threading
import time

def invoke_command(item):
    # Replace this with the actual command you want to invoke
    time.sleep(0.5)
    print(f"\n{round(time.time() - current_time, 4)} Processing {item}")

items = ["item1", "item2", "item3", "item4"]
current_time = time.time()

print("\nSequential processing\n")
for item in items:
    invoke_command(item)
    

print("\nParallel processing\n")
threads = []
for item in items:
    thread = threading.Thread(target=invoke_command, args=(item,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()