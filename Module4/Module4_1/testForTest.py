import pytest
import task as tk


@pytest.mark.parametrize("text, expected",
                         [
                             ("level", True),
                             ("Python", False),
                             ("A man a plan a canal Panama", True),
                             ("No lemon no melon", True),
                             ("Hello", False)
                         ]
                         )
def test_check(text, expected):
    assert tk.is_palindrome(text) == expected

@pytest.mark.parametrize('n,output',[
    (0,1),
    (-10,None),
    (3,6)
])
def test_factorial(n,output):
    assert tk.factorial(n) == output