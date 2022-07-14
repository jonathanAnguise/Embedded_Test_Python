# Embedded Test Python
> It's a test divided in 2 parts, moore info see pdf file (not in the repo). 
## Part 1: Unit Testing
Create 3 parameterized functions:
1. A function that given 2 vectors of integers finds the first repeated number
2. A function that given a path of the file finds the fist file that meets the folloring requirements:
   * The file owner is admin
   * The file is executable
   * The file has a size lower than 14*2<sup>20</sup>

3. A function that given a sequence of coin flips (0 is tails, 1 is heads) finds the
minimum quantity of permutations so that the sequence ends interspersed. For
example, given the sequence 0,1,1,0 how many changes are needed so that the
result is 0,1,0,1

Functions are in main.py, tests are in tests/test_functions.py
After cloning the repo, and before execution please make sure to have a venv and run:
```python
pip3 install -r requirements.txt
```
To execute tests, run:
```bash
python -m pytest tests/test_functions.py
```

## Part 2: System Testing
Here is the markdown file of the exercice:
* [link](https://github.com/jonathanAnguise/Embedded_Test_Python/blob/main/Part_2_System_testing.md)
