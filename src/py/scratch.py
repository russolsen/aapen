import ast

# pip/pip3 install astor
# to play with later, getting 'No defined handler for node of type Expression'
# import astor

# navigation via obj api :/
tree = ast.parse("1 + 2", mode="eval")
binop = tree.body
op = binop.op
rnum = binop.right
lnum = binop.left

# get value back with
compiled = compile(
    # this feels in missing line, col. no type junk
    ast.fix_missing_locations(tree),
    # req. but doesn't matter what gets put
    filename='<ast>',
    # series of commands (exec) or value of an expression (eval), also
    # hook for interactive that prints an expression result (single)
    mode='eval'
)
print(eval(compiled))
# 3


def ast_compile(_ast):
    return compile(
        ast.fix_missing_locations(_ast),
        filename='<ast>',
        mode='eval',
    )

mantree = ast.Expression(
    ast.BinOp(
        op=ast.Add(),
        left=ast.Num(1),
        right=ast.Num(2),
    )
)

mancomp = ast_compile(mantree)
print(eval(mancomp))
