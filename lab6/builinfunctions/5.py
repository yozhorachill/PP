#5
def all_true(elements):
    return all(elements)

# Example usage
tuple1 = (True, True, False, True)
tuple2 = (True, True, True)

print("All elements in tuple1 are true:", all_true(tuple1))
print("All elements in tuple2 are true:", all_true(tuple2))