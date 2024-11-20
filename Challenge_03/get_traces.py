# Small script to get all the traces from the web
traces_list = []
with open('Challenge_03/trace.txt') as file:
    for line in file:
        traces_list.append(line.strip().split())

print(traces_list)