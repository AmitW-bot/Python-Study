log_file = [
   "INFO: Operation successful",
   "ERROR: line 43-File not found",
   "DEBUG: Connection established",
   "ERROR: port-4385 Database connection failed",
]

for line in log_file:
    if "ERROR" in line:
        print(line)