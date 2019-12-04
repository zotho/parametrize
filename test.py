import parametrize

def test_dot():
    dot1 = parametrize.Dot()
    assert str(dot1) == "x: 0.00; y: 0.00", "Bad str implementation"
