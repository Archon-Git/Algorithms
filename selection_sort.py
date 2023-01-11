def selection(unsorted, c):
    n = len(unsorted)
    for i in range(n):
        min_index = i
        for j in  range(i + 1, n):
            if(c == 1):
                if(unsorted[j] < unsorted[min_index]):
                    min_index = j
            elif (c == 2):
                if(unsorted[j] > unsorted[min_index]):
                    min_index = j    
            else:
                print("\nInvalid Choice.")            
        unsorted[i], unsorted[min_index] = unsorted[min_index], unsorted[i]
    return unsorted 

def main():
    arr = list(map(int, input("Enter the numbers of the array: \n").strip().split()))
    ch = int(input("Enter 1 for Ascending order and 2 for Descending order: \n"))
    print(selection(arr, ch))

if __name__ == "__main__":
    main()