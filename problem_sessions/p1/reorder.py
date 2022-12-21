def reorder(L):
    '''
    Input: L | linked list with head L.head and size L.size
    Output: None |
    This function should modify list L to reverse its last half.
    Your solution should NOT instantiate:
        - any additional linked list nodes
        - any other non-constant-sized data structures
    '''

    # get to nth node
    n = L.size // 2
    a = L.head
    
    for _ in range(n-1):
        a = a.next
    
    # reverse next pointers from n+1 -> 2n
    # keeping track of where u came from and where u're going to
    b = a.next
    x_p, x = a, b

    for _ in range(n):
        x_n = x.next
        x.next = x_p
        x_p, x = x, x_n
   
    # clean up the ends
    a.next = x_p
    b.next = x
    return 

