pages = list(map(int, input("Enter page sequence (space separated): ").split()))
frames = int(input("Enter number of frames: "))
memory = []
page_faults = 0
hits = 0
index = 0
fault=0

for page in pages:
    if page not in memory:
        if len(memory) < frames:
                memory.append(page)
        else:
            memory[index] = page
            index = (index + 1) % frames
        page_faults += 1
        fault = "Miss"
    else:
            hits += 1
            fault = "Hit"

    print(f"Page: {page} -> Frames: {memory} -> {fault}")

total = len(pages)
hit_ratio = hits / total
miss_ratio = page_faults / total

print("\nTotal Pages:", total)
print("Total Hits:", hits)
print("Total Misses (Faults):", page_faults)
print("Hit Ratio:", round(hit_ratio, 2))
print("Miss Ratio:", round(miss_ratio, 2))

# input:1 2 3 4 1 2 5 1 2 3 4 5
#frame: 3