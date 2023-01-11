def bubbleSort(arr, ch):
    n = len(arr)
    
    for i in range(n):
        for j in range(0, n-i-1):
            if ch == 1 :
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
            elif ch == 2 :
                if arr[j] < arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
            else:
                print("Invalid choice")
    
    return arr

def main():
    
    arr = list(map(int, input("\n Enter the numbers: ").strip().split()))
    ch = int(input("Enter 1 for Ascending order, 2 for Descending order: "))
    print(bubbleSort(arr, ch))

if __name__ == "__main__":
    main()