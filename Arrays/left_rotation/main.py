def get_left_rotated_array(times, array):
    popped_items = []
    for i in range(0, times):
        popped_items.append(array[i])
    
    return array[i + 1:] + popped_items


if __name__ == "__main__":
    n, d = tuple(map(int, input().strip().split()))
    array = input().strip().split()
    print(' '.join(get_left_rotated_array(d, array)))