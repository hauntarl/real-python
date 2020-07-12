s = 'spam ham clam jam'

print('COUNT:')
# getting the count of how many times a substring
# occurred in a particular string
print(f"count of 'am' in '{s}' is {s.count('am')}")
# searching for the occurrence of substring in the given
# range of the string
print(
    f"count of 'am' in '{s[:len(s) // 2]}' is {s.count('am', 0, len(s) // 2)}")

print('\nENDSWITH:')
# determine whether the given string ends with the
# particular substring or not
s = 'baconsausage'
print(f"does '{s}' ends with 'age'? {s.endswith('age')}")
print(
    f"does '{s[:len(s) // 2]}' ends with 'age'? {s.endswith('age', 0, len(s) // 2)}")

print('\nSTARTSWITH:')
# determine whether the given string starts with the
# particular substring or not
print(f"does '{s}' starts with 'bac'? {s.startswith('bac')}")
print(
    f"does '{s[len(s) // 2:]}' starts with 'bac'? {s.startswith('bac', len(s) // 2)}")

print('\nFIND:')
# returns the lowest index where the substring is found
# returns -1 of not found
print(f"In '{s}' found 'sa' at {s.find('sa')}")
print(f"In '{s[6:]}' found 'sa' at {s.find('sa', 6)}")
print(f"In '{s[9:]}' found 'sa' at {s.find('sa', 9)}")

print('\nRFIND:')
# searches the string in reverse order
print(f"In '{s}' found 'sa' at {s.rfind('sa')}")
print(f"In '{s[:8]}' found 'sa' at {s.rfind('sa', 0, 8)}")
print(f"In '{s[:5]}' found 'sa' at {s.rfind('sa', 0, 5)}")

print('\nINDEX:')
# returns the index where the substring is found
# raises ValueError instead of returning -1 if not found
print(f"In '{s}' found 'sa' at {s.index('sa')}")
print(f"In '{s[6:]}' found 'sa' at {s.index('sa', 6)}")
# print(f"In '{s[9:]}' found 'sa' at {s.index('sa', 9)}")  # raises exception

print('\nRINDEX:')
# works similar to rfind but raises ValueError on not found
print(f"In '{s}' found 'sa' at {s.rindex('sa')}")
print(f"In '{s[:8]}' found 'sa' at {s.rindex('sa', 0, 8)}")
# print(f"In '{s[:5]}' found 'sa' at {s.rindex('sa', 0, 5)}")  # raises exception
