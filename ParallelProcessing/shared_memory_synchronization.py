from multiprocessing import Process, Value
import time


def invoke_command(item, start_flag):
    while start_flag.value == 0:
        pass  # Wait for the start signal
    # Replace this with the actual command you want to invoke
    print(f"\n{round(time.time() - current_time, 8)} Processing {item}")


current_time = time.time()

if __name__ == "__main__":
    items = ["item1", "item2", "item3", "item4"]
    start_flag = Value("i", 0)  # Shared flag to synchronize start

    processes = []
    for item in items:
        process = Process(target=invoke_command, args=(item, start_flag))
        processes.append(process)
        process.start()

    # Signal all processes to start
    start_flag.value = 1

    for process in processes:
        process.join()
