import pytest

import parametrize

class TestDot:
    dot_1 = parametrize.Dot()
    

    def test_str(self):
        assert str(self.dot_1) == "t: 0.00; x: 0.00; y: 0.00", "Bad str implementation"

    @pytest.mark.parametrize(
        ("key", "value"),
        [
            ("x", 100),
            ("y", 100.000001),
            ("y", 1.3e-199),
        ]
    )
    def test_properties(self, key, value):
        setattr(self.dot_1, key, value)
        actual_value = self.dot_1.state[{"x": 1, "y": 2}[key]]
        assert actual_value == value, "Value is not stored"