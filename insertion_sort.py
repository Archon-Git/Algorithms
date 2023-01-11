def insertion(unsorted, c):
    for i in range(1, len(unsorted)):
        j = i
        
        if(c == 1):
            while unsorted[j] < unsorted[j-1] and j > 0 :
                unsorted[j], unsorted[j-1] = unsorted[j-1], unsorted[j]
                j -= 1
        elif(c == 2):
            while unsorted[j] > unsorted[j-1] and j > 0 :
                unsorted[j], unsorted[j-1] = unsorted[j-1], unsorted[j]
                j -= 1
        else:
            print("Invalid Choice.")
    return unsorted


def main():
    arr = list(map(int, input("Enter the numbers of the array: ").strip().split()))
    ch = int(input("Enter 1 if you want Ascending order, 2 if you want Descending order: "))
    print(insertion(arr, ch))

if __name__ == "__main__":
    main()