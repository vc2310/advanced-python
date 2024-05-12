# Exercise 2

## Instructions

You may use the Python documentation, Google, and Generative AI tools to complete the exercise. You may not use solutions in GitHub from prior classes.

## Requirements

1. Install the "requests" package from PyPi.org. Create a new file named `get_rates.py`. Do all coding in the new file.

2. Using the "requests" package API, call the following URL for each date returned from the "business_days" function. If you are using a Codespace use the localhost address (127.0.0.1:8080) and http (not https) to call the endpoint from your Python code.

<http://127.0.0.1:8080/api/2019-01-01?base=USD&symbols=EUR>

Iterate over a range of business days, and run the above request for each day.

3. Create a list of text values from each response. The text value is formatted as JSON. Do not parse the JSON. Just put each JSON response in the list.

4. Display each list item in the console.

## When you are done

Email me at [eric.greene@atmosera.com](mailto:eric.greene@atmosera.com) to let me know you are done. In the email, include the exercise number, but please do not include the code.
