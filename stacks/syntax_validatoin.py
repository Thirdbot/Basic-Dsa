
sample = "[[{}{}][({{{{{{}}}}}})][]]"

elements = {"[": "]", "{": "}", "(": ")"}

def is_valid(s):
    stack = []
    for i in s:
        #front
        if i in elements:
            stack.append(i)
        #back
        if i in elements.values():
            #convert to key
            key = {str(v): str(k) for k, v in elements.items()}[i]
            #check if stack is not empty
            if len(stack) != 0:
                #check if last element is the same as key
                if stack[-1] == key:
                    #pop the last element
                    stack.pop(stack.index(key))
                else:
                    #it not have the same key in stack before
                    print("Invalid")
            # stack.pop(index-1)
            
    #if already checked all elements
    if len(stack) == 0:
        print("Valid")

is_valid(sample)



        