# Food Management System

A web-based application and RESTful API built with Python, Django, and Django REST Framework for managing food records. Users can view, search, add, update, and delete food items through a clean web interface or interact with the data programmatically via API endpoints.

**Student:** Mukisa Moureen  
**Reg. No:** 24/446BSE/AP/U  

---

## Tools & Technologies

| Technology | Purpose |
| :--- | :--- |
| **Python** | Main programming language |
| **Django (v6.0.6)** | Web framework for backend logic and page handling |
| **Django REST Framework** | Provides REST API endpoints |
| **SQLite** | Stores application records |
| **HTML** | Creates the web pages |
| **Visual Studio Code** | Code editor |
| **EchoAPI / Postman** | Used for testing REST API endpoints |

---

## Main System Functions

* **View Foods:** Displays all food records saved in the database.
* **Search Foods:** Filter and find specific food records by name.
* **Add Food:** Create and save a new food item with a name, price (UGX), and description.
* **Update Food:** Edit and save changes to existing food records.
* **Delete Food:** Safely remove records after user confirmation.
* **REST API Access:** Perform full CRUD (`GET`, `POST`, `PUT`, `PATCH`, `DELETE`) operations via JSON endpoints.
* **Admin Panel:** Built-in Django administration dashboard for managing `Food` and `Product` models.

---

## Database Design

### `Food` Model (Primary)

| Field | Type / Meaning |
| :--- | :--- |
| `id` | Automatically generated unique record number |
| `name` | Name of the food item |
| `price` | Price of the food item (UGX) |
| `description` | Additional details about the food |
| `created_at` | Timestamp when the record was created |
| `update_at` | Timestamp when the record was last updated |

*(Note: A secondary `Product` model with `name`, `category`, `price`, and `expiry` fields is also registered in the admin interface.)*

---

## Project Folder Structure

```text
rest/
├── manage.py
├── rest/
│   ├── settings.py
│   └── urls.py
└── super/
    ├── admin.py
    ├── models.py
    ├── serialisers.py
    ├── urls.py
    ├── views.py
    └── templates/
        └── foods/
            ├── food_list.html
            ├── food_form.html
            └── food_confirm_delete.html
```


---

## How to Run the System

### 1. Activate Virtual Environment & Start Server
Open your terminal in the project root directory, activate your Python virtual environment, navigate into the `rest` directory, and run the development server:

```bash
# Windows PowerShell activation example
.\venv\Scripts\Activate.ps1

# Navigate to project directory and run server
cd rest
python manage.py runserver
```
*(Or use `py manage.py runserver` depending on your Python installation.)*

### 2. Access the Application
Once the server is running at `http://127.0.0`, open your browser or API client to access:

* **Web Dashboard:** `http://127.0.0super/`
* **REST API Root:** `http://127.0.0food/`
* **Django Admin Panel:** `http://127.0.0admin/`

---

## Main Pages & API Routes

### Web Interface Routes

| Route | Purpose |
| :--- | :--- |
| `/super/` | Main food management dashboard (View & Search) |
| `/super/add/` | Form to add a new food record |
| `/super/<id>/edit/` | Form to update a selected food record |
| `/super/<id>/delete/` | Confirmation page to delete a record |

### REST API Endpoints

| Endpoint | Allowed Methods | Purpose |
| :--- | :--- | :--- |
| `/food/` | `GET`, `POST`, `OPTIONS` | Retrieve all food records or create a new one |
| `/food/<id>/` | `GET`, `PUT`, `PATCH`, `DELETE` | Retrieve, update, partially update, or delete a specific record |

*(Note: Check `super/urls.py` if custom route prefixes like `/app/` are configured in your local branch.)*

---

## Testing Checklist

- [ ] Open `/super/` and verify that existing food records load properly.
- [ ] Add a new food record and confirm it appears in the list.
- [ ] Edit an existing record and verify changes persist.
- [ ] Delete a test record after confirming on the delete prompt.
- [ ] Use the search bar to filter food items by name.
- [ ] Test `GET`, `POST`, `PUT`, `PATCH`, and `DELETE` requests against `/food/` and `/food/<id>/` using EchoAPI or Postman (including `400`/`405` bad request handling and `404` not found responses).

---

## Future Improvements

* Add user registration and login authentication.
* Implement user roles and access permissions.
* Add stock quantity tracking and low-stock notifications.
* Add expiry-date reminders and inventory reports.
* Enhance responsive styling for mobile devices.
* Deploy the application to a secure production web host.
