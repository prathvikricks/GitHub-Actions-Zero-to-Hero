# app.py
# This is a test commit
#this is a test commit by prathvi
def add(a, b):
    return a + b

def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0
    assert add(12, -2) == 10
    assert add(11, -2) == 9
    assert add(10, -2) == 8 #added this new line
