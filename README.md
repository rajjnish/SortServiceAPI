
# Steps to set up project  : The set can be done done on Windows or Linux
# Python interpreter : Python3.8

# clone the repo

https://github.com/rajjnish/AptitudeTestSortServiceAPI.git

# install dependencies:

pip install -r requirements.txt

# to run tests: 

- run the sortserverapi.py from terminal (command line) 

There are two endpoints one for ASC Sorting and second one for Reverse sorting 

/v1/sort         -- response {"list": [1, 2, 9, 10]}

/v1/reverse    -- response {"list": [10, 9, 2, 1]}

Payload request format:

{"list": [1,10, 9, 2]}


Run the tests:
- test suites can be run individually from pycharm by setting the "Integrated tool" as Pytest

   or from command line:
   
   pytest -m sort_negative -vv test/
   
   pytest -m sort_asc_positive -vv test/
   
   pytest -m sort_rev_positive -vv test/

   
