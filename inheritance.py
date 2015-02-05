class parent:
    var1 = "hi im variable 1"
    var2 = "hi im variable 2"
class child(parent):
    def __init__(slef):
        print parent.var1
        print parent.var2

cob = child()  
