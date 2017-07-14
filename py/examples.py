from pyast import *
from munge import *


def add2(a,b):
    print("add2 called with", a, b)
    return a+b

# (println 44)

m = mod('m', [expr(println(n(44)))])

eval(to_code(m))


# (println (add2 1 10))

m = mod('m', [expr(println(call('add2', [n(1), n(10)])))])

eval(to_code(m))


# (defn same [a] a)

m = mod('exm', [func('same', ['a'], [ret_var('a')])])
print(eval(to_code(m)))

print(same(4444))

# (defn addx [a b] (+ a b))

m = mod('exm',
        [func('addx', ['a','b'],
            [assign_var('result', add(rval('a'), rval('b'))), 
             ret_var('result')])])

print(eval(to_code(m)))

print(addx(1,20))

# (if 44 1 0)


m = mod('m', [ifelse(n(44), [expr(println((n(9))))], [expr(println(n(0)))])])

# (print;n (if 44 1 2))


print(eval(to_code(m)))
