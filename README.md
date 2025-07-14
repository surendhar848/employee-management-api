# Employee Management API 🧑‍💼

A RESTful API built using Python (Flask) and SQLite to manage employee records. Supports full CRUD operations with features like search by department and role.

## 🔧 Technologies Used
- Python
- Flask
- SQLAlchemy (ORM)
- SQLite
- Postman (for API testing)

## 🚀 Features
- Add new employees
- View all employees
- Update employee info
- Delete employee
- Search by department or role

## 📂 API Endpoints

| Method | Endpoint            | Description               |
|--------|---------------------|---------------------------|
| POST   | /employees          | Add new employee          |
| GET    | /employees          | View all employees        |
| PUT    | /employees/<id>     | Update employee by ID     |
| DELETE | /employees/<id>     | Delete employee by ID     |
| GET    | /employees/search   | Filter by dept or role    |

## 🧪 Example POST Request (JSON)
```json
{
  "name": "Surendhar",
  "department": "IT",
  "role": "Backend Developer",
  "salary": 55000
}
