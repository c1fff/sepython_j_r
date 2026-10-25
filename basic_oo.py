### Assignment basic_oo ###

# s123456_s56789, YourLastname1_YourLastname2       ##TODO

####### IMPORTANT #######

# Make sure your document doesn't contain any syntax error and contains all procedures

#########################


#Task 1: map/filter/sum/...

#1a:
#Given a list of numbers lst that represent temperature values in fahrenheit. Write a procedure toCelsius that converts this list into Celsius scale. Note: the celsius-list shall be returned (not printed).
#Important: use the procedure 'map' 
#Example: [-40, 32, 50] --> [-40.0, 0.0, 10.0]

#C = (F - 32) / 1.8
def toCelsiusMap(lst):
  res = list(map(lambda i: (i - 32) / 1.8, lst))
  return res

#toCelsiusMap([-40, 32, 50])


#1b:
#Implement the conversion to celsius by using list comprehension (instead of map).

def toCelsiusLC(lst):
  res = [(i - 32) / 1.8 for i in lst]
  return res


#1c: 
#Implement a procedure mathFunc() that returns the result of the formula given in image basic_oo_formula.png. 
#The "%" sign represents the "modulo"-operator (.... Rest bei einer Division) and "==" simply means "equals".
#The upper and the lower bound shall be provided as arguments.
#Note there exists a procedure that sums all values in a list
#Important: use the procedures 'map' and 'filter'

def mathFuncMapFilter(lowerBound, upperBound):
  result = sum(map(lambda i: i**3, filter(lambda i: i % 2 == 0, range(lowerBound, upperBound + 1))))
  return result
    
#1d:
#Implement the formula (1c) by using list comprehension (it should be one line!)

def mathFuncLC(lowerBound, upperBound):
  return sum(i**3 for i in range(lowerBound, upperBound + 1) if i % 2 == 0)

##########################################################################

#Task 2
# Create a class "Person" that has three attributes (instance variables): "name", "comment" and "id".
# The class shall have a constructor such that a Person-object can be created with "p = Person("aName", 4)", where "aName" is the name of the person and 4 is its id.
# Furthermore, invoking the statement print(p) should lead to the following output "aName (id = 4)".
# Finally, a person shall be renamable by invoking p.rename("newName")
class Person:
    def __init__(self, name: str, id:int, comment = None):
      self.name = name
      self.comment = comment
      self.id = id

    def rename(self, newName):
      self.name = newName

    def __repr__(self):
      return f"{self.name} (id={self.id})"
    

#Example. This code:
#p = Person("aName", 4)
#p.rename("aNewName")
#print(p)
#shall lead to the following output:   aNewName (id=4)


##########################################################################


#Task 3
# Implement a procedure "toObjectList" that takes a list of names (strings) and returns a list of Person objects, 
# where the "name"-attribute of each person matches the given name, and the "id"-attribute of a person shall be the index in the name list.

def toObjectList(names):
    res = []
    for i in range(len(names)):
      res.append(Person(names[i], i))
    return res

#Example: the following code
oL = toObjectList(['Thomas', 'Michael', 'Thomas'])
for p in oL:
  print(p)

#shall output:
#Thomas (id=0)
#Michael (id=1)
#Thomas (id=2)


##########################################################################


#Task 4
#Implement a procedure "getDuplicatesAlphabetical" that take a list of person objects and returns a tuple containing all the names that appear multiple times
#at this, the names in the tuple shall be sorted alphabetically

def getDuplicatesAlphabetical(listOfPersonObjects):
  names = [p.name for p in listOfPersonObjects]
  duplicates = set([name for name in names if names.count(name) > 1])
  return tuple(sorted(duplicates))

#Example
getDuplicatesAlphabetical(toObjectList(['Thomas', 'Michael', 'Thomas','Susanne','Michael','Thomas','Alfred','Alfred']))
#shall output: ('Alfred', 'Michael', 'Thomas')



##########################################################################

#Task 5: Implement a class that represents 2D-points (i.e., a point that has an x- and a y- position).
#Implement the following methods:
#  distanceFromOrigin(): calculates and returns the distance to Point2D(0,0). Hint: pythagorean theorem
#  halfway(target): returns an instance of Point2D that represents the point in the middle of this point (self) and another Point2D (target)  
#  getX(): returns the x-position
#  getY(): returns the y-position
#  __repr__: find out what __repr__ usually is used for and implement it accordingly, such that your output meets the output provided below

class Point2D:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def distanceFromOrigin(self):
    distance = (self.x**2 + self.y**2) ** 0.5
    return distance

  def halfway(self, target):
    middle_x = (self.x + target.x) / 2
    middle_y = (self.y + target.y) / 2
    return Point2D(middle_x, middle_y)

  def getX(self):
    return self.x

  def getY(self):
    return self.y

  def __repr__(self):
    return f"({self.x}, {self.y})"

#this code
'''
p = Point2D(3,4)
print(p.distanceFromOrigin())
print(p.halfway(Point2D(0,0)))
print(p.getX() * 100)
print([Point2D(1,1), Point2D(2,2), Point2D(3,3)])
'''
#shall produce the following output
'''
5.0
(1.5, 2.0)
300.0
[(1, 1), (2, 2), (3, 3)]
'''

