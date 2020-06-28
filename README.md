# SGP.PushshiftAPIParser
This project uses the Pushshift API (https://github.com/pushshift/api) to find the number of users who posted at least 5 comments in a subreddit with a given time period.

## Contents
### src Directory (for Source code) ###

"src/input.py": defines a Input class and methods to find the success measure
  
<li>An instance of the Input class needs: subreddit name as a string (ex.: "UCDavis"), a start date, and end date both in Unix Epoch Time (for conversion use www.epochconverter.com)</li>
  
<li>An instance can also be initialized with an optional size parameter which tells the API how many entires you want (default is the API's max of 1000)</li>
  
 
### test Directory (for tests) ###

<li>"test/testInput.py": contains unittests for parts of the code in src/input.py</li>

## Future Features to Add
<li>Using the csv module so the parser returns a csv file with the subreddit and its number of users with at least 5 comments</li>

<li>Streamlining the procress<li/>

