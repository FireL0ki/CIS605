# Project: In class demo - Demo2
# Description: Demonstrate if, elif, match statements
# Date: September 2025

class Car4:
    # initializer is a method used to initalize attributes of a newly created object
    def __init__(self, make, model, volume, type):
        # pass - a temporary placeholder before implementing the method
        self.__car_make = make
        self.__car_model = model
        self.__car_volume = volume
        self.__car_type = type

        # calling the instance method on itself, needs to be self.__set_car_size()
        # these first two are different versions of working with if statements
        # self.__car_size = self.__set_car_size()
        # self.__car_size = self.__find_car_size()

        # another version -- if and
        self.__car_size = self.__determine_car_size()
        # this version uses match / case
        self.__car_size = self.__identify_car_size()



    # region getters & setters
    # define getters & setters for the attributes
    @property
    def car_make(self):
        return self.__car_make
    
    @car_make.setter
    def car_make(self, value):
        self.__car_make = value

    @property
    def car_model(self):
        return self.__car_model
    
    @car_model.setter
    def car_model(self, value):
        car_model = value

    @property
    def car_volume(self):
        return self.__car_volume
    
    @property
    def car_type(self):
        return self.__car_type
    
    @property
    def car_size(self):
        return self.__car_size

    # endregion

    # region instance methods - methods that target the object

    # Class	Interior combined passenger and cargo volume index for Sedans
    # Minicompact	< 85 cubic feet (2,405 L)
    # Subcompact	85–99.9 cubic feet (2,405–2,830 L)
    # Compact	100–109.9 cubic feet (2,830–3,110 L)
    # Mid-size	110–119.9 cubic feet (3,115–3,395 L)
    # Large	≥ 120 cubic feet (3,400 L)
    
    # Class	Interior volume index for Station Wagons
    # Small	< 130 cubic feet (3,680 L)
    # Midsize	130–159 cubic feet (3,680–4,500 L)
    # Large	≥ 160 cubic feet (4,530 L)

    def __set_car_size(self):
        
        # define car size constants
        # MINI_COMPACT_VOLUME = 85

        # initialize size variable to be set in the if else statements based on the car_volume variable
        size = ""
        # check if car volume is greater than 85
        if self.car_volume < 85:
            # set size variable to minicompact
            size = "Minicompact"
        # do not need to say > 85, as that condition has already been checked by the first state
        elif self.car_volume < 100:
            size = "Subcompact"
        elif self.car_volume < 110:
            size = "Compact"
        elif self.car_volume < 120:
            size = "Mid-size"
        # else for the final condition, as all other vehicles will fall into this category - can use elif > 120 if you wish
        else:
            size = "Large"
        
        return size
    
    # nested if statements
    def __find_car_size(self):
        # can use nested if - check the type of car first, then within that, check the volumes of that car type
        size = ""
        # find the car type
        if self.car_type == "Sedan":
            if self.car_volume < 85:
                size = "Minicompact"
            elif self.car_volume < 100:
                size = "Subcompact"
            elif self.car_volume < 110:
                size = "Compact"
            elif self.car_volume < 120:
                size = "Mid-size"
            else:
                size = "Large"

        elif self.car_type == "Station Wagon":
            if self.car_volume < 130:
                size = "Small"   
            elif self.car_volume < 160:
                size = "Midsize"            
            else:
                size = "Large"

        return size

    # multiple conditions with logical operator
    def __determine_car_size(self):
        size = ""

        if self.car_type == "Sedan" and self.car_volume < 85:
            size = "Minicompact"
        elif self.car_type == "Sedan" and self.car_volume < 100:
            size = "Subcompact"
        elif self.car_type == "Sedan" and self.car_volume < 110:
             size = "Compact"
        elif self.car_type == "Sedan" and self.car_volume < 120:
            size = "Mid-size"
        elif self.car_type == "Sedan" and self.car_volume >= 120:
            size = "Large"
        
        elif self.car_type == "Station Wagon" and self.car_volume < 130:
            size = "Small"
        elif self.car_type == "Station Wagon" and self.car_volume < 160:
            size = "Mid-size"
        elif self.car_type == "Station Wagon" and self.car_volume >= 160:
            size = "Large"
        
        return size
    
    # use match for comparisons
    def __identify_car_size(self):
        size = ""

        # can check two conditions at once
        match(self.car_type, self.car_volume):
            case(x, y) if x == "Sedan" and y < 85:
                size = "Minicompact"
            case(x, y) if x == "Sedan" and y < 100:
                size = "Subcompact"
            case(x, y) if x == "Sedan" and y < 110:
                size = "Compact"
            case(x, y) if x == "Sedan" and y < 120:
                size = "Mid-size"
            case(x, y) if x == "Sedan" and y >= 120:
                size = "Large"

            case(x, y) if x == "Station Wagon" and y < 130:
                size = "Small"
            case(x, y) if x == "Station Wagon" and y < 160:
                size = "Mid-size"
            case(x, y) if x == "Station Wagon" and y >= 160:
                size = "Large"

        return size

    def __str__(self):
        return f'Make: {self.car_make}\nModel: {self.car_model}\nVolume: {self.car_volume:,}\nType: {self.car_type}\nSize: {self.car_size}'

    # endregion
