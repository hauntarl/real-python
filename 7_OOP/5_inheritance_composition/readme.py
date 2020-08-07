"""
Inheritance: What common attributes and behaviors exists between real-world
objects, In case of Python - how one class might share more or all of the same
code with another including the attributes and methods.
- Inheritance models an 'is-a' relationship
- Creates a tightly coupled relationship where classes heavily rely on one 
  another


Composition: How are objects in real-world are composed of one another.
- Composition models a 'has-a' relationship
- Creates a loosely coupled relationship that supports changing runtime
  behavior


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

- mixins and further improving design with composition:
	- inheriting mixin class to extend functionality of classes
	- conceptually implementing singleton classes
	- exploring @property annotation - refer employees.py
	- adding a new LTD policy to explore how easy it becomes to add new features
	  when using composition compared to inheritance
	FILES: 
		4_mixins/
			- *


Composition vs Inheritance:
- Use Inheritance over Composition in Python to model a clear 'is-a' 
  relationship
	- Justify the relationship between derived and base class, then reverse it
	  and try to justify it. If you can justify the relationship in both
	  directions, then you should not use inheritance between them
- Use Inheritance over Composition to leverage both the interface and 
  implementation of base class
- Use Inheritance over Composition to provide mixin features to several 
  unrelated classes when there is only one implementation of that feature.
- Use Composition over Inheritance that models a 'has-a' relationship that
  leverages the implementation of the component class.
- Use Composition over Inheritance to create components that can be reused by
  multiple classes in Python application.
- Use Composition over Inheritance in Python to implement groups of behaviors 
  and policies that can be applied interchangeably to other classes to 
  customize their behavior
- Use Composition over Inheritance to enable run-time behavior changes without
  affecting existing classes
"""
