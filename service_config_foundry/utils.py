

# Converts a string from snake_case to CamelCase.
# Example: "example_name" -> "ExampleName"
def convert_to_camel_case(name):
    # Split the input string on underscores, capitalize each part, and join them back together.
    return "".join([i.capitalize() for i in name.split("_")])

# Converts a string from CamelCase to snake_case.
# Example: "ExampleName" -> "example_name"
def convert_to_snake_case(name):
    # Iterate through each character in the string, prepend an underscore if the character is uppercase,
    # and convert it to lowercase. Strip any leading underscores from the result.
    return ''.join(['_' + char.lower() if char.isupper() else char for char in name]).lstrip('_')

# Merges two dictionaries recursively.
# - If both dictionaries contain a key with a dictionary as its value, merge the inner dictionaries.
# - Otherwise, the value from the second dictionary overwrites the value in the first dictionary.
# Example:
# dict1 = {"a": 1, "b": {"x": 2}}
# dict2 = {"b": {"y": 3}, "c": 4}
# Result: {"a": 1, "b": {"x": 2, "y": 3}, "c": 4}
def merge_dicts(dict1, dict2):
    if not dict1:
        return dict2
    
    if not dict2:
        return dict1
    
    for key, value in dict2.items():
        # If the key exists in both dictionaries and their values are also dictionaries,
        # recursively merge the inner dictionaries.
        if key in dict1 and isinstance(dict1[key], dict) and isinstance(value, dict):
            merge_dicts(dict1[key], value)
        else:
            # Otherwise, overwrite the value in the first dictionary with the value from the second dictionary.
            dict1[key] = value
    
    return dict1