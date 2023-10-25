from task import is_prime, primes, checksum, pipeline

def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(4) == False

def test_primes():
    assert primes(5) == [2, 3, 5, 7, 11]
    assert len(primes(5)) == 5

def test_checksum():
    assert checksum([2, 3, 5, 7, 11]) == 5124642

def test_pipeline():
    assert pipeline() == 7785816

if __name__ == '__main__':
    test_is_prime()
    test_primes()
    test_checksum()
    test_pipeline()
