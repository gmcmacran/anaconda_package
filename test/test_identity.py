from gregs_conda_package.identity import identity


def test_identity_returns_same_value():
    assert identity(5) == 5
    assert identity("Greg") == "Greg"
    assert identity([1, 2, 3]) == [1, 2, 3]


def test_identity_returns_same_object_for_mutables():
    data = [1, 2, 3]
    result = identity(data)
    assert result is data


def test_identity_does_not_modify_input():
    original = {"a": 1}
    returned = identity(original)
    assert returned == original
    assert returned is original
