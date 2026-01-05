import unittest

from dispatching.service import sort


class TestDispatch(unittest.TestCase):
    def test_only_heavy_dispatch(self):
        assert sort(height=1,width=1,length=2,mass=20) == 'SPECIAL'

    def test_only_bulky_dispatch(self):
        assert sort(height=1001,width=10020,length=2000,mass=1) == 'SPECIAL'

    def test_both_bulky_and_heavy_dispatch(self):
        assert sort(height=1000,width=1000,length=2000,mass=20) == 'REJECTED'

    def test_standard_dispatch(self):
        assert sort(height=10,width=10,length=20,mass=19) == 'STANDARD'