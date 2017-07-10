import ast
#
# Build the following ast by hand:
#
# print('hello ast', 42)
#
# "Module(body=[Expr(value=Call(func=Name(id='print', ctx=Load()), args=[Str(s='hello world')], keywords=[]))])"

f_name = ast.Name('print', ast.Load())
n = ast.Num(42)
s = ast.Str('Hello ast')

f_call = ast.Call(f_name, [s, n], [])
f_expr = ast.Expr(f_call)
f_mod = ast.Module([f_expr])

ast.fix_missing_locations(f_mod)

c = compile(f_mod, '<hand generated>', 'exec')
eval(c)
