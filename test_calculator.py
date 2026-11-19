from calculator import CircleArea, multiply, divide, add, sub

def test_multiply():
    assert multiply(6,3) == 18

def test_divide():
    assert divide(6,3) == 2

def test_add():
    assert add(6,5) == 11

def test_sub():
    assert sub(6,5) == 1


def test_circleArea():
    assert CircleArea(-4) == "Error"
