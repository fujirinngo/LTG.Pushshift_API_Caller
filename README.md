# LTG.Pushshift_API_Caller
This project uses the Pushshift API (https://github.com/pushshift/api) to find the number of users who posted at least 5 submissions and/or comments in a subreddit within a given time period.

## Contents

**pushshift_API_caller.py**: main Python script that combines all the elements; main "interface" to use the project and find the number of users who made 5 submissions or comments to a subbreddit within a given time period.

#### src Directory (for source code)

**date_convertor.py**: provides functions to take a datetime string and convert it into a UNIX epoch timestamp

**input.py**: defines a Input class and methods to find the success measure for each subreddit.
  
<li>An instance of the Input class needs: subreddit name as a string (ex.: "UCDavis" for reddit.com/r/UCDavis), a start date, and end date both in Unix Epoch Time
  
<li>An instance can also be initialized with an optional size parameter which tells the API how many entires you want (default is the API's max of 1000)

#### test Directory (for tests)
**test_date_converter.py**: contains unittests for src/date_converter.py functions (Note: https://www.epochconverter.com was used to confirm accuracy)

**test_input.py**: contains unittests for parts of the code in src/input.py

**sample_json** folder contains json objects that mimics Pushshift API outputs for testing purposes


## Instructions for Installation

Please run the following in your terminal:

<code> $ git clone https://gitlab.com/c2lab_/freygroup/pushshift-api-caller.git </code>

Packaages to install in your local computer/environment: **requests**, **pytz**

The "request" package can be installed by running the following in your terminal:

<code> $ pip install request </code>

Likewise, the "pytz" package can be installed by running the following in your terminal:

<code> $ pip install pytz </code>
