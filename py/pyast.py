import ast
import astpp

def dump(tree):
    return astpp.dump(tree)

def pdump(tree):
    """Print the ast tree."""
    print(dump(tree))

def wrap_args(args):
    """Wrap the strings passed in in ast arg objects."""
    return list(map(lambda q: ast.arg(arg=q, annotation=None), args))

def arguments(args):
    """Take an array of strings and turn them into an arguments instance."""
    a =ast.arguments(
          args=wrap_args(args),
          vararg=None, kwonlyargs=[],
          kw_defaults=[], kwarg=None, defaults=[])
    return a

def n(x):
    return ast.Num(x)

def func(name, args, body):
    """Make a function with the given name, positional args and body. Body should be list of trees."""
    wrapped_args = arguments(args)
    f=ast.FunctionDef(name=name, args=wrapped_args, body=body, decorator_list=[], returns=None)
    return f

def call(fname, args):
    """Call a function with the given name with the  args. Args should be list of trees."""
    fcall = ast.Call(func=rval(fname), args=args, keywords=[])
    return fcall

def expr(x):
    return ast.Expr(value=x)

def println(t):
    """Emit code to print the value of evaluating tree t"""
    return call('print', [t])

def mod(mname, body):
    """Make a module with the given name. Body should be list of trees."""
    return ast.Module(name=mname, body=body)

def add(left, right):
    """Return an ast tree that adds the two arguments together."""
    return ast.BinOp(op=ast.Add(), left=left, right=right)

def ifelse(expr, iftrue, iffalse=None):
    return ast.If(test=expr, body=iftrue, orelse=iffalse)

def lval(s):
    """Make an ast lval for a var"""
    return ast.Name(s, ast.Store())

def rval(s):
    """Make an ast lval for a var"""
    return ast.Name(s, ast.Load())

#Expr(value=BoolOp(op=And(), values=[Compare(left=Name(id='x', ctx=Load()), ops=[NotEq()], comparators=[NameConstant(value=None)]), Compare(left=Name(id='x', ctx=Load()), ops=[NotEq()], comparators=[NameConstant(value=False)])]))])

def truthy(t):
    vals = [ast.NameConstant(value=True), ast.NameConstant(value=None)]
    compare = ast.Compare(left=t, comparators=vals, ops=[ast.In()])
    expr = ast.Expr(value=compare)
    return expr

def ret(t):
    """Return an ast tree that returns t which should be a tree."""
    return ast.Return(t)

def ret_var(v):
    """Return an ast tree that returns the variable v which should be a string."""
    return ret(rval(v))

def assign_var(v, value):
    """Assign the value to v. V should be a string, v a tree."""
    return ast.Assign(targets=[lval(v)], value=value)

def to_code(tree, file="<<generated>>"):
    """Compile the given ast into Python code."""
    print("Compiling:")
    pdump(tree)
    tree = ast.fix_missing_locations(tree)
    return compile(tree, file, 'exec')

