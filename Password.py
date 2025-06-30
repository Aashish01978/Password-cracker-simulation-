# Password-cracker-simulation-
import itertools
import string
import time

# Set of characters to try (digits + punctuation)
chars = string.digits + string.punctuation  # Include more characters

# The password to be cracked
password = "12@"  # Example password

# Maximum length of the password to try
max_length = 4  # Increase for longer passwords

# Record start time
start_time = time.time()

found = False

# Try all lengths from 1 to max_length
for length in range(1, max_length + 1):
    if found:
        break
    # Try all combinations of the given length
    for combination in itertools.product(chars, repeat=length):
        candidate = "".join(combination)
        print("Trying password:", candidate)
        if candidate == password:
            end_time = time.time()
            print("Password found:", candidate)
            print("Time taken:", end_time - start_time, "seconds")
            found = True
            break

if not found:
    print("Password not found within the specified parameters.")
