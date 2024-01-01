""" Homework 6: OOP and Inheritance"""

#####################
# Required Problems #
#####################

class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.add_funds(15)
    'Machine is out of stock. Here is your $15.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must add $10 more funds.'
    >>> v.add_funds(7)
    'Current balance: $7'
    >>> v.vend()
    'You must add $3 more funds.'
    >>> v.add_funds(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.add_funds(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.add_funds(15)
    'Machine is out of stock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.add_funds(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    "*** YOUR CODE HERE ***"
    def __init__(self,nam,pric):
        self.name=nam
        self.stock=0
        self.balance=0
        self.price=pric
    
    def restock(self,n):
        self.stock+=n
        return 'Current {0} stock: {1}'.format(self.name,self.stock)
    
    def add_funds(self,n):
        if(self.stock==0):
            return 'Machine is out of stock. Here is your ${0}.'.format(n)
        else:
            self.balance+=n
            return 'Current balance: ${0}'.format(self.balance)
        
    def vend(self):
        if(self.stock==0):
            return 'Machine is out of stock.'
        elif(self.balance<self.price):
            return 'You must add ${0} more funds.'.format(self.price-self.balance)
        elif(self.balance==self.price):
            self.balance=0
            self.stock-=1
            return 'Here is your {0}.'.format(self.name)
        else:
            temp=self.balance-self.price
            self.balance=0
            self.stock-=1
            return 'Here is your {0} and ${1} change.'.format(self.name,temp)

class PrintModule:
      def pp(self):
        pretty_print(self)

class Pet(PrintModule):
    """A pet.

    >>> kyubey = Pet('Kyubey', 'Incubator')
    >>> kyubey.talk()
    Kyubey
    >>> kyubey.eat('Grief Seed')
    Kyubey ate a Grief Seed!
    """
    def __init__(self, name, owner):
        self.is_alive = True    # It's alive!!!
        self.name = name
        self.owner = owner
    
    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")
    
    def talk(self):
        print(self.name)

    def to_str(self):
        "*** YOUR CODE HERE ***"
        return f"{Colors.OKCYAN}{'({0}, {1})'.format(self.name,self.owner)}{Colors.ENDC}"


class Cat(Pet,PrintModule):
    """A cat.

    >>> vanilla = Cat('Vanilla', 'Minazuki Kashou')
    >>> isinstance(vanilla, Pet) # check if vanilla is an instance of Pet.
    True
    >>> vanilla.talk()
    Vanilla says meow!
    >>> vanilla.eat('fish')
    Vanilla ate a fish!
    >>> vanilla.lose_life()
    >>> vanilla.lives
    8
    >>> vanilla.is_alive
    True
    >>> for i in range(8):
    ...     vanilla.lose_life()
    >>> vanilla.lives
    0
    >>> vanilla.is_alive
    False
    >>> vanilla.lose_life()
    Vanilla has no more lives to lose.
    """
    def __init__(self, name, owner, lives=9):
        "*** YOUR CODE HERE ***"
        super(Cat,self).__init__(name,owner)
        self.lives=lives
        self.is_alive=True

    def talk(self):
        """ Print out a cat's greeting.
        """
        "*** YOUR CODE HERE ***"
        print(self.name+" says meow!")

    def lose_life(self):
        """Decrements a cat's life by 1. When lives reaches zero, 'is_alive'
        becomes False. If this is called after lives has reached zero, print out
        that the cat has no more lives to lose.
        """
        "*** YOUR CODE HERE ***"
        if((self.lives-1)!=-1):
            self.lives-=1
            if(self.lives==0):
                self.is_alive=False
        else:
            print(self.name+" has no more lives to lose.")

    def to_str(self):
        "*** YOUR CODE HERE ***"
        return f"{Colors.OKCYAN}{'({0}, {1}, {2})'.format(self.name,self.owner,self.lives)}{Colors.ENDC}"


class NoisyCat(Cat,PrintModule): # Dose this line need to change?
    """A Cat that repeats things twice.

    >>> chocola = NoisyCat('Chocola', 'Minazuki Kashou')
    >>> isinstance(chocola, Cat) # check if chocola is an instance of Cat.
    True
    >>> chocola.talk()
    Chocola says meow!
    Chocola says meow!
    """
    def talk(self):
        """Talks twice as much as a regular cat.
        """
        "*** YOUR CODE HERE ***"
        super().talk()
        super().talk()

class Colors:
    HEADER     = '\033[95m'
    OKBLUE     = '\033[34m'
    OKCYAN     = '\033[35m'
    WARNING    = '\033[93m'
    FAIL       = '\033[91m'
    ENDC       = '\033[0m'
    BOLD       = '\033[1m'
    UNDERLINE  = '\033[4m'


def pretty_print(obj):
    """Pretty prints the object using the Colors class.
    >>> kyubey = Pet('Kyubey', 'Incubator')
    >>> pretty_print(kyubey)
    \033[34mPet\033[0m\033[35m(Kyubey, Incubator)\033[0m
    """
    "*** YOUR CODE HERE ***"
    n1=f"{Colors.OKBLUE}{obj.__class__.__name__}{Colors.ENDC}"
    n2=obj.to_str()
    print("{0}{1}".format(n1,n2))

    

        
          
        



##########################
# Just for fun Questions #
##########################

class Fib:
    """A Fibonacci number.

    >>> start = Fib()
    >>> start.value
    0
    >>> start.next().value
    1
    >>> start.next().next().value
    1
    >>> start.next().next().next().value
    2
    >>> start.next().next().next().next().value
    3
    >>> start.next().next().next().next().next().value
    5
    >>> start.next().next().next().next().next().next().value
    8
    >>> start.value # Ensure start isn't changed
    0
    """

    def __init__(self, value=0):
        self.value = value
        self.pre=None

    def next(self):
        "*** YOUR CODE HERE ***"
        if self.pre:
         new_value=self.value+self.pre.value
         next_Fib=Fib(new_value)
         next_Fib.pre=self
        elif self.pre is None:
         new_value=1
         next_Fib=Fib(new_value)
         next_Fib.pre=self
        else:
         new_value=self.value
         next_Fib=Fib(new_value)
         next_Fib.pre=self
        return next_Fib


