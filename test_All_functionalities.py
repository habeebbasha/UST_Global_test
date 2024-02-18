from UST_Tests.Frequency_of_words import word_frequency
from UST_Tests.shape_square_class import Shape, Square


# Test word_frequency function
def test_word_frequency():
    line = "which is better python 2 or python 3"
    expected_result = [('2', 1), ('3', 1), ('better', 1), ('is', 1), ('or', 1), ('python', 2), ('which', 1)]
    assert word_frequency(line) == expected_result


# Test Shape class
def test_shape_area():
    shape = Shape()
    assert shape.area() == 0


def test_square_area():
    shape = Square(5)
    assert shape.area() == 25
