<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>

<h1>Armed Forces OOP Project</h1>

<p>This project serves as a practical demonstration of Object-Oriented Programming (OOP) concepts through the modeling of different branches of the armed forces: Army, Navy, and Air Force. Each class in this implementation showcases core OOP principles, including abstraction, encapsulation, inheritance, and polymorphism.</p>

<h2>Table of Contents</h2>
<ul>
    <li><a href="#features">Features</a></li>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#code">Code Overview</a></li>
    <li><a href="#concepts">OOP Concepts Explained</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
</ul>

<h2 id="features">Features</h2>
<ul>
    <li><strong>Abstract Classes:</strong> The <code>ArmedForce</code> abstract class defines common properties and methods that all armed forces must implement, enforcing a consistent interface.</li>
    <li><strong>Inheritance:</strong> The <code>Army</code>, <code>Navy</code>, and <code>AirForce</code> classes inherit from <code>ArmedForce</code>, allowing for code reuse and organization.</li>
    <li><strong>Encapsulation:</strong> Private attributes (e.g., <code>__name</code>, <code>__personnel</code>) protect the internal state of objects, while public methods allow controlled access and modification.</li>
    <li><strong>Polymorphism:</strong> Each military branch implements its own versions of methods like <code>primary_function()</code> and <code>training()</code>, demonstrating how different classes can provide specific implementations of the same interface.</li>
    <li><strong>Deployment Logic:</strong> The <code>deploy()</code> method in <code>ArmedForce</code> allows for flexible deployment of units based on various parameters.</li>
</ul>

<h2 id="installation">Installation</h2>
<pre><code>git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
</code></pre>
<p>No additional dependencies are required to run this project. Ensure you have Python 3.x installed.</p>

<h2 id="usage">Usage</h2>
<pre><code>python main.py
</code></pre>
<p>Executing the above command will run the main program, which initializes instances of each armed force and demonstrates their functionality through method calls and outputs.</p>

<h2 id="code">Code Overview</h2>
<p>The project is organized into several classes, each representing a different branch of the armed forces. Below is a brief overview of the core classes:</p>

<pre><code>from abc import ABC, abstractmethod

class ArmedForce(ABC):
    def __init__(self, name, personnel):
        self.__name = name  
        self.__personnel = personnel 

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_personnel(self):
        return self.__personnel

    def set_personnel(self, personnel):
        self.__personnel = personnel

    @abstractmethod
    def primary_function(self):
        pass

    @abstractmethod
    def training(self):
        pass

    def deploy(self, *args):
        if len(args) == 0:
            return "Deploying standard units."
        elif len(args) == 1:
            return f"Deploying {args[0]} units."
        else:
            return f"Deploying {args[0]} units from {args[1]}."
</code></pre>

<h3>Army Class</h3>
<pre><code>class Army(ArmedForce):
    def __init__(self, name, personnel, ground_units):
        super().__init__(name, personnel) 
        self.ground_units = ground_units  

    def primary_function(self):
        return "The Army's primary function is land defense and ground operations."

    def training(self):
        return "The Army training includes physical endurance, weapons handling, and battlefield tactics."
    
    def deploy_ground_units(self, units=None):
        if units:
            return f"Deploying {units} ground units for operation."
        return f"Deploying {self.ground_units} standard ground units for operation."
</code></pre>

<h3>Navy Class</h3>
<pre><code>class Navy(ArmedForce):
    def __init__(self, name, personnel, ships):
        super().__init__(name, personnel)
        self.ships = ships 

    def primary_function(self):
        return "The Navy's primary function is maritime defense and naval operations."

    def training(self):
        return "The Navy training includes seamanship, underwater combat, and navigation."

    def deploy_ships(self, ships=None):
        if ships:
            return f"Deploying {ships} ships for operation."
        return f"Deploying {self.ships} standard ships for maritime operation."
</code></pre>

<h3>AirForce Class</h3>
<pre><code>class AirForce(ArmedForce):
    def __init__(self, name, personnel, aircraft):
        super().__init__(name, personnel)
        self.aircraft = aircraft  

    def primary_function(self):
        return "The Air Force's primary function is aerial defense and air operations."

    def training(self):
        return "The Air Force training includes flight simulation, aerial combat, and precision bombing."

    def deploy_aircraft(self, aircraft=None):
        if aircraft:
            return f"Deploying {aircraft} aircraft for air operation."
        return f"Deploying {self.aircraft} standard aircraft for air operation."
</code></pre>

<h2 id="concepts">OOP Concepts Explained</h2>
<p>This project exemplifies key OOP principles:</p>
<ul>
    <li><strong>Abstraction:</strong> The use of an abstract class (<code>ArmedForce</code>) hides implementation details while exposing a common interface for derived classes.</li>
    <li><strong>Encapsulation:</strong> Internal object states are kept private, ensuring that they can only be modified through defined methods, thus maintaining control over data.</li>
    <li><strong>Inheritance:</strong> Allows for extending the base functionality provided by the <code>ArmedForce</code> class, enabling specific characteristics for each branch.</li>
    <li><strong>Polymorphism:</strong> Enables methods to be implemented in different ways based on the class that is calling them, allowing for flexibility in code execution.</li>
</ul>

<h2 id="contributing">Contributing</h2>
<p>Contributions are welcome! If you would like to contribute to this project:</p>
<ol>
    <li>Fork the repository.</li>
    <li>Create a new branch for your feature or bug fix.</li>
    <li>Submit a pull request for review.</li>
</ol>

<h2 id="license">License</h2>
<p>This project is licensed under the MIT License. See the <code>LICENSE</code> file for more details.</p>

</body>
</html>
