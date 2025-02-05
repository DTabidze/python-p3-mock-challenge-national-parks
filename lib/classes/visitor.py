import ipdb

class Visitor:
    def __init__(self, name):        
        self.name = name
        self._trips = []
        self._national_parks = []
        
    def __repr__(self):
        return f"name: {self.name}"
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 15 and not hasattr(self, 'name'):
            self._name = value
        else:
            raise Exception("Name must be a string between 1 and 15 characters or name already exists")
        
    def trips(self, new_trip=None):
        from classes.trip import Trip
        if new_trip and isinstance(new_trip, Trip):
            self._trips.append(new_trip)
        
        return self._trips
    
    def national_parks(self, new_national_park=None):
        from classes.national_park import NationalPark
        if new_national_park and isinstance(new_national_park, NationalPark) and new_national_park not in self._national_parks:
            self._national_parks.append(new_national_park)
            
        return self._national_parks

# ipdb.set_trace()
