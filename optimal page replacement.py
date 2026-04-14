pages = list(map(int, input("Enter page sequence (space separated): ").split()))
frames = int(input("Enter number of frames: "))

memory = []

miss = 0
hits = 0
fault = ""

for i in range(len(pages)):
    page = pages[i]

    # jodi page list er value memory teh peye jay tahole hit
    if page in memory:
        hits += 1
        fault = "hit"

    else:   # jodi page list er value memory teh na pay tahole miss
        miss += 1
        fault = "miss"

        # jodi memory teh jaiga thake tokhon page list theke page store korbe
        if len(memory) < frames:
            memory.append(page)

        else:  # jodi memory teh jaiga na thake tokhon replace korte hobe

            # page list er current index er porer gula niye future list toiri
            future = pages[i+1:]

            # memory teh jei index er value replace korbo
            index_to_replace = -1

            # shobar last e je value use hobe tar position track korar jonno
            farthest = -1

            for j in range(len(memory)):

                # jodi memory er kono value future e ar use na hoy
                # tahole oita direct replace kora hobe
                if memory[j] not in future:
                    index_to_replace = j
                    break

                else:
                    # memory er value future list er kothay ache seta ber kora
                    pos = future.index(memory[j])

                    # jei value shobar pore use hobe seta select kora
                    if pos > farthest:
                        farthest = pos
                        index_to_replace = j

            # selected index e new page bosano
            memory[index_to_replace] = page

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

#input: 7 0 1 2 0 3 0 4 2 3 0 3 2 1 2 0 1 7 0 1
#frame: 3