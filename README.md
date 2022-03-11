
# PMEC : Parallel Markets Engineering Challenge

Quickly written to meet the core engineering challenge for the Parallel Markets interview process.

Written in Python3 with Flask, SQLAlchemy, and Werkzeug Utilities

* Optionally uses 'virtualenv' ("pip3 install virtualenv")
* Requires 'Python3' to be installed ("brew install python@3.10")
* Requires 'Flask' and 'SQLAlchemy' to be installed ("pip3 install flask sqlalchemy flask-sqlalchemy")

Initialize the database in the project working directory via the Python3 command line with the following commands:
* "from pmec import db"
* db.create_all()

Run the web application in the project working directory with the following command:
* python3 pmec.py

The web application should be available in your web browser via localhost at port 5000 (only tested with Chrome)

---

Basic form structure allows for adding new user records (all form fields required), listing all currently created records, updating the first and last names of any record, and uploading files per record

All uploaded files are placed in the "upload" subdirectory of the project working directory.

---

REQUIREMENTS

Create a web application that allows a partner user to input an investor's information (list below) and at least 1 file into a form. The partner user should be able to submit the form and then enter the next investor's information. When the form is submitted, the investor information should be stored in a relational database, and the file should be stored on the server's filesystem. You may use any language, framework, or tools that you'd like, as long as they are free and open source and can be run on either a Linux or Mac OS X machine. Your web application does not need authentication or authorization capabilities. Assume that uploaded files won't exceed 3 MB in size and that all input fields should be required.

The investor information that should be accepted (along with at least 1 file for upload) includes:

Investor first name
Investor last name
Investor date of birth
Investor phone number
Investor street address (assume US addresses only)
Investor state (assume US addresses only)
Investor zip code (assume US addresses only)
Please include detailed instructions in a README file describing in full the process to setup/install any prerequisite software, initialize the relational database, and run the web application.

---

TASKS COMPLETED (after alotted 2 hours):

* All core requirements met

---

EXTRA CREDIT COMPLETED (after alotted 2 hours):

* Fully documenting both what you were able to complete and what you would want to do additionally if you had more time
* A full git history showing your development style.
* Detecting and handling updating addresses for existing customers with matching names/SSNs (partially)

---

EXTRA CREDIT INCOMPLETE (after alotted 2 hours):

* Authentication and authorization capabilities
* Support for files larger than 3MB (upload progress indicator, etc)
* Support for SSNs and record disambiguation
* Tests

---

ADDITIONAL DESIRED FEATURES COMPLETED (after alotted 2 hours):

* Built as a full CRUD app (create, retrieve, update, delete)
* Limited file upload to only certain file extension types
* Tried to prevent shenanigans with bad actor file uploads via Werkzeug 'secure_filename' utilities

---

ADDITIONAL DESIRED FEATURES INCOMPLETE (after alotted 2 hours):

* Sorting and searching database
* CSS styling
* Unique key (hash or incrementing index?) per record (indexed)
* Stronger field typing, error checking, and messaging
* Fix the filename record display

---

Copyright [2022] [Jonathan T. Beard]

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.


