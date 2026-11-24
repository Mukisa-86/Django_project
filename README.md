**FOOD MANAGEMENT SYSTEM
 TOOLS AND TECHNOLOGIES**
Technology	-Purpose
Python	-Main programming language.
Django	Web framework -for backend logic and page handling.
HTML	-Creates the web pages.
SQLite	-Stores application records.
Django REST Framework	-Provides REST API endpoints.
Visual Studio Code	-Code editor.
Web browser	-Used to access the system.
** MAIN SYSTEM FUNCTIONS**
View foods: Displays food records saved in the database.
Search foods: Helps find a food record.
Add food: Saves a food name, price and description.
Update food: Changes details of an existing food record.
Delete food: Removes a record after confirmation.
API access: Allows food data to be accessed through API endpoints.
** DATABASE DESIGN**
The main database model is Food. Its fields are:
Field	Meaning
id	-Automatically generated unique record number.
name	-Name of the food.
price	-Price of the food.
description	-Additional details about the food.
created_at	--Date and time the record was created.
update_at	--Date and time the record was last updated, according to the model field name.
A Product model may also be present with name, category, price and expiry fields. The main web pages in this documentation manage Food records.
 
** PROJECT FOLDER STRUCTURE**
rest/
├── manage.py
├── rest/
│├── settings.py
│└── urls.py
└──super/
    ├──models.py
    ├──views.py
    ├──serialisers.py
    ├──urls.py
    ├──admin.py
    └──templates/
        └──foods/
            ├──food_list.html
            ├──food_form.html
            └── food_confirm_delete.html
  HOW TO RUN THE SYSTEM?
Step 1: Open the project folder in the terminal and activate your Python virtual environment, Start the local server by running: python manage.py runserver

 
Step 2 : Open a browser and go to http://127.0.0.1:8000/super  for the web interface, or test http://127.0.0.1:8000/food  in Postman and http://127.0.0.1:8000/admin for the super user.
 
 
	 
 
MAIN PAGES AND API ROUTES
Route	Purpose
/app/	Food management page.
/app/add/	Add a food record.
/app/<id>/edit/	Update a selected record.
/app/<id>/delete/	Confirm and delete a record.
/food/	Food API endpoint.
/food/<id>/	API endpoint for one food record.
The exact routes depend on the URL patterns in your project. Check super/urls.py if a route is different.
 TESTING
•	Open the food page and check that records are displayed.
•	Add a food record and confirm it appears in the list.
•	Edit a record and confirm the changes are saved.
•	Delete a test record and confirm it is removed.
•	Search for a food record.
•	Open the API endpoint and check that it returns food data.
 FUTURE IMPROVEMENTS
•	Add user registration and login.
•	Add user roles and access permissions.
•	Add stock quantities and low-stock notifications.
•	Add expiry-date reminders and reports.
•	Improve the design for mobile phones.
•	Deploy the application to secure web hosting.
 
Figure 1: The Home Dashboard
 
Figure 2: Add Food Item Form
 
Figure 3:Edit Food Item Form
 
Figure 4: Delete Food Item Form
 
Figure 5: GET Method in Echo API
 
Figure 6: POST Method in Echo API
 
Figure 7: PUT Method in Echo API
 
Figure 8: PATCH Method in Echo API
 
Figure 9: DELETE Method in Echo API
 
Figure 10: Error response of Bad Request after the wrong data entry on Price


Figure 11: Error response of Not Found

