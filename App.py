from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employees.db'
db = SQLAlchemy(app)

# Employee model
class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    department = db.Column(db.String(50), nullable=False)
    role = db.Column(db.String(50), nullable=False)
    salary = db.Column(db.Integer)

# Routes
@app.route('/employees', methods=['POST'])
def add_employee():
    data = request.json
    emp = Employee(**data)
    db.session.add(emp)
    db.session.commit()
    return jsonify({"message": "Employee added"}), 201

@app.route('/employees', methods=['GET'])
def get_all():
    employees = Employee.query.all()
    return jsonify([{
        "id": e.id, "name": e.name,
        "department": e.department, "role": e.role,
        "salary": e.salary
    } for e in employees])

@app.route('/employees/<int:id>', methods=['PUT'])
def update_employee(id):
    emp = Employee.query.get(id)
    if not emp:
        return jsonify({"error": "Employee not found"}), 404
    data = request.json
    emp.name = data.get("name", emp.name)
    emp.department = data.get("department", emp.department)
    emp.role = data.get("role", emp.role)
    emp.salary = data.get("salary", emp.salary)
    db.session.commit()
    return jsonify({"message": "Employee updated"})

@app.route('/employees/<int:id>', methods=['DELETE'])
def delete_employee(id):
    emp = Employee.query.get(id)
    if not emp:
        return jsonify({"error": "Not found"}), 404
    db.session.delete(emp)
    db.session.commit()
    return jsonify({"message": "Deleted"})

@app.route('/employees/search', methods=['GET'])
def search():
    dept = request.args.get('department')
    role = request.args.get('role')
    query = Employee.query
    if dept:
        query = query.filter_by(department=dept)
    if role:
        query = query.filter_by(role=role)
    results = query.all()
    return jsonify([{
        "id": e.id, "name": e.name, "department": e.department,
        "role": e.role, "salary": e.salary
    } for e in results])

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

