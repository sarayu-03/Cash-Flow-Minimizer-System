#!/bin/bash

# Compile the C++ program if not already compiled
# Check if the correct number of arguments is provided
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <banks_file> <transactions_file>"
    exit 1
fi

# Run the compiled program with the provided arguments
./static/cash_flow "$1" "$2"

