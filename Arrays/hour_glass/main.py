def get_hourglass_sum(row_idx, col_idx, array):
    hourglass_sum = 0

    # sum of top row
    row = array[row_idx]
    hourglass_sum += row[col_idx]
    hourglass_sum += row[col_idx + 1]
    hourglass_sum += row[col_idx + 2]

    # sum of middle row
    row = array[row_idx + 1]
    hourglass_sum += row[col_idx + 1]
    
    # sum of bottom row
    row = array[row_idx + 2]
    hourglass_sum += row[col_idx]
    hourglass_sum += row[col_idx + 1]
    hourglass_sum += row[col_idx + 2]
    
    return hourglass_sum

def get_max_hourglass_sum(n, sub_array_size, array):
    largest_sum = -999999
    
    # iterate only till the index from where a subarray can be formed
    n = n - sub_array_size + 1
    for i in range(0, n):
        for j in range(0, n): # since the array is of n * n
            current_hourglass_sum = get_hourglass_sum(i, j, array)
            if current_hourglass_sum > largest_sum:
                largest_sum = current_hourglass_sum
    
    return largest_sum

if __name__ == "__main__":
    n = 6
    sub_array_size = 3
    array = []
    for _ in range(0, n):
        row = list(map(int, input().strip().split()))
        array.append(row)

    get_max_hourglass_sum(n, sub_array_size, array)