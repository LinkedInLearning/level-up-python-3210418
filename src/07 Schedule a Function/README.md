# Python Code Challenge #7: Schedule a Function

Your goal is to implement a function, `schedule_function()`, that takes three inputs arguments for the time at which to run a specified function, the function you want to execute, and a variable number (zero or more) of arguments which are passed to the schedule function to use. 

When your `schedule_function()` is called, it should immediately print a message indicating which function was scheduled and when it will execute.

## Example Test Output
```console
>>> schedule_function(time.time() + 1, print, 'Howdy!')
print() scheduled for Sun Aug 14 20:39:28 2022
```
Then one second later...
```console
Howdy!
```
