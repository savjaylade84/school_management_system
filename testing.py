from Teacher import teacher

t = teacher('0999','sara dutch','math')
print(t.data)

from Guardian import guardian

g = guardian('john','009','brother')

print(g.data)

from Tools import is_none
if is_none(None):
    print('hello')