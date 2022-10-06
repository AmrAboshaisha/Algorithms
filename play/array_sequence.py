class ArraySeq:
    def __init__(self):
        self.A = []
        self.size = 0
    
    def __len__(self): return self.size
    def __iter__(self): yield from self.A

    # given an iterable X, build sequence from items in X return the number of stored items
    def build(self, X):
        self.A = [a for a in X]
        self.size = len(self.A)
    
    def _copy_forward(self, i, n, A, j):
        for k in range(n):
            A[j+k] = self.A[i+k]

    def get_at(self, i):
        # return the ith item
        if (i < 0 or i > self.size): raise IndexError
        else: return self.A[i] 
    

    def set_at(self, i, x):
        # replace the ith item with x
        if (i < 0 or i > self.size): raise IndexError
        else: self.A[i] = x

    
    def insert_at(self, i, x):
        # add x as the ith item
        n = len(self)
        ## create a new array to populate the extra number
        A = [None] * (n + 1)
        ## copy whatever is before i
        self._copy_forward(0,i,A,0)
        ## insert the new number
        A[i] = x
        ## copy whatever is after i
        self._copy_forward(i,n-i,A,i+1)
        self.build(A)

    def delete_at(self, i):
        # remove and return the ith item 
        n = len(self)
        A = [None] * (n-1)
        self._copy_forward(0,i,A,0)
        self._copy_forward(i+1,n-i-1,A,i)
        self.build(A)

    def insert_first(self, x):
        # add x as the first item
        self.insert_at(0,x)
    def delete_first(self):
        # remove and return the first item 
        self.delete_at(0)
    def insert_last(self, x):
        # add x as the last item
        self.insert_at(len(self), x)
    def delete_last(self):
        # remove and return the last item
        self.delete_at(len(self)-1)
