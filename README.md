# SGP.Pushshift_API_Caller
This project uses the Pushshift API (https://github.com/pushshift/api) to find the number of users who posted at least 5 submisions and/or comments in a subreddit with a given time period.

## Contents
#### src Directory (for Source code)

**"date_convertor.py"**: provides functions to take a datetime string and convert it into a UNIX epoch timestamp

**"input.py"**: defines a Input class and methods to find the success measure for each subreddit.
  
<li>An instance of the Input class needs: subreddit name as a string (ex.: "UCDavis" for reddit.com/r/UCDavis), a start date, and end date both in Unix Epoch Time
  
<li>An instance can also be initialized with an optional size parameter which tells the API how many entires you want (default is the API's max of 1000)

#### test Directory (for tests)
**"test_date_converter.py"**: contains unittests for date_converter functions (Note: https://www.epochconverter.com was used to confirm accuracy)

**"test_input.py"**: contains unittests for parts of the code in src/input.py


## Instructions for Installation

Please run the following in your terminal:

<code> $ git clone https://github.com/fujirinngo/SGP.Pushshift_API_Caller.git </code>

Packaages to install in your local computer/environment: None?

## Future Features to be Added
<li>Using the csv module so the caller returns a csv file with the subreddit and its number of users with at least 5 comments
  
<li>Streamlining the process more?
  
