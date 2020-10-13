
# Steps to set up project  : Windows/Linux

# clone the repo

https://github.com/rajjnish/SortServiceAPI.git

# install dependencies:

pip install -r requirements.txt

# to run tests: 

1) - run the sortserverapi.py from terminal (command line) 

There are two endpoints one for ASC Sorting and second one for Reverse sorting 

/v1/sort         -- response : sorted list {"list": [1, 2, 9, 10]}

/v1/reverse    -- response : sorted list {"list": [10, 9, 2, 1]}

Payload request format:

{"list": [1,10, 9, 2]}


2) Run the tests:  command line:
   
   pytest -m sort_negative -vv test/
   
   pytest -m sort_asc_positive -vv test/
   
   pytest -m sort_rev_positive -vv test/

   
