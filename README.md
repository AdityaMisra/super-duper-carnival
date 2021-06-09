# super-duper-carnival

* We have some customer records in a text file (customers.txt) -- one customer per line, JSON lines formatted. We want to invite any customer within 100km of our Dublin office for some food and drinks on us. 
* This program will read the full list of customers and output the names and user ids of matching customers (within 100km), sorted by User ID (ascending). 
* You must use the first formula from this Wikipedia article to calculate distance. Don't forget, you'll need to convert degrees to radians. 
* The GPS coordinates for our Dublin office are 53.339428, -6.257664. 
* You can find the Customer list in `resources/customer.txt` file.


### Python setup
    https://realpython.com/installing-python/

    https://www.python.org/downloads/

### Setup the Project
```
pip install . 
```

#### Let's say you want to install a package named foo. Then you do,
```
$ git clone https://github.com/AdityaMisra/super-duper-carnival.git  
$ cd super-duper-carnival
$ python setup.py install
```

#### Instead, if you don't want to actually install it but still would like to use it. Then do,
```
$ python setup.py develop
```

### Run from command line
```
$ python get_invitees.py -h
usage: get_invitees.py [-h] [-r R] [-i I] [-o O]

This program returns a list of customers present with in a radius range

optional arguments:
  -h, --help  show this help message and exit
  -r R        Radius within which we want to invite customers. 
              Default value - 100.0 km
  -i I        File for reading the input. 
              Default value - resources/customer.txt
  -o O        File for writing the output. 
              Default value - resources/output.txtt
                        
python get_invitees.py -r 100 -i resources/customer.txt -o resources/output.txt
```

### From ipython or python prompt
```
from service.invitation_service import InvitationService

invitation_service = InvitationService("resources/customer.txt", "resources/output.txt")
invitation_service.find_customers_within_radius()

```

### How to run the tests
* This command runs the unit test in verbose mode & also reports the coverage
    ```
    pytest --cov . -v
    ```