## Buzz Fizz
My solution to the modified `fizzbuzz` classic posed by SwiftNav at https://github.com/swift-nav/screening_questions/blob/master/questions.md#swift-navigation-application-questions

- "Buzz" when F(n) is divisible by 3.
- "Fizz" when F(n) is divisible by 5.
- "FizzBuzz" when F(n) is divisible by 15.
- "BuzzFizz" when F(n) is prime.
- the value F(n) otherwise.

## Run me 
Simple! Just run from the command line with a Python 2/3 interpreter. Optional `--debug` argument will print out the Fibonacci sequence number, the actual fibonacci number, as well as the fizzbuzzed encoding. 

```
python fizzbuzz.py 12
```
![Imgur](http://i.imgur.com/nJj8inM.png)

## Env
Dependencies and requirements are pretty minimal, and you can create your own setup with your very own custom made Anaconda environment using the included `environment.yml` file. (http://conda.pydata.org/docs/using/envs.html)

```
conda env create -f environment.yml
source activate fizzbuzz
```

![Imgur](http://i.imgur.com/AO2apmR.png)

## Tests
Tests are included in a combo of `doctest` strings for expressionable verifiers, and `pytest` tests for more involved functionality tests. Both can be ran through the `pytest` utility. If all goes well, you should see minimal output. 

```
pytest --doctest-modules fizzbuzz.py
pytest fizzbuzz.py
```
![Imgur](http://i.imgur.com/Cl1xerY.png)
