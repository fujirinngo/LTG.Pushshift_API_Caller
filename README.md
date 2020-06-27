# SGP.PushshiftAPIParser
This project uses the Pushshift API (https://github.com/pushshift/api) to find the number of users who posted at least 5 comments in a subreddit with a given time period.

## Contents
"src/input.py": defines a Input class and methods to find the success measure
  
  -An instance of the Input class needs: subreddit name as a string (ex.: "UCDavis"), a start date, and end date both in Unix Epoch Time (for conversion use www.epochconverter.com)
  
  -An instance can also be initialized with an optional size parameter which tells the API how many entires you want (default is the API's max of 1000)

## Future Features to Add
-Using the csv module so the parser returns a csv file with the subreddit and its number of users with at least 5 comments

-Streamlining the procress

