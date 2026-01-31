import random
import time
import multiprocessing

# Generate random integers and write to file
# count: number of random integers to generate
# filename: output file path
# process_id: process identifier
def generate_random_numbers(count, filename, process_id):
    numbers = []
    for _ in range(count):
        numbers.append(str(random.randint(0, 32767)))
    return (process_id, numbers)

# Main entry point
# filename: output file path
def main(filename):
    start = time.time()
    
    total_count = 10000000
    num_processes = 8
    count_per_process = total_count // num_processes
    
    with multiprocessing.Pool(num_processes) as pool:
        results = pool.starmap(generate_random_numbers, [(count_per_process, filename, i) for i in range(num_processes)])
    
    with open(filename, 'w') as f:
        for _, numbers in sorted(results):
            f.write('\n'.join(numbers) + '\n')
    
    end = time.time()
    print(f"Execution time: {end - start} seconds")

if __name__ == "__main__":
    main("file2_threaded.txt")
