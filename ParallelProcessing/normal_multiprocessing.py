from multiprocessing import Process
import time

def invoke_command(item):
    # Replace this with the actual command you want to invoke
    print(f"\n {round(time.time() - current_time, 20)} Processing {item}")

current_time = time.time()

if __name__ == "__main__":
    items = ["item1", "item2", "item3", "item4"]

    processes = []
    for item in items:
        process = Process(target=invoke_command, args=(item,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()