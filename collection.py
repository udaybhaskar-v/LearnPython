# touple and dictinary in function

def myfunc(first, last, *touple1, **dictionary1):
    print first, last
    print touple1
    print dictionary1
myfunc('uday', 'bhaskar', 23,25,26,26,27,29,33, anand='anand',bhaskar='uday',reddy='ram')
