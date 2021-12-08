# alta3research-mycode-cert (API design with Python Certification Project)

The objective of this little project is to obtain a Python and RESTful API Certification demonstrating basic proficiency of Python and RESTful APIs.

The script alta3research-flask01.py aims to demonstrate proficiency with the flask library. 

Script alta3research-requests02.py aims to demonstrate proficiency with the requests HTTP library.


## Getting Started
These instructions will get you a copy of the project up and running on your local machine
for development and testing purposes. 

### Prerequisites
TO RUN THE "alta3research-flask01.py" PROGRAM:
- After copying the "alta3research-flask01.py" & "send_request_to_API.py" files on your local machine, you need to put the 4 templates in a sub-directory called templates.
- The "templates" directory must contain the 4 files:
. equipment.html
. home.html
. list.html
. result.html

The IP address and port of the flask server can be changed at the end of the script on the line "app.run(host="0.0.0.0", port=2224, debug=True)" by specifying the host IP address and the port.

Once "alta3research-flask01.py" is executed with python3, a web server will be started and can be accessed with a browser, currently at the address "http://127.0.0.1:2224"

Just follow the directions to :
a) Enter new equipment in the database (
b) View all records of the database as an html page
c) View all records in the database in the JSON format

If desired, "send_request_to_API.py" can be used to send a get request to "http://127.0.0.1:2224/list-json" to view all records in the database in the JSON format.
------------------------------------------------------
TO RUN THE "alta3research-requests02.py" PROGRAM:
As explained in the file "alta3research-requests02.py", this program requires your personal API key that you can generate here:
https://quickfs.net/features/public-api

Then, you need to put that key in a file named "my_quickfs_key" in a directory.
And put this file in the path you will have specified in the variable "key_path" just below the initial imports in the program.

For example:  key_path = "/home/student/.ssh/"

------------------------------------------------------
## Built With

* [Python](https://www.python.org/) - The coding language used

## Authors

* **Benoit Legault** 
