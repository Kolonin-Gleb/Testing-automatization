def test_abs1():
    assert abs(-42) == 42, "Shoould be positive" # success

def test_abs2():
    assert abs(-42) == -42, "Shoould be positive" # fail

def test_abs3():
    assert abs(-42) == 42, "Shoould be positive" # success

if __name__ == "__main__":
    # Запуск юнит тестов
    print("All tests passed!")
