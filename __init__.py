from employees import Employee, Manager
from flask import Flask, jsonify, request
app = Flask(__name__)

mgr = Manager()

@app.route('/employees', methods = ['GET', 'POST'])
def all_employee_handler():
  if request.method == 'GET':
    data = mgr.get_all()
    if data is  None:
      return jsonify({"error":"cannot get all employees"})
    return jsonify({'data':data})
  elif request.method == 'POST':
    data = request.json['data']
    emp = Employee(data['name'], data['address'], data['salary'], data['salary'])
    data = mgr.addEmployee(emp)
    print data
    if data is None:
      return jsonify({"error":"cound not add employee"})
    return jsonify({'id':data})


    
@app.route('/employees/<int:id>', methods = ['GET','PUT'])
def employee_handler(id):
  if request.method == 'GET':
    data = mgr.get_by_id(id)
    if data is None:
      return jsonify({"error":"unable to get employee with id %s"%id})
    return jsonify(data)
  elif request.method == 'PUT':
    data = request.json['data']
    emp = mgr.update_by_id(id, data)
    if emp is None:
      return jsonify({"error":"unable to update employee with id %s"%id})
    return jsonify(data)

    

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)