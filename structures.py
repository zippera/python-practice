# study some high-level data structures in python
# ref: http://blog.jobbole.com/65218/

import collections as cl
import array
import heapq
import bisect
import weakref
import pprint


### collections

# Counter
# count the number of times an element occurs
def test_counter():
    li = ["Dog", "Cat", "Mouse", 42, "Dog", 42, "Cat", "Dog"]
    a = cl.Counter(li)
    print a
    print a.most_common(2)


# Deque
def test_deque():
    q = cl.deque(range(5))
    print q
    q.append(13)
    q.appendleft(22)
    print q
    print q.pop()
    print q.popleft()
    print q
    q.rotate(2)
    print q

# Defaultdict
# Same with dict, except when a key not exists
def test_defaultdict():
    s = "the quick brown fox jumps over the lazy dog"
    words = s.split()
    l = cl.defaultdict(list)
    for k,v in enumerate(words):
        l[v].append(k)
    print l

    d = {}
    for k,v in enumerate(words):
        d.setdefault(k,[]).append(v)
    print d

    # same with counter
    li = ["Dog", "Cat", "Mouse", 42, "Dog", 42, "Cat", "Dog"]
    dd = cl.defaultdict(int)
    for k in li:
        dd[k] += 1
    print dd


### Array: small than list, element with one type

# i is type code, stands for signed int
def test_array():
    a = array.array('i',range(5))
    print a
    b = array.array(a.typecode,[x*2 for x in a])
    print b
    for i,x in enumerate(a):
        a[i] = x*2
    print a

### heapq

def test_heapq():
    heap = []
    for v in range(5):
        heapq.heappush(heap,v)
    print heapq.heappop(heap)
    print heapq.nlargest(3,heap)

### bisect
def test_bisect():
    a = [1,2,6,89]
    bisect.insort_right(a,4)
    print a
    print bisect.bisect(a,3)

### weakref
# like = , strong ref. except destroyed only when none ref is left
# do not really understand yet!
def test_weakref():
    a = 2
    b = a
    del b
    print a
    
    class Foo():
        a = 1
    f = Foo()
    d = weakref.ref(f)
    del f
    print d

### pprint
# beautiful print
def test_pprint():
    matrix = [ [1,2,3], [4,5,6], [7,8,9] ]
    a = pprint.PrettyPrinter(width = 20)
    a.pprint(matrix)

if __name__ == '__main__':
#    test_counter()
#    test_deque()
#    test_defaultdict()
#    test_array()
#    test_heapq()
#    test_bisect()
#    test_weakref()
    test_pprint()

