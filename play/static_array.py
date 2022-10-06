class StaticArray:
    def __init__(self, n):
        # allocate a new static array of size n initialized to 0 in Θ(n) time
        self.data = [None] * n
    def get_at (self, i):
        # return the word stored at array index i in Θ(1) time
        if (i < 0 or i > len(self.data)): raise IndexError
        return self.data[i]

    def set_at (self, i, x): 
        # write the word x to array index i in Θ(1) time
        if (i < 0 or i > len(self.data)): raise IndexError
        self.data[i] = x
