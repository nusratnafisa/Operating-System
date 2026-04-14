pages = list(map(int, input("Enter page sequence (space separated): ").split()))
frames = int(input("Enter number of frames: "))

memory = []

miss = 0
hits = 0
fault = ""

# recent use track korar jonno dictionary
recent = {}

for i in range(len(pages)):
    page = pages[i]

    # jodi page memory te thake → hit
    if page in memory:
        hits += 1
        fault = "hit"

    else:   # jodi page memory te na thake → miss
        miss += 1
        fault = "miss"

        # jodi memory te jaiga thake
        if len(memory) < frames:
            memory.append(page)

        else:  # memory full → LRU replace korte hobe

            # memory er moddhe je page ta shobar age use hoyeche (least recently used)
            lru_page = memory[0]
            min_index = recent[lru_page] # eikhane memory er first value tah dhora hoyeche first use hoyeche so eita re replace korbo tai recent e er index kotot ber kora hoche 

            for p in memory:
                if recent[p] < min_index: 
                    min_index = recent[p]
                    lru_page = p

            # oi LRU page ta replace kora
            replace_index = memory.index(lru_page)
            memory[replace_index] = page

    # current page er last used index update
    recent[page] = i

    # protita step print
    print(f"Page: {page} -> Frames: {memory} -> {fault}")


# total calculation
total = len(pages)
hit_ratio = hits / total
miss_ratio = miss / total

print("\nTotal Pages:", total)
print("Total Hits:", hits)
print("Total Misses:", miss)
print("Hit Ratio:", round(hit_ratio, 2))
print("Miss Ratio:", round(miss_ratio, 2))