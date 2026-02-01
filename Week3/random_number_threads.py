import random
import time
import threading


# Generate random integers and write to file
# count: number of random integers to generate
# filename: output file path
# results: shared list to store generated numbers
# start_idx: starting index for this thread
def generate_random_numbers(count, results, start_idx):
    for i in range(count):
        results[start_idx + i] = random.randint(0, 32767)


# Main entry point
# filename: output file path
def main(filename):
    start = time.time()

    total_count = 1000000
    num_threads = 4
    count_per_thread = total_count // num_threads

    results = [0] * total_count
    threads = []

    for i in range(num_threads):
        thread = threading.Thread(target=generate_random_numbers,
                                  args=(count_per_thread, results, i * count_per_thread))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    with open(filename, 'w') as f:
        for num in results:
            f.write(f"{num}\n")

    end = time.time()
    print(f"Execution time: {end - start} seconds")


if __name__ == "__main__":
    main("file2_threaded.txt")
