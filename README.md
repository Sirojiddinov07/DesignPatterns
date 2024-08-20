In this  project all focus are given to learning design pattern

Design Patterns: A Brief Overview
Design patterns are proven solutions to common software design problems. They provide a template or guideline for structuring code in a way that is both reusable and maintainable. These patterns capture best practices and principles used by experienced developers, making them easier to apply across different projects.

Categories of Design Patterns:
Creational Patterns:

Focus on object creation mechanisms.
Examples: Singleton, Factory Method, Builder, Abstract Factory.
Structural Patterns:

Deal with object composition and relationships to form larger structures.
Examples: Adapter, Composite, Decorator, Proxy, Facade.
Behavioral Patterns:

Concerned with object interaction, communication, and responsibility.
Examples: Observer, Strategy, Command, Chain of Responsibility, State.
Why Use Design Patterns?
Reusability: They provide solutions that can be applied to multiple problems.
Maintainability: They help create code that is easier to manage and extend.
Efficiency: They offer time-tested solutions, reducing the need to solve common problems from scratch.
Communication: They provide a shared vocabulary for developers, improving team collaboration and understanding.





Singleton Design Pattern
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