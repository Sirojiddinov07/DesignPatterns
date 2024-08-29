In this  project all focus are given to learning design pattern

# Design patterns are proven solutions to common software design problems. They provide a template or guideline for structuring code in a way that is both reusable and maintainable. These patterns capture best practices and principles used by experienced developers, making them easier to apply across different projects.

# Categories of Design Patterns:
## Creational Patterns:

Focus on object creation mechanisms.
Examples: Singleton, Factory Method, Builder, Abstract Factory.
## Structural Patterns:

Deal with object composition and relationships to form larger structures.
Examples: Adapter, Composite, Decorator, Proxy, Facade.
## Behavioral Patterns:

Concerned with object interaction, communication, and responsibility.
Examples: Observer, Strategy, Command, Chain of Responsibility, State.
Why Use Design Patterns?
Reusability: They provide solutions that can be applied to multiple problems.
Maintainability: They help create code that is easier to manage and extend.
Efficiency: They offer time-tested solutions, reducing the need to solve common problems from scratch.
Communication: They provide a shared vocabulary for developers, improving team collaboration and understanding.





# Singleton Design Pattern
Definition
The Singleton pattern ensures that a class has only one instance and provides a global point of access to that instance. It’s useful when exactly one object is needed to coordinate actions across the system.

Key Characteristics
Single Instance: Only one instance of the class is created.
Global Access Point: The instance is accessible globally.
Controlled Instantiation: The constructor is made private or protected to prevent direct instantiation.
Use Cases
Logger classes
Configuration settings managers
Connection pools
Thread pools

# Factory Design Pattern 
Definition:
The Factory Design Pattern is a creational design pattern used to create objects without specifying the exact class of object that will be created. Instead of calling a constructor directly to create an object, you use a factory method that returns instances of a class based on the input or configuration. This pattern is useful for managing and maintaining the creation logic of objects.

## Key Concepts:
Factory Method: A method for creating objects in a superclass but allowing subclasses to alter the type of created objects.
Product: The interface or abstract class for objects that the factory method creates.
Concrete Product: The actual implementation of the Product interface.
Creator: The class that declares the factory method.
Concrete Creator: The class that implements the factory method.


#  Abstract Factory design pattern

The Abstract Factory design pattern is a creational pattern that provides an interface for creating families of related or dependent objects without specifying their concrete classes. This pattern is particularly useful when a system needs to be independent of how its objects are created and represented.

## Key Concepts
Abstract Factory Interface: Declares a set of methods for creating abstract products.
Concrete Factory Classes: Implement the abstract factory interface and produce concrete products.
Abstract Product Interface: Declares the interface for a type of product object.
Concrete Product Classes: Implement the abstract product interface.

# Builder design pattern 

The Builder design pattern is a creational design pattern used to construct complex objects step by step. Instead of creating the object directly using a constructor, the Builder pattern provides a way to construct a complex object by specifying the type and content of the object it is to produce. It allows you to create different types and representations of an object using the same construction process.

## Key Concepts of the Builder Pattern:
Builder: An abstract interface that defines the methods for creating the parts of a Product object.
Concrete Builder: A class that implements the Builder interface to construct and assemble parts of the product.
Director: Constructs an object using the Builder interface. The Director class is optional and often used to construct the object in a particular sequence.
Product: The complex object that is being constructed.
