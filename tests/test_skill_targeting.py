import pytest
import math
from gameplay import skill_targeting as mod

CASES = [
    ("ground", 'm.ground_hit(2, 0.5, 1) == approx(2)'),
    ("radius", 'm.radius(3, 90) == approx(4.5)'),
    ("inside", 'm.inside((0, 0), (1, 1), (0.5, 0.5)) is True'),
    ("layer", 'm.layer("enemy", "enemy") is True'),
    ("dist", 'm.distance3((0, 0, 0), (1, 2, 2)) == 3'),
    ("blocked", 'm.blocked(2) is True'),
    ("judge", 'm.judge(True, True) is True'),
    ("dead", 'm.deadzone(0.05, 0.1) is False'),
    ("valid", 'm.valid(True) is True'),
    ("nearest", 'm.nearest([3, 1, 2]) == 1'),
    ("clamp", 'm.clamp_radius(9, 5) == 5'),
    ("height", 'm.indicator_height(2) == 2'),
    ("key", 'm.target_key(4) == "t:4"'),
    ("cap", 'm.max_targets(5, 3) == 3'),
    ("dot", 'm.forward_dot(2, 0) == 2')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx, "math": math})
