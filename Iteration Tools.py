# advanced iteration functions in the itertools package
# Nishank Kuppa

import itertools

def testFunction(x):
    return x < 40


def main():
    # TODO: cycle iterator can be used to cycle over a collection
    seq1 = ["Joe", "John", "Mike"]
    cycle1 = itertools.cycle(seq1)
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1))


    # TODO: use count to create a simple counter
    mycounter = itertools.count(100,10)
    print(next(mycounter))
    print(next(mycounter))
    print(next(mycounter))
    print(next(mycounter))

    # TODO: accumulate creates an iterator that accumulates values
    vals = [10,20,30,40,50,40,30,1000]
    accumulator = itertools.accumulate(vals)   #running addition
    print(list(accumulator))

    accumulator = itertools.accumulate(vals, max)  # running addition
    print(list(accumulator))
            
    # TODO: use chain to connect sequences together
    chain1 = itertools.chain("ABCD", "12345")
    print(list(chain1))
    
    # TODO: dropwhile and takewhile will return values until
    # a certain condition is met that stops them
    print(list(itertools.dropwhile(testFunction, vals))) # drop vals from sequence while testfunc = true
    print(list(itertools.takewhile(testFunction, vals))) # return vals from sequence while testfunc = true
    
if __name__ == "__main__":
    main()
    