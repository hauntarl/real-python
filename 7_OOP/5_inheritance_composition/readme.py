"""
Inheritance: What common attributes and behaviors exists between real-world
objects, In case of Python - how one class might share more or all of the same
code with another including the attributes and methods.
- Inheritance models an 'is-a' relationship


Composition: How are objects in real-world composed of one another.
- Composition models a 'has-a' relationship


Interface: description of features and behaviors an object has, not the
implementation of the method but just the declaration.

Some OOP languages have actual mechanisms called interfaces, Python does not
have or need this, because unlike other languages Python supports multiple
inheritance.
NOTE: Interfaces aren't built into Python, but we can use them conceptually
in our UML diagrams.


Liskov Substitution Principle: if S is a subtype or child of class T then 
objects of type T may be replaced with objects of type S without altering any 
desired properties of the program

For more Refer: https://realpython.com/inheritance-composition-python/


In the following examples we will implement:

- a small payroll calculator:
	- explores Inheritance and Interfaces, also sheds some light on abstract
      classes, methods.
  	UML: 
		- https://files.realpython.com/media/ic-initial-employee-inheritance.b5f1e65cb8d1.jpg
  	FILES: 
	  1_example/
    	- payroll.py
    	- employees.py
    	- payroll_calculator.py

- an employee productivity tracker:
  	- extension of the above example
  	UML: 
		- https://files.realpython.com/media/ic-class-explosion.a3d42b8c9b91.jpg
  	FILES: 
	  1_example/
    	- productivity.py
    	- employees.py
    	- productivity_tracker.py

- the diamond problem:
	- encountering the diamond problem in multiple inheritance
	UML: 
		- https://files.realpython.com/media/ic-diamond-problem.8e685f12d3c2.jpg
	FILES: 
	  1_example/
		- employees.py
		- diamond.py
	RESOURCES: 
		- https://medium.com/technology-nineleaps/python-method-resolution-order-4fd41d2fcc

- redesign:
	- to avoid the diamond structure, redesigning the classes
	UML: 
		- https://files.realpython.com/media/ic-class-explosion.a3d42b8c9b91.jpg
	FILES: 
	  2_redesign/
	  	- *

- compositions:
	- extending the functionalities of previous example by using composition and
	  restricting inheritance between classes to minimal by making dependencies
	  loosely coupled with each other, essentially creating a flat structure.
	UML: 
		- https://files.realpython.com/media/ic-policy-based-composition.6e78bdb5824f.jpg
	FILES:
	  3_composition/
	  	- *

- mixins:
	- inheriting mixin class to extend functionality of classes
	FILES: 
		4_mixins/
			- representations.py
			- employees.py
			- contacts.py
			- program.py
"""
