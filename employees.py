
class Employee(object):
	"""docstring for Employee"""
	def __init__(self, name, address, department, salary):
		self.name = name
		self.address = address
		self.department = department
		self.salary = salary
		self.id = -1
		
	def get_name(self):
		return self.name

	def get_address(self):
		return self.address

	def get_department(self):
		return self.department

	def get_salary(self):
		return self.salary

	def get_id(self):
		return self.id
		
	def set_name(self, name):
		self.name = name

	def set_address(self, address):
		self.address = address

	def set_department(self, department):
		self.department = department

	def set_salary(self, salary):
		self.salary = salary

	def set_id(self, id):
		self.id = id
		
	def calculateTax(self):
		rate = .1
		yearly_salary = self.salary * 12
		tax = (yearly_salary - 60000) * rate 
		return tax/12

	def to_json(self):
		return {"id":self.id, "name":self.name, "address":self.address, "department":self.department, "salary":self.salary}



class Manager(Employee):
	"""docstring for Manager"""

	def __init__(self):
		self.employees = []
		
	def get_all(self):
		return [e.to_json() for e in self.employees]

	def get_by_id(self, id):
		if id < 0 or id > len(self.employees):
			return None
		return self.employees[id].to_json()

	def update_by_id(self, id, data):
		if id < 0 or id > len(self.employees):
			return None
		emp = Employee(**data)
		self.employees[id] = emp
		return emp.to_json()


	def addEmployee(self, emp):
		if len(self.employees) == 0:
			if isinstance(emp, Employee):
				id = len(self.employees)
				emp.set_id(id)
				self.employees.append(emp)
				return id
			else:
				print "Not an Employee object"
				return None
		else:
			for e in self.employees:
				if isinstance(emp, Employee):
					print "instance"
					if emp.name == e.name:
						print "Employee %s already exists"%emp.name
						return None
					else:
						id = len(self.employees)
						emp.set_id(id)
						self.employees.append(emp)
						return id
				else:
					print "Not an Employee object"
					return None


