# exporting pydantic models to python dictionary or json

# using one model as a field in another model

from pydantic import BaseModel 

class Address(BaseModel):
    street: str
    city: str
    country: str

class Patient(BaseModel):
    name: str
    age : int
    gender : str
    address: Address 
    
address_dict = {'street': '123 Main St', 'city': 'New York', 'country': 'USA'}
address1 = Address(**address_dict) # this will create an object of Address class
patient_info = {'name': 'John Doe', 'age': 30, 'gender': 'male', 'address': address1} 
patient1 = Patient(**patient_info) # this will create an object of Patient class

#converting to python dictionary 
# temp = patient1.model_dump(include = ['name']) # this will convert the model to python dictionary
temp = patient1.model_dump(exclude = ['name']) # this will convert the model to python dictionary
print(temp) # this will print the dictionary
print(type(temp)) 