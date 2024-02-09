def unique_elements(input_list):
    
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

# Example usage:
original_list = [1, 2, 2, 3, 4, 4, 5]
result = unique_elements(original_list)
print("Original List:", original_list)
print("List with Unique Elements:", result)
