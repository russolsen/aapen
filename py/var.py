
class Var:
    def __init__(self, name, ns, root):
        self.name=name
        self.ns=ns
        self.root=root

    def value(self):
        return self.root

    def __call__(self, *args):
        return self.root(*args)

     def invoke(self, *args):
        return self.root(*args)
  

def isdefined(ns, name):
    return ns.__dict__.__contains__(name)

def intern(ns, name, value):
    if not isdefined(ns, name):
        v = Var(name, ns, value)
        ns.__dict__[name] = v
        return v

    x = ns.__getattr__(name)
    if isinstance(x, Var):
        x.root = value
        return x
    else:
        v = Var(name, ns, value)
        ns.__dict__[name] = v
        return v
