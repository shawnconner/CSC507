#!/bin/bash

SECONDS=0

# For loop that will write 1000 random numbers to a file named file1.txt
for i in {1..1000000}
do
    echo $RANDOM >> file1.txt
done

echo "Execution time: $SECONDS seconds"
