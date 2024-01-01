from math import sqrt
from ADT import make_city, get_name, get_lat, get_lon, tree, label, branches, is_leaf, print_tree

# Problem 4.1.1
def fst(p):
    return p(0)

def snd(p):
    return p(1)

def pair(x, y):
    """Return a function that represents a pair.
    
    >>> p = pair(1, 2)
    >>> fst(p)
    1
    >>> snd(p)
    2
    """
    def p(t):
        return [x,y][t]
    return p

def change_fst(p, v):
    """Change pair p's first element into v and return it.

    >>> p = pair(1, 2)
    >>> fst(p)
    1
    >>> snd(p)
    2
    >>> p = change_fst(p, 3)
    >>> fst(p)
    3
    >>> snd(p)
    2
    """
    def c_p(t):
        return [v,snd(p)][t]
    return c_p

def change_snd(p, v):
    """Change pair p's second element into v and return it.

    >>> p = pair(1, 2)
    >>> fst(p)
    1
    >>> snd(p)
    2
    >>> p = change_snd(p, 3)
    >>> fst(p)
    1
    >>> snd(p)
    3
    """
    def c_p_again(t):
        return [fst(p),v][t]
    return c_p_again

# Problem 4.1.2.1
def distance(city1, city2):
    """
    >>> city1 = make_city('city1', 0, 1)
    >>> city2 = make_city('city2', 0, 2)
    >>> distance(city1, city2)
    1.0
    >>> city3 = make_city('city3', 6.5, 12)
    >>> city4 = make_city('city4', 2.5, 15)
    >>> distance(city3, city4)
    5.0
    """
    "*** YOUR CODE HERE ***"
    d = get_lat(city1)-get_lat(city2)
    l = get_lon(city1)-get_lon(city2)
    return sqrt(d**2+l**2)

# Problem 4.1.2.2
def closer_city(lat, lon, city1, city2):
    """
    Returns the name of either city1 or city2, whichever is closest to
    coordinate (lat, lon).

    >>> berkeley = make_city('Berkeley', 37.87, 112.26)
    >>> stanford = make_city('Stanford', 34.05, 118.25)
    >>> closer_city(38.33, 121.44, berkeley, stanford)
    'Stanford'
    >>> bucharest = make_city('Bucharest', 44.43, 26.10)
    >>> vienna = make_city('Vienna', 48.20, 16.37)
    >>> closer_city(41.29, 174.78, bucharest, vienna)
    'Bucharest'
    """
    "*** YOUR CODE HERE ***"
    city3 = make_city('r',lat,lon)
    if distance(city1,city3)<distance(city2,city3):
        return get_name(city1)
    else:
        return get_name(city2)

# Problem 4.2.1
def my_map(fn, seq):
    """Applies fn onto each element in seq and returns a list.
    >>> my_map(lambda x: x*x, [1, 2, 3])
    [1, 4, 9]
    >>> my_map(lambda x: abs(x), [1, -1, 5, 3, 0])
    [1, 1, 5, 3, 0]
    >>> my_map(lambda x: print(x), ['sicp', 'autumn', '2023'])
    sicp
    autumn
    2023
    [None, None, None]
    """
    "*** YOUR CODE HERE ***"
    for i in range(0,len(seq)):
        seq[i]=fn(seq[i])
    return seq

# Problem 4.2.2
def my_filter(pred, seq):
    """Keeps elements in seq only if they satisfy pred.
    >>> my_filter(lambda x: x % 2 == 0, [1, 2, 3, 4])  # new list has only even-valued elements
    [2, 4]
    >>> my_filter(lambda x: (x + 5) % 3 == 0, [1, 2, 3, 4, 5])
    [1, 4]
    >>> my_filter(lambda x: print(x), [1, 2, 3, 4, 5])
    1
    2
    3
    4
    5
    []
    >>> my_filter(lambda x: max(5, x) == 5, [1, 2, 3, 4, 5, 6, 7])
    [1, 2, 3, 4, 5]
    """
    "*** YOUR CODE HERE ***"
    lis=[]
    for i in range(0,len(seq)):
        if pred(seq[i]):
            lis.append(seq[i])
    return lis



# Problem 4.2.3
def my_reduce(combiner, seq):
    """Combines elements in seq using combiner.
    seq will have at least one element.
    >>> my_reduce(lambda x, y: x + y, [1, 2, 3, 4])  # 1 + 2 + 3 + 4
    10
    >>> my_reduce(lambda x, y: x * y, [1, 2, 3, 4])  # 1 * 2 * 3 * 4
    24
    >>> my_reduce(lambda x, y: x * y, [4])
    4
    >>> my_reduce(lambda x, y: x + 2 * y, [1, 2, 3]) # (1 + 2 * 2) + 2 * 3
    11
    """
    "*** YOUR CODE HERE ***"
    cmb=seq[0]
    for i in range(1,len(seq)):
        cmb=combiner(cmb,seq[i])
    return cmb

# Problem 4.3.1
def preorder(t):
    """Return a list of the entries in this tree in the order that they
    would be visited by a preorder traversal (see problem description).

    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> preorder(numbers)
    [1, 2, 3, 4, 5, 6, 7]
    >>> preorder(tree(2, [tree(4, [tree(6)])]))
    [2, 4, 6]
    """
    "*** YOUR CODE HERE ***"
    #need improvement!!!
    if is_leaf(t):
        return [label(t)]
    else:
        result = [label(t)]
        for branch in branches(t):
            result.extend(preorder(branch))
        return result


# Problem 4.3.2
def nut_finder(t):
    """Returns True if t contains a node with the value 'nut' and
    False otherwise.

    >>> scrat = tree('nut')
    >>> nut_finder(scrat)
    True
    >>> sproul = tree('roots', [tree('branch1', [tree('leaf'), tree('nut')]), tree('branch2')])
    >>> nut_finder(sproul)
    True
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> nut_finder(numbers)
    False
    >>> t = tree(1, [tree('nut',[tree('not nut')])])
    >>> nut_finder(t)
    True
    """
    "*** YOUR CODE HERE ***"
    lis=preorder(t)
    for i in range(len(lis)):
        if lis[i]=='nut':
            return True
    return False

# Problem 4.3.3
def sprout_leaves(t, values):
    """Sprout new leaves containing the data in values at each leaf in
    the original tree t and return the resulting tree.

    >>> t1 = tree(1, [tree(2), tree(3)])
    >>> print_tree(t1)
    1
      2
      3
    >>> new1 = sprout_leaves(t1, [4, 5])
    >>> print_tree(new1)
    1
      2
        4
        5
      3
        4
        5

    >>> t2 = tree(1, [tree(2, [tree(3)])])
    >>> print_tree(t2)
    1
      2
        3
    >>> new2 = sprout_leaves(t2, [6, 1, 2])
    >>> print_tree(new2)
    1
      2
        3
          6
          1
          2
    """
    "*** YOUR CODE HERE ***"
    if is_leaf(t):
        return tree(label(t),[tree(n1) for n1 in values])
    else:
        return tree(label(t),[sprout_leaves(n2,values) for n2 in branches(t)])

    


def insert_items(lst, entry, elem):
    """
    >>> test_lst = [1, 5, 8, 5, 2, 3]
    >>> new_lst = insert_items(test_lst, 5, 7)
    >>> new_lst
    [1, 5, 7, 8, 5, 7, 2, 3]
    >>> large_lst = [1, 4, 8]
    >>> large_lst2 = insert_items(large_lst, 4, 4)
    >>> large_lst2
    [1, 4, 4, 8]
    >>> large_lst3 = insert_items(large_lst2, 4, 6)
    >>> large_lst3
    [1, 4, 6, 4, 6, 8]
    >>> large_lst3 is large_lst
    True
    """
    "*** YOUR CODE HERE ***"
    num = 0   
    while num<=(len(lst)-1):
        if lst[num]==entry:
            lst.insert(num+1,elem)
            if entry == elem:
                num+=1
        num+=1
    return lst
