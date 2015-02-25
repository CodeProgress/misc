
def isBalanced(aString):
    stack = []
    openings = {'(':')', '{':'}', '[':']'}
    closings = {')':'(', '}':'{', ']':'['}
    for i in aString:
        if i in openings: 
            stack.append(i)
        elif i in closings:
            if stack == []: 
                return False
            possibleMatch = stack.pop()
            if closings[i] != possibleMatch: 
                return False
    
    return stack == []
            
#True
test0 = "()"
test1 = "(this) is (((a))) {(())} test"
test2 = "(this) is (((a))) {(())} test{{(([[([{}])]]))}}"

#False
test3 = "(this) is (((a))) {(())} test{{(([[([{}])]]))}}("
test4 = "{"
test5 = "(((((((((((((((((((((((((((((((((((((((((((((((()"


def test_balanced_function(aFunction):
    assert aFunction(test0)
    assert aFunction(test1)
    assert aFunction(test2)
    assert not aFunction(test3)
    assert not aFunction(test4)
    assert not aFunction(test5)
    
test_balanced_function(isBalanced)

