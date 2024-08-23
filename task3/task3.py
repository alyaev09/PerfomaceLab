import sys

file_values = sys.argv[1]
file_tests = sys.argv[2]
file_report = sys.argv[3]

values = {}

with open(file_values) as file:
    for line in file:
        if "\"id\"" in line:
            ourId = line[line.find(":") + 2:-2]
        if "\"value\"" in line:
            values[ourId] = line[line.find(":") + 2:-1]
with open(file_report, 'w') as report:
    with open(file_tests) as tests:
        for line in tests:
            if "\"id\"" in line:
                ourId = line[line.find(":") + 2:-2]
            if "\"value\"" in line:
                line = line.replace("\"\"", values[ourId])
            report.write(line)