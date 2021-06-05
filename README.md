# super-duper-carnival

* We have some customer records in a text file (customers.txt) -- one customer per line, JSON lines formatted. We want to invite any customer within 100km of our Dublin office for some food and drinks on us. 
* This program will read the full list of customers and output the names and user ids of matching customers (within 100km), sorted by User ID (ascending). 
* You must use the first formula from this Wikipedia article to calculate distance. Don't forget, you'll need to convert degrees to radians. 
* The GPS coordinates for our Dublin office are 53.339428, -6.257664. 
* You can find the Customer list in `customer.txt` file.


### Python setup
    https://realpython.com/installing-python/

    https://www.python.org/downloads/

### where’s the main entry point? 
```
from service.invitation_service import InvitationService

invitation_service = InvitationService("resources/customer.txt", "resources/output.txt")
invitation_service.find_invitees_within_radius()

```
### How to run the tests
* This command runs the unit test in verbose mode & also reports the coverage
    ```
    pytest --cov . -v
    ```