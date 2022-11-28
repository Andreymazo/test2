from Zadacha.zadacha_2 import set_


def test_set_1():
    true_data = 3
    test_dict = {
        "a": {"b": {"c": 4}}
    }
    set_(test_dict, ["a", "b", "c"], 3)
    assert test_dict["a"]["b"]["c"] == true_data

def test_set_2():
    true_data = 4
    test_dict = {
        "a": {"b": {"c": 5}}
    }
    set_(test_dict, ["a", "b", "c"], 4)
    assert test_dict["a"]["b"]["c"] == true_data

def test_set_3():
    true_data = 4
    test_dict = {
        "a": {"b": {"c": 5}}
    }
    set_(test_dict, ["x", "y", "z"], 4)
    assert test_dict["x"]["y"]["z"] == true_data

def test_set_4():
    true_data = 5
    test_dict = {
        "a": {"b": {"c": 6}}
    }
    set_(test_dict, ["a", "b", "z"], 5)
    assert test_dict["a"]["b"]["z"] == true_data