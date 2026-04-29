def mergesort():
    number  = 25000000
    max_val = 25000000
    # number=int(input("hur många tal"))
    # max_val=int(input("Hur högt ska talen gå"))
    import random
    arr = []
    import time
    for i in range(number):
        arr.append(random.randint(0,max_val))
        

    def merge(arr, counter):
  
        if len(arr) > 1:
            mid = len(arr)//2
            L = arr[:mid]
            R = arr[mid:]

            counter = merge(L, counter)
            counter = merge(R, counter)

            i = j = k = 0

            while i < len(L) and j < len(R):

                counter += 1
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1

            while i < len(L):

                arr[k] = L[i]
                i += 1
                k += 1

            while j < len(R):

                arr[k] = R[j]
                j += 1
                k += 1

        return counter

    start_time = time.perf_counter()
    swishswishbish = merge(arr, 0)
    end_time = time.perf_counter()

    print(f"Här är din sorterade lista! {arr}")
    slut_tid = end_time - start_time
    print(f"Antalet sekunder som krävdes för loopen: {slut_tid}s")
    print(f"du har kört loopen {swishswishbish} gånger!")
    medelbyte = swishswishbish / slut_tid if slut_tid > 0 else float('inf')
    print(f"medeltiden per byte var {medelbyte} ggr/sek")

    return start_time, end_time
    
    
endtime=10000
starttime= 0
mergesortrun=0
tottid = 0
while endtime-starttime > 2:
    mergesortrun+=1
    starttime, endtime =mergesort()
    tottid += (endtime-starttime)
print(f"den körde bubbasort {mergesortrun} gånger")
print(f"den körde totalt {tottid} sekunder")

    