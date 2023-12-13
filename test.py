a=20
def f():
    a=2
    def g():
        nonlocal a
        a=a+2
        print(a)
    g()
    print(a)
f()

import re
print(re.findall(r"[a-zA-z]+ing", "walking down and thinking and smiling"))
