def min_machines_required(start, end):
    events = [(time, 1) for time in start] + [(time, -1) for time in end]
    events.sort(key=lambda x: (x[0], -x[1]))  

    machines = 0
    max_machines = 0

    for event in events:
        machines += event[1]
        max_machines = max(max_machines, machines)

    return max_machines

start = [1,3,5,7,9]
end = [2, 4, 6, 9,12]
machines_required = min_machines_required(start, end)
print("Number of machines required:", machines_required)
