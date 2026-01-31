import random
import time
import multiprocessing

# Generate random integers and write to file
# count: number of random integers to generate
# filename: output file path
def generate_random_numbers(count, filename):
    with open(filename, 'w') as f:
        for _ in range(count):
            f.write(f"{random.randint(0, 32767)}\n")

# Main entry point
# base_filename: base name for output files
def main(base_filename):
    start = time.time()
    
    total_count = 10000000
    num_processes = 8
    count_per_process = total_count // num_processes
    
    processes = []
    
    for i in range(num_processes):
        filename = f"{base_filename}_{i}.txt"
        process = multiprocessing.Process(target=generate_random_numbers, args=(count_per_process, filename))
        processes.append(process)
        process.start()
    
    for process in processes:
        process.join()
    
    end = time.time()
    print(f"Execution time: {end - start} seconds")

if __name__ == "__main__":
    main("file2_threaded")
