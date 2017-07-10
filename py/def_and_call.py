import ast
#
# Build the following ast by hand:
#
# def add2(a, b):
#  result = a + b
#  return result
#
#"Module(body=[
# FunctionDef(name='add2', 
#             args=arguments(args=[arg(arg='a', annotation=None), arg(arg='b', annotation=None)],
#             vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]), body=[Assign(targets=[Name(id='result', ctx=Store())], value=BinOp(left=Name(id='a', ctx=Load()), op=Add(), right=Name(id='b', ctx=Load()))), Return(value=Name(id='result', ctx=Load()))], decorator_list=[], returns=None)])"

def pdump(tree):
  """Print the ast tree."""
  print(ast.dump(tree))

def wrap_args(args):
  """Wrap the strings passed in in ast arg objects."""
  return list(map(lambda q: ast.arg(arg=q, annotation=None), args))

def mk_arguments(args):
  """Take an array of strings and turn them into an arguments instance."""
  a =ast.arguments(
          args=wrap_args(args),
          vararg=None, kwonlyargs=[],
          kw_defaults=[], kwarg=None, defaults=[])
  return a

def mk_func(name, args, body):
  """Make a function with the given name, positional args and body. All should be trees."""
  wrapped_args = mk_arguments(args)
  f=ast.FunctionDef(name=name, args=wrapped_args, body=body, decorator_list=[], returns=None)
  return f

def mk_add(left, right):
  """Return an ast tree that adds the two arguments together."""
  return ast.BinOp(op=ast.Add(), left=left, right=right)

def mk_name(s, rval=True):
  """Make an ast Name object. If rval is true then it loads the name, otherwise stores it."""
  if rval:
    return ast.Name(s, ast.Load())
  else:
    return ast.Name(s, ast.Store())

def mk_ret(t):
  """Return an ast tree that returns t which should be a tree."""
  return ast.Return(t)

def mk_ret_var(v):
  """Return an ast tree that returns the variable v which should be a string."""
  return mk_ret(mk_name(v))

def mk_assign_var(v, value):
    """Assign the value to v. V should be a string, v a tree."""
    return ast.Assign(targets=[mk_name(v, False)], value=value)

def mk_code(tree, file="<<generated>>"):
  """Compile the given ast into Python code."""
  tree = ast.fix_missing_locations(tree)
  print("making code:", ast.dump(tree))
  return compile(tree, file, 'exec')

n1 = ['a', 'b']

f_args = mk_arguments(n1)

f_body = [
        mk_assign_var('result',
            mk_add(mk_name('a'), mk_name('b'))),
        mk_ret_var('result')]

fd = mk_func('add2', ['a', 'b'], f_body)

m = ast.Module(body=[fd])

c = mk_code(m)
eval(c)

print(add2(1,44))
