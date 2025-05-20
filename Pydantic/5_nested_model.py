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

print(patient1)
print(patient1.address.street) # this will print the street of the address
print(patient1.address.city) # this will print the city of the address