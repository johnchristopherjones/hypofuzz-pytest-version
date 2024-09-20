from hypothesis import given, strategies as st

@given(st.integers())
def test_anything(a):
    assert True