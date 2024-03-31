class Scooters:
    def __init__(self,location,battery_lvl,uq_identifier,per_km_fare=10,to_travel=0):
        self.location=location
        self.battery_level=battery_lvl
        self.__unique_identifier=uq_identifier
        self.per_km_fare=per_km_fare
        self.distance=to_travel
        def change_Unique_ID(self,new):
            self._Scooters__unique_identifier=new
    def change_location(self,current):
        self.current_location=current
    def start(self):
        print(f"scooter initiated from {self.location}")
    def stop(self):
        print(f"journey ended at {self.current_location}")
        self.last_location=self.current_location
    def calculate_fare(self):
        return f"{self.distance*self.per_km_fare} taka"
    def __str__(self):
        return f"from {self.location} to self.{self.last_location} fare is {self.calculate_fare()}"
    
class User:
    def __init__(self,id,name):
        self.__id=id
        self.name=name
    def search_for_ride(self,location,battery_lvl,uq_identifier,per_km_fare,to_travel):
        return Scooters(location,battery_lvl,uq_identifier,per_km_fare,to_travel)
    def change_id(self,new):
        self._User__id=new
class Ride(User):
    def __init__(self,id,name,destination):
        super.__init__(id,name)
        self.scooter=super.search_for_ride()
        self.fare=self.scooter.calculate_fare()
        self.destination=destination
    def thanking_user(self):
        if self.destination==self.scooter.last_location:
            return f"Thank you using Ecogo, {self.name},your fare is {self.fare}"
user1=User(1001,"abul")
user1.search_for_ride("savar",19,1001,10,100)

    
        
