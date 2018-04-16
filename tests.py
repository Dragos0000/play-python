def test_are_equal (actual, expected):
	assert expected == actual, "Expected {0}, got {1} ".format(expected, actual)


def test_are_not_equal (a, b):
	assert a != b, "The actual value {1} is equal to the test value {0}. They should be different".format(a,b)

def test_is_in (collection, item):
	assert item in collection, "{0} does not contain {1}".format(collection, item)
	
def test_between(value, lowerLimit, upperLimit):
	assert value >= lowerLimit and value <= upperLimit, "{0} is not between {1} and {2}".format(value, lowerLimit, upperLimit)
	
def test_not_in(collection,item):
   assert item not in collection, "{0} is not in {1}".format(item, collection)

test_between(4,1,5)