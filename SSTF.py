requests = list(map(int, input("Enter list: ").split()))

head = requests[0]
queue = requests[1:]

current = head
total = 0
path = [head]
calc = []

while len(queue) > 0:
    nearest = queue[0]
    min_dist = abs(nearest - current)

    for r in queue:
        dist = abs(r - current)
        if dist < min_dist:
            min_dist = dist
            nearest = r

    calc.append(f"|{nearest}-{current}|")
    total = total + min_dist

    current = nearest
    path.append(nearest)
    queue.remove(nearest)

print("Path:", *path)
print("Total Distance Calculation:")
print(" + ".join(calc))
print("=", total)