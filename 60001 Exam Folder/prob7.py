### Do not change the Location or Campus classes. ###
class Location(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self, deltaX, deltaY):
        return Location(self.x + deltaX, self.y + deltaY)
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def dist_from(self, other):
        xDist = self.x - other.x
        yDist = self.y - other.y
        return (xDist**2 + yDist**2)**0.5
    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y)
    def __str__(self):
        return '<' + str(self.x) + ',' + str(self.y) + '>'
        
class Campus(object):
    def __init__(self, center_loc):
        self.center_loc = center_loc
    def __str__(self):
        return str(self.center_loc)


## THIS ONE
class Campus(object):
    def __init__(self, center_loc):
        self.center_loc = center_loc
    def __str__(self):
        return str(self.center_loc)

class MITCampus(Campus):
    """ A MITCampus is a Campus that contains buildings """
    def __init__(self, center_loc, bldg_loc = Location(0,0)):
        """ Assumes center_loc and bldg_loc are Location objects 
        Initializes a new Campus centered at location center_loc 
        with a building at location bldg_loc """
        self.center_loc = center_loc
        self.buildings = [bldg_loc] # technically locations for buildings, but I prefer "buildings" because it's easier to write quick
      
    def add_bldg(self, new_bldg_loc):
        """ Assumes new_bldg_loc is a Location
        Adds new_bldg_loc to the campus only if the building is at least 0.5 distance 
        away from all other buildings already there. Campus is unchanged otherwise.
        Returns True if it could add the building, False otherwise. """
        try:
            for building in self.buildings:
                if new_bldg_loc.dist_from(building) < 0.5:
                    return False
            # else just add it
            self.buildings.append(new_bldg_loc)
            return True
        except:
            return False

    def remove_bldg(self, bldg_loc):
        """ Assumes bldg_loc is a Location
        Removes bldg_loc from the campus. 
        Raises a ValueError if there is not a building at bldg_loc.
        Does not return anything """
        if self.buildings.contains(bldg_loc):
            self.buildings.remove(bldg_loc)
            # return None (also because of the 0.5 rule there is only one occurence and we gucci here with remove)
            pass
        else:
            raise ValueError("Trying to remove a non-existent building")
      
    def get_bldgs(self):
        """ Returns a list of all buildings on the campus. The list should contain 
        the string representation of the Location of a building. The list should 
        be sorted by the x coordinate of the location. """
        # because factory sort REQUIRES me to RETURN AN INTEGER AND NOT A LOCATION
        # do a bubble sort because it's good enough for us right now
        if len(self.buildings) < 1:
            return ""

        sorted = False
        while (not sorted):
            sorted = True
            for i in range(0,len(self.buildings)-1):
                if self.buildings[i].getX() > self.buildings[i+1].getX():
                    sorted = False
                    self.buildings[i], self.buildings[i+1] = self.buildings[i+1], self.buildings[i]
                pass
            pass
        
        st = []
        for building in self.buildings:
            st.append(str(building))
        return st

c = MITCampus(Location(1,2))
print c.add_bldg(Location(2,3)) # should return True
print c.add_bldg(Location(1,2)) # should return  True
print c.add_bldg(Location(0,0)) # should return False
print c.add_bldg(Location(2,3)) # should return False
print c.get_bldgs() # should return ['<0,0>', '<1,2>', '<2,3>']