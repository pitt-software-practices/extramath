
import pytest
from pytest import approx

import extramath
from extramath.sqrt import sqrt

def test_sqrt():
    assert sqrt(4.0) == approx(2.0)
