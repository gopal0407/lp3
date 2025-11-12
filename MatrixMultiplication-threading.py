import threading
import time

# -------- Normal Matrix Multiplication --------
def normal_multiply(A, B):
    n = len(A)
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j]
    return result

# -------- Multithreaded (One Thread per Row) --------
def row_multiply(A, B, result, row):
    n = len(A)
    for j in range(n):
        for k in range(n):
            result[row][j] += A[row][k] * B[k][j]

def threaded_multiply(A, B):
    n = len(A)
    result = [[0] * n for _ in range(n)]
    threads = []

    for i in range(n):
        t = threading.Thread(target=row_multiply, args=(A, B, result, i))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    return result

# -------- Main Function --------
if __name__ == "__main__":
    n = int(input("Enter size of square matrix (n x n): "))

    print("\nEnter elements of Matrix A:")
    A = []
    for i in range(n):
        row = list(map(int, input(f"Row {i+1}: ").split()))
        A.append(row)

    print("\nEnter elements of Matrix B:")
    B = []
    for i in range(n):
        row = list(map(int, input(f"Row {i+1}: ").split()))
        B.append(row)

    # Normal multiplication
    start = time.time()
    result_normal = normal_multiply(A, B)
    end = time.time()
    print("\nNormal Multiplication Result:")
    for row in result_normal:
        print(row)
    print("Time taken (normal):", round(end - start, 5), "seconds\n")

    # Multithreaded multiplication
    start = time.time()
    result_threaded = threaded_multiply(A, B)
    end = time.time()
    print("Multithreaded Multiplication Result:")
    for row in result_threaded:
        print(row)
    print("Time taken (multithreaded):", round(end - start, 5), "seconds")
