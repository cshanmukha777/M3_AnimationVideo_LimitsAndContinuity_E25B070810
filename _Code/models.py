"""Rules for the graphed branches and their endpoint markers."""


def line_plus_two(x):
    return x+2


def square_plus_one(x):
    return x*x+1


def identity(x):
    return x


RULES = {
    "f": (line_plus_two,line_plus_two,4),
    "g": (square_plus_one,square_plus_one,2.35),
    "h": (line_plus_two,identity,4),
}
ENDPOINTS = {"f": ((4,True),(1,False)), "g": ((5,False),),
             "h": ((4,True),(2,False))}
