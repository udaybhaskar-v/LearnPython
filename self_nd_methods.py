class myclass:
    def foo(self,name):
        self.name = name	
    def foo2(self):
        return self.name
    def foo3(self):
        print "Hello %s" % self.name

class anthrclass:
    first = myclass()
    first.foo('uday')
    print  first.foo2()
    first.foo3()
    
    second = myclass()
    second.foo('bhaskar')
    print  second.foo2()
    second.foo3()
