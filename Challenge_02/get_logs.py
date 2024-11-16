# Small script to get all the logs from the web
logs_list = []
with open('Challenge_02/logs.txt') as topo_file:
    for line in topo_file:
        logs_list.append(line.strip())

# print(logs_list) to copy and paste into the main script
