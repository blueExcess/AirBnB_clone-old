# 0x00. AirBnB clone - The console

## Description
What you should learn from this project:

* How to create a Python package
* How to create a command interpreter in Python using the cmd module
* What is Unit testing and how to implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* How to manage datetime
* What is an UUID
* What is *args and how to use it
* What is **kwargs and how to use it
* How to handle named arguments in a function

---

### [0. README, AUTHORS](./README.md)
* 
Write a README.md:


description of the project
description of the command interpreter:


how to start it
how to use it
examples


You should have an AUTHORS file at the root of your repository, listing all individuals having contributed content to the repository. For format, reference Docker’s AUTHORS page
Also, we strongly encourage you to use branches and pull requests on Github - it will help you as team to organize your work



### [1. Be PEP8 compliant!](./tests/)
* Write beautiful code that passes the PEP8 checks.


### [2. Unittests](./models/base_model.py)
* All your files, classes, functions must be tested with unit tests


### [3. BaseModel](./models/base_model.py)
* Write a class BaseModel that defines all common attributes/methods for other classes:


### [4. Create BaseModel from dictionary](./models/engine/file_storage.py)
* Previously we created a method to generate a dictionary representation of an instance (method to_dict()).


### [5. Store first object](./console.py)
* Now we can recreate a BaseModel from another one by using a dictionary representation:


### [6. Console 0.0.1](./console.py)
* Write a program called console.py that contains the entry point of the command interpreter:


### [7. Console 0.1](./models/user.py)
* Update your command interpreter (console.py) to have these commands:


### [8. First User](./models/state.py)
* Write a class User that inherits from BaseModel:


### [9. More classes!](./console.py)
* Write all those classes that inherit from BaseModel:


### [10. Console 1.0](./console.py)
* Update FileStorage to manage correctly serialization and deserialization of all our new classes: Place, State, City, Amenity and Review


### [11. All instances by class name](./console.py)
* Update your command interpreter (console.py) to retrieve all instances of a class by using: <class name>.all().


### [12. Count instances](./console.py)
* Update your command interpreter (console.py) to retrieve the number of instances of a class: <class name>.count().


### [13. Show](./console.py)
* Update your command interpreter (console.py) to retrieve an instance based on its ID: <class name>.show(<id>).


### [14. Destroy](./console.py)
* Update your command interpreter (console.py) to destroy an instance based on his ID: <class name>.destroy(<id>).


### [15. Update](./console.py)
* Update your command interpreter (console.py) to update an instance based on his ID: <class name>.update(<id>, <attribute name>, <attribute value>).


### [16. Update from dictionary](./tests/test_console.py)
* Update your command interpreter (console.py) to update an instance based on his ID with a dictionary: <class name>.update(<id>, <dictionary representation>).


---

## Author
* **Nathan Petersen** - [blueExcess](https://github.com/blueExcess)



## Console
* How to start:
	To begin, please run the file "console.py". `./console.py`
### Commands:
* quit
	No arguments - will exit the console. `quit`
* help [command]
	Can run with no arguments to show what commands there are. Running with an argument (a command) will give you details about that command.
	`help` and `help quit`
* create <model_name>
	Will create a new instance of the indicated model, and then print the id of the new object. Accepted models are: BaseModel, User, State, City, \
Amenity, Place, and Review.
	`create BaseModel`
* show <model_name, id>
	Will show indicated model.
	`show BaseModel 8173-i3880-andn83`
* destroy <model_name, id>
	Will delete the indicated object.
	`destroy Amenity 9182-8373-8177393`
* all [model_name]
	Print all currently existing objects to output. If given a model_name, will print all current instances of indicated model.
	`all` or `all User`
* update <model_name, id, attribute [value (str, int, or float)]>
	Update the indicated object with the given attribute, which will have the value indicated.
	`update BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com"`
