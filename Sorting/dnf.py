# Leetcode 77 - Sort Colors, Dutch National Flag

def dutch_flag_sort(balls):
    # 3 Partition approach, lets set a pivot -> Green
    # Red goes to the left of green - low_boundary
    # Blue goes to the right of green - high_boundary
    # Define Boundaries
    low_boundary = 0
    high_boundary = len(balls) - 1
    i = 0
    while i <= high_boundary:
        if balls[i] == 'R': # Element less than pivot
            balls[i], balls[low_boundary] = balls[low_boundary], balls[i]
            low_boundary += 1
            i += 1
        elif balls[i] == 'B': # Element greater than pivot
            balls[i], balls[high_boundary] = balls[high_boundary], balls[i]
            high_boundary -= 1
        else:
            i += 1
    print(balls)