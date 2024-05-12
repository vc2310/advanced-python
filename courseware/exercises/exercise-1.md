# Exercise 1

## Instructions

You may use the Python documentation, Google, and Generative AI tools to complete the exercise. You may not use solutions in GitHub from prior classes.

## Requirements

1. Create a new folder named `dates_demo` in the `demos` folder.

2. Create a new Python file named `business_days.py` in the `dates_demo` folder. Do all coding for the exercise in the `business_days.py` file.

3. Create a function named "business_days" that returns the business days between a start date and an end date. The date range should be inclusive of the start and end date. Use a generator to implement the function. Check out the `datetime` module for functions to help you implement your code.

4. A business day is defined as any date that is not a weekend or a US holiday. Explore the "holidays" package on PyPi.org to figure out how to determine US holidays.

Note: if Conda does not work, try `pip`: <https://pypi.org/project/holidays/>

```
pip install holidays
```

5. Using the "business_days" function display a listing of all business days between the start and end date in the console. Please display one date per line.

## When you are done

Email me at [eric.greene@atmosera.com](mailto:eric.greene@atmosera.com) to let me know you are done. In the email, include the exercise number, but please do not include the code.
