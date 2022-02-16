class Car:
    def __init__(self, brand, mileage = 0):
        self.brand = brand
        self.mileage = mileage
        
    def get_brand(self):
        return self.brand
    
    def get_mileage(self):
        return self.mileage
    
    def update_mileage(self, km):
        self.mileage += km

if __name__ == "__main__":
    my_car = Car('BYD', 100)
    car_brand = my_car.get_brand()    
    print(car_brand)      # BYD
    distace_traveled = my_car.get_mileage()
    print(distace_traveled)       # 100
    my_car.update_mileage(200)   
    print(my_car.get_mileage())   # 300
