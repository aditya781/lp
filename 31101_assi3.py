
def printArray(A,n):
    for i in range(n):
        print("%d" % A[i], end=" ")

def selectionSort(A,n):
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if A[min_idx] > A[j]:
                min_idx = j
        A[i], A[min_idx] = A[min_idx], A[i]


A = []
n=1

#menu driven code
while(n):
    print("\n-----MENU-----\n 1. Exit\n 2. Insert Array\n 3. Sort\n 4. Display\n")
    n=int(input("Choose the number : "))
    if(n==1):
        n=0
        print("Programme ended!")
        break
    elif(n==2):
        size=int(input("Insert size of array : "))
        for i in range(size):
            ele=int(input("insert "+str(i+1)+"st number : "))
            A.append(ele)
    elif(n==3):
        selectionSort(A,len(A))
        print("Sorted the array successfully.")
    elif(n==4):
        printArray(A, len(A))
    else:
        print("Please select correct number")

