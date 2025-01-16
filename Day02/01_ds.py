# Array

# List
environment = ["dev","prod","stg"]
print(environment)
print(environment[0])
print(environment[1])
print(environment[2])
print(len(environment))
environment.append("test")
print(environment)

# Dictionary

device_info = {
    "Device Type" : "Laptop",
    "Brand" : "HP",
    "Model" : "HP Probook 440 G8",
    "CPU" : 8,
    "RAM" : "16 GB"
}

storage = ["256 GB", "1 TB"]
print(device_info.get("Model"))
device_info.update({"Storage" : storage})
print(device_info)

# Sets

old_device_ids = {0,1,2,3,4,5,6,7,8,9,10} # set of elements
new_device_ids = {10,11,12,13}
print(old_device_ids.union(new_device_ids))

# Tuples

days_of_week = ("Sun","Mon","Tue","Wed","Thus","Fri","Sat")
print(days_of_week)