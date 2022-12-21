def selection_sort(L):
    ## For each index / location in list L, see if the element in it is less than all others. If less than others, move to the beginning of the unsorted part of the list.

    # look at each location in list. This is the smallest item so far
    if len(L) > 1:
        for i in range(len(L)-1):
            smallest_so_far_idx = i
            # look at the loctions in front of your current location.
            for j in range(i+1, len(L)):
                    # if any of them is less than yours, update the smallest so far to become this new value
                    if L[j] < L[smallest_so_far_idx]:
                        smallest_so_far_idx = j
                    # when u reach the end, swap the value at your current location with this smallest value
            tmp = L[i]
            L[i] = L[smallest_so_far_idx]
            L[smallest_so_far_idx] = tmp


def insertion_sort(L):
    for i in range(1, len(L)):
        current = i
        previous = i-1
        while previous >= 0:
            if L[current] < L[previous]:
                L[current], L[previous] = L[previous], L[current]
                current -=1
                previous -=1
            else:
                break
