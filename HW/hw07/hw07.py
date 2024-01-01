""" Homework 07: Special Method, Linked Lists and Mutable Trees"""

#####################
# Required Problems #
#####################

class Polynomial:
    """Polynomial.

    >>> a = Polynomial([0, 1, 2, 3, 4, 5, 0])
    >>> a
    Polynomial([0, 1, 2, 3, 4, 5])
    >>> print(a)
    0 + 1*x^1 + 2*x^2 + 3*x^3 + 4*x^4 + 5*x^5
    >>> b = Polynomial([-1, 0, -2, 1, -3])
    >>> print(b)
    -1 + 0*x^1 + -2*x^2 + 1*x^3 + -3*x^4
    >>> print(a + b)
    -1 + 1*x^1 + 0*x^2 + 4*x^3 + 1*x^4 + 5*x^5
    >>> print(a * b)
    0 + -1*x^1 + -2*x^2 + -5*x^3 + -7*x^4 + -12*x^5 + -11*x^6 + -15*x^7 + -7*x^8 + -15*x^9
    >>> print(a)
    0 + 1*x^1 + 2*x^2 + 3*x^3 + 4*x^4 + 5*x^5
    >>> print(b) # a and b should not be changed
    -1 + 0*x^1 + -2*x^2 + 1*x^3 + -3*x^4
    >>> zero = Polynomial([0])
    >>> zero
    Polynomial([0])
    >>> print(zero)
    0
    """
    "*** YOUR CODE HERE ***"
    def __init__(self,list):
        while list[-1]==0 and len(list)>1:
            list.pop(-1)
        self.list=list
        self.len=len(self.list)
    def __repr__(self):
        return f'Polynomial({self.list})'
    def __str__(self):
        temp=f'{self.list[0]}'
        for i in range(1,len(self.list)):
            temp+=f' + {self.list[i]}*x^{i}'
        return temp
    def __add__(self,other):
        if self.len==other.len:
           add_result=[]
           for i in range(self.len):
               add_result.append(self.list[i]+other.list[i])
           return Polynomial(add_result)
        elif self.len>other.len:
            add_result=[]
            for i in range(other.len):
                add_result.append(other.list[i]+self.list[i])
            for j in range(other.len,self.len):
                add_result.append(self.list[j])
            return Polynomial(add_result)
        else:
            add_result=[]
            for i in range(self.len):
                add_result.append(other.list[i]+self.list[i])
            for j in range(self.len,other.len):
                add_result.append(other.list[j])
            return Polynomial(add_result)
    def __mul__(self,other):
        max_index=self.len+other.len
        mul_result=[]
        for i in range(0,(max_index+1)):
            temp=0
            for j in range(min(i+1,self.len)):
                if other.len>(i-j):
                    temp+=(self.list[j]*other.list[i-j])
            mul_result.append(temp)
        return Polynomial(mul_result)
        


def remove_duplicates(lnk):
    """ Remove all duplicates in a sorted linked list.

    >>> lnk = Link(1, Link(1, Link(1, Link(1, Link(5)))))
    >>> Link.__init__, hold = lambda *args: print("Do not steal chicken!"), Link.__init__
    >>> try:
    ...     remove_duplicates(lnk)
    ... finally:
    ...     Link.__init__ = hold
    >>> lnk
    Link(1, Link(5))
    """
    "*** YOUR CODE HERE ***"
    if lnk is Link.empty:
        return
    if lnk.rest is not Link.empty:
        if lnk.first==lnk.rest.first:
            lnk.rest=lnk.rest.rest
            remove_duplicates(lnk)
        else:
            remove_duplicates(lnk.rest)
            
            

def reverse(lnk):
    """ Reverse a linked list.

    >>> a = Link(1, Link(2, Link(3)))
    >>> # Disallow the use of making new Links before calling reverse
    >>> Link.__init__, hold = lambda *args: print("Do not steal chicken!"), Link.__init__
    >>> try:
    ...     r = reverse(a)
    ... finally:
    ...     Link.__init__ = hold
    >>> print(r)
    <3 2 1>
    >>> a.first # Make sure you do not change first
    1
    """
    "*** YOUR CODE HERE ***"
    curr=lnk
    prev=Link.empty
    while curr is not Link.empty:
        next=curr.rest
        curr.rest=prev
        prev=curr
        curr=next
    lnk=prev
    return lnk

class Tree:
    """
    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """

    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str

        return print_tree(self).rstrip()
    
    def __eq__(self,other): # Does this line need to be changed?
        """Returns whether two trees are equivalent.

        >>> t1 = Tree(1, [Tree(2, [Tree(3), Tree(4)]), Tree(5, [Tree(6)]), Tree(7)])
        >>> t1 == t1
        True
        >>> t2 = Tree(1, [Tree(2, [Tree(3), Tree(4)]), Tree(5, [Tree(6)]), Tree(7)])
        >>> t1 == t2
        True
        >>> t3 = Tree(0, [Tree(2, [Tree(3), Tree(4)]), Tree(5, [Tree(6)]), Tree(7)])
        >>> t4 = Tree(1, [Tree(5, [Tree(6)]), Tree(2, [Tree(3), Tree(4)]), Tree(7)])
        >>> t5 = Tree(1, [Tree(2, [Tree(3), Tree(4)]), Tree(5, [Tree(6)])])
        >>> t1 == t3 or t1 == t4 or t1 == t5
        False
        """
        "*** YOUR CODE HERE ***"
        if self.label != other.label:
            return False
        else:
            if (self.is_leaf() and not other.is_leaf()) or (other.is_leaf() and not self.is_leaf()):
               return False
            if (not self.is_leaf()and not other.is_leaf()):
               if len(self.branches)!=len(other.branches):
                   return False
               for i in range(len(self.branches)):
                   if self.branches[i]!=other.branches[i]:
                       return False                   
        return True



def generate_paths(t, value):
    """Yields all possible paths from the root of t to a node with the label value
    as a list.

    >>> t1 = Tree(1, [Tree(2, [Tree(3), Tree(4, [Tree(6)]), Tree(5)]), Tree(5)])
    >>> print(t1)
    1
      2
        3
        4
          6
        5
      5
    >>> next(generate_paths(t1, 6))
    [1, 2, 4, 6]
    >>> path_to_5 = generate_paths(t1, 5)
    >>> sorted(list(path_to_5))
    [[1, 2, 5], [1, 5]]

    >>> t2 = Tree(0, [Tree(2, [t1])])
    >>> print(t2)
    0
      2
        1
          2
            3
            4
              6
            5
          5
    >>> path_to_2 = generate_paths(t2, 2)
    >>> sorted(list(path_to_2))
    [[0, 2], [0, 2, 1, 2]]
    """
    "*** YOUR CODE HERE ***"
    list=[t.label]
    if t.label==value:
        yield list
        if not t.is_leaf():
          for b in t.branches:
            for ite in generate_paths(b,value):
                yield list+ite
    else:
        for b in t.branches:
            for ite in generate_paths(b,value):
                yield list+ite

def count_coins(total, denominations):
    """
    Given a positive integer `total`, and a list of denominations,
    a group of coins make change for `total` if the sum of them is `total` 
    and each coin is an element in `denominations`.
    The function `count_coins` returns the number of such groups. 
    """
    if total == 0:
        return 1
    if total < 0:
        return 0
    if len(denominations) == 0:
        return 0
    without_current = count_coins(total, denominations[1:])
    with_current = count_coins(total - denominations[0], denominations)
    return without_current + with_current


def count_coins_tree(total, denominations):
    """
    >>> count_coins_tree(1, []) # Return None since there is no way to make change with empty denominations
    >>> t = count_coins_tree(3, [1, 2]) 
    >>> print(t) # 2 ways to make change for 3 cents
    3, [1, 2]
      2, [1, 2]
        2, [2]
          1
        1, [1, 2]
          1
    >>> # 6 ways to make change for 15 cents
    >>> t = count_coins_tree(15, [1, 5, 10, 25]) 
    >>> print(t)
    15, [1, 5, 10, 25]
      15, [5, 10, 25]
        10, [5, 10, 25]
          10, [10, 25]
            1
          5, [5, 10, 25]
            1
      14, [1, 5, 10, 25]
        13, [1, 5, 10, 25]
          12, [1, 5, 10, 25]
            11, [1, 5, 10, 25]
              10, [1, 5, 10, 25]
                10, [5, 10, 25]
                  10, [10, 25]
                    1
                  5, [5, 10, 25]
                    1
                9, [1, 5, 10, 25]
                  8, [1, 5, 10, 25]
                    7, [1, 5, 10, 25]
                      6, [1, 5, 10, 25]
                        5, [1, 5, 10, 25]
                          5, [5, 10, 25]
                            1
                          4, [1, 5, 10, 25]
                            3, [1, 5, 10, 25]
                              2, [1, 5, 10, 25]
                                1, [1, 5, 10, 25]
                                  1
    """
    "*** YOUR CODE HERE ***"
    if not denominations or denominations==[]:
      return None
    
    if total<0:
      return None
    if total==0:
      return Tree("1")
    

    left = count_coins_tree(total,denominations[1:])
    right = count_coins_tree(total-denominations[0],denominations)
    if left is not None and right is not None:
          return Tree(f'{total}, {denominations}',[left,right])
    elif left is not None:
          return Tree(f'{total}, {denominations}',[left])
    elif right is not None:
          return Tree(f'{total}, {denominations}',[right])
    else:
          return None
    
def is_bst(t):
    """Returns True if the Tree t has the structure of a valid BST.

    >>> t1 = Tree(6, [Tree(2, [Tree(1), Tree(4)]), Tree(7, [Tree(7), Tree(8)])])
    >>> is_bst(t1)
    True
    >>> t2 = Tree(8, [Tree(2, [Tree(9), Tree(1)]), Tree(3, [Tree(6)]), Tree(5)])
    >>> is_bst(t2)
    False
    >>> t3 = Tree(6, [Tree(2, [Tree(4), Tree(1)]), Tree(7, [Tree(7), Tree(8)])])
    >>> is_bst(t3)
    False
    >>> t4 = Tree(1, [Tree(2, [Tree(3, [Tree(4)])])])
    >>> is_bst(t4)
    True
    >>> t5 = Tree(1, [Tree(0, [Tree(-1, [Tree(-2)])])])
    >>> is_bst(t5)
    True
    >>> t6 = Tree(1, [Tree(4, [Tree(2, [Tree(3)])])])
    >>> is_bst(t6)
    True
    >>> t7 = Tree(2, [Tree(1, [Tree(5)]), Tree(4)])
    >>> is_bst(t7)
    False
    >>> t8= Tree(10,[Tree(5,[Tree(1),Tree(9)]), Tree(11,[Tree(9),Tree(12)])])
    >>> is_bst(t8)
    False
    """
    "*** YOUR CODE HERE ***"
    #this is not an perfect version,however,I've tried my best
    def bst_min(t):
        if t.is_leaf():
            return t.label
        else:
            return min([t.label] + [bst_min(b) for b in t.branches])

    def bst_max(t):
        if t.is_leaf():
            return t.label
        else:
            return max([t.label] + [bst_max(b) for b in t.branches])
        
    if not t.is_leaf():
        if len(t.branches)==1:
            if t.branches[0].label<=t.label:
                if t.label>=bst_max(t.branches[0]):
                    return is_bst(t.branches[0])
                else:
                    return False
            else:
                if t.label<bst_min(t.branches[0]):
                    return is_bst(t.branches[0])
                else:
                    return False
        
        if (len(t.branches)==2 and t.label>=bst_min(t.branches[1])) or t.label<bst_max(t.branches[0]):
            return False
        else:
            return all(is_bst(b) for b in t.branches)
    else:
        return True

##########################
# Just for fun Questions #
##########################

def has_cycle(lnk):
    """ Returns whether lnk has cycle.

    >>> lnk = Link(1, Link(2, Link(3)))
    >>> has_cycle(lnk)
    False
    >>> lnk.rest.rest.rest = lnk
    >>> has_cycle(lnk)
    True
    >>> lnk.rest.rest.rest = lnk.rest
    >>> has_cycle(lnk)
    True
    """
    "*** YOUR CODE HERE ***"


def balance_tree(t):
    """Balance a tree.

    >>> t1 = Tree(1, [Tree(2, [Tree(2), Tree(3), Tree(3)]), Tree(2, [Tree(4), Tree(4)])])
    >>> balance_tree(t1)
    >>> t1
    Tree(1, [Tree(2, [Tree(3), Tree(3), Tree(3)]), Tree(3, [Tree(4), Tree(4)])])
    """
    "*** YOUR CODE HERE ***"


#####################
#        ADT        #
#####################

class Link:
    """A linked list.

    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.first = 5
    >>> s.rest.first = 6
    >>> s.rest.rest = Link.empty
    >>> s                                    # Displays the contents of repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # Prints str(s)
    <5 7 <8 9>>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'
