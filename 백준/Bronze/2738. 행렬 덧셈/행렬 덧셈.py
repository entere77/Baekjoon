N,M=map(int, input().split())
matrix_a=[list(map(int, input().split())) for _ in range(N)]
matrix_b=[list(map(int, input().split())) for _ in range(N)]
sum_matrix=[[0 for _ in range(M)]for _ in range(N)]
for i in range(N):
    for j in range(M):
        sum_matrix[i][j]=matrix_a[i][j]+matrix_b[i][j]
        
for row in sum_matrix:
    print(*row)