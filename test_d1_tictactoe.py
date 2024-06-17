from d1_tictactoe import move, evaluate

# Tests for the evaluate function

def test_evaluate_x():
# Tests if the function returns the right answer to x winning
    board = "--xxx----o--oo"
    res = evaluate(board)
    assert res == ("x", True)

def test_evaluate_draw():
# Tests if the function returns the right answer to a draw
    board = "xoxoxoxoxoxoxoxo"
    res = evaluate(board)
    assert res == ("!", True)

def test_evaluate_continue():
# Tests if the function correctly continues the game if there is an empty (-) space left in the board
    board= "--xxo----o--oo"
    res = evaluate(board)
    assert res == ("-", False)

# Tests for the move function

# Writing these tests, it occurs to me that I maybe should have written the move function differently: 
# it should be handle to deal with a position being already taken and show an error message (I would test that). 
# Since I have not written it that way, I cannot test it that way...

def test_x_mark():
# Tests if the function can handle a placed x mark
    board = "----x----o--oo"
    res = move(board, "x", 1)
    assert res == "-x--x----o--oo"

def test_o_mark():
# Tests if the function can handle a placed o mark
   board = "----x----o--oo"
   res = move(board, "o", 1)
   assert res == "-o--x----o--oo"

# Questions
# What is a module and how does it differ from a package?
    # A module is a collection of code that can be imported into code I am writing - like a plug in I can add to some software.
    # A package is a collection of modules - i.e. it is a module containing sub-modules. 

# What are side effects?
    # Side effect means that a module we have imported does something (e.g.printing, writing something into a file, asking for a user input).
    # This should be avoided, since the purpose of modules is to import functions so that we can use them to do something - not for
    # the module to do the thing for us. 

# What are Exceptions and what should we do with them if a third party code throws them?
    # An exception is an event that occures when we run our code that we did not expect to happen - in other words, 
    # they are not syntax errors (not errors with the code), but errors with the exectution of the code. 
    # They occure e.g. when there is a user input and the code expects a str but the user input is an int. 

    # The best way forward is to terminate the program and try to understand the problem (and potentially solve it). 
    # Only catch them if you anticipate some exception. 

# What are the keywords to create, throw and catch custom Exceptions?
    # create = raise
    # not sure what you mean by throwing a costum exception (I also could not find out through googling) 
    # catch = assert when testing, try/except when expecting an exception and already planing the code in a way that can handle it

# What are the benefits of testing?
    # 1. To test if the code does what it is supposed to do. T
        # Testing is especially necessary if the code is more complex, as testing cannot be done manually on such codes. 
    # 2. To set benchmarks for your code - the code is good enough, if it can pass the tests (anyting better is the cherry on top).
    # 3. To undertsand your code: it can help to think of test cases your code is supposed to be able to handle before you start coding. 
        # This can help you understand what kind of tasks your code should be able to handle and then code accordingly 
        # (see my comment on the move function above.)