arr = [13,1,3,7,4,14,8,6,5,9,10,12,2]
import time

def bubble():
    start_time =time.perf_counter()
    gjort_byten = True
    while gjort_byten:
        gjort_byten = False
        for i in range(len(arr)-1):
            if (arr[i]>arr[i+1]):
                temp = arr[i]
                arr[i]=arr[i+1]
                arr[i+1]=temp
                gjort_byten = True
            else:
                print(f"{arr}\n")
                
        
    print(f"Här är din sorterade lista! {arr}")
    end_time = time.perf_counter()
    print(f"Antalet sekunder som krävdes för loopen: {(end_time - start_time)}s")

bubble()