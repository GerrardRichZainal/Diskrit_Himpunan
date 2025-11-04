from himpunan import Himpunan

def test_operasi():
    A = Himpunan(1,2,3)
    B = Himpunan(3,4)
    assert (A + B) == Himpunan(1,2,3,4)
    assert (A / B) == Himpunan(3)
    assert len(A) == 3
