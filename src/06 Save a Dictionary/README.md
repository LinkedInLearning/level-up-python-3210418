# Python Code Challenge #6: Save a Dictionary

Your goal is to implement two functions, `save_dict()` and `load_dict()`. The `save_dict()` function takes two inputs arguments for the dictionary to save and an output file path. The `load_dict()` function takes an input argument of the file path to the saved dictionary and returns its stored dictionary object.

## Example Test Output
```console
>>> save_dict({1: 'a', 2: 'b', 3: 'c'}, 'test.pickle')
print(load_dict('test.pickle'))
{1: 'a', 2: 'b', 3: 'c'}
```
