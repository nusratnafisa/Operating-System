# FCFS Disk Scheduling Algorithm in Python
requests = list(map(int, input("Enter the request queue: ").split()))
head = requests[0]

total_movement = 0
current_position = head
calc = []

print("Head Movement:\n")
    
for request in requests:
    distance = abs(request - current_position)
    total_movement += distance
        
    calc.append(f"|{request}-{current_position}|")
    print(f"{current_position} -> {request}  movement = {distance}")
        
    current_position = request

    print("\nTotal Distance Calculation:")
    print(" + ".join(calc))
    
    print("\nTotal Head Movement =", total_movement)





