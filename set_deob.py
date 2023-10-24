#  _  _  +     _|  _   _  |_
# _) (/_ | -- (_| (/_ (_) |_) v.0.0.1
# 

import os
import re
import sys

# Check if the correct number of command-line arguments is provided
if len(sys.argv) != 3:
    print("Usage: python deobfuscate.py <set_file> <obfuscated_file>")
    sys.exit(1)

set_file_path = sys.argv[1]
obfuscated_file_path = sys.argv[2]

# Read the "set" list from the provided file
with open(set_file_path, 'r') as set_file:
    set_list = {}
    for line in set_file:
        line = line.rstrip('\n')  # Remove only the newline character
        if line:
            # Split on the first equal sign
            first_equal_index = line.find('=')
            if first_equal_index != -1:
                variable = line[:first_equal_index]
                value = line[first_equal_index + 1:]
                set_list[variable] = value

# Read the obfuscated batch script from the provided file
with open(obfuscated_file_path, 'r') as malware_file:
    obfuscated_code = malware_file.read()

# Use regular expressions to replace variables in the obfuscated code
pattern = r'%\w+%'
def replace_variable(match):
    variable = match.group()[1:-1]  # Remove '%' characters
    return set_list.get(variable, match.group())

deobfuscated_code = re.sub(pattern, replace_variable, obfuscated_code)

# Generate the output deobfuscated file path
base_filename, file_extension = os.path.splitext(obfuscated_file_path)
deobfuscated_file_path = base_filename + '_deob' + file_extension

# Write the deobfuscated code to the output file
with open(deobfuscated_file_path, 'w') as deobfuscated_file:
    deobfuscated_file.write(deobfuscated_code)

print("Deobfuscation completed. Deobfuscated code saved in '{}'.".format(deobfuscated_file_path))
