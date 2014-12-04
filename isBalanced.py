
def isBalanced(aString):
    stack = []
    openings = {'(':')', '{':'}', '[':']'}
    closings = {')':'(', '}':'{', ']':'['}
    for i in aString:
        if i in openings: 
            stack.append(i)
        elif i in closings:
            if not stack: 
                return False
            possibleMatch = stack.pop()
            if closings[i] != possibleMatch: 
                return False
    
    return not stack
    

#True
test0 = "()"
test1 = "(this) is (((a))) {(())} test"
test2 = "(this) is (((a))) {(())} test{{(([[([{}])]]))}}"

#False
test3 = "(this) is (((a))) {(())} test{{(([[([{}])]]))}}("
test4 = "{"
test5 = "(((((((((((((((((((((((((((((((((((((((((((((((()"

assert isBalanced(test0)
assert isBalanced(test1)
assert isBalanced(test2)
assert not isBalanced(test3)
assert not isBalanced(test4)
assert not isBalanced(test5)
