from abc import ABC, abstractmethod

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
            return f"Deploying standard units."
        elif len(args) == 1:
            return f"Deploying {args[0]} units."
        else:
            return f"Deploying {args[0]} units from {args[1]}."

class Army(ArmedForce):
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

class Navy(ArmedForce):
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

class AirForce(ArmedForce):
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

def display_force_details(armed_force):
    print(f"{armed_force.get_name()}:")
    print(armed_force.primary_function())
    print(f"Training: {armed_force.training()}\n")

def main():
    army = Army("Indian Army", 1200000, 500)
    navy = Navy("Indian Navy", 65000, 150)
    air_force = AirForce("Indian Air Force", 140000, 800)

    display_force_details(army)
    display_force_details(navy)
    display_force_details(air_force)

    print(army.deploy())  
    print(army.deploy(300)) 
    print(army.deploy(300, "border region"))  
    print(f"\nOriginal name of Army: {army.get_name()}")
    army.set_name("Bharatiya Thal Sena")
    print(f"Updated name of Army: {army.get_name()}\n")

    print(army.deploy_ground_units())
    print(navy.deploy_ships())
    print(air_force.deploy_aircraft())

    print(army.deploy_ground_units(250))  
    print(navy.deploy_ships(100))  
    print(air_force.deploy_aircraft(400))  


if __name__ == "__main__":
    main()
