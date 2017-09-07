# 6.00 Problem Set 9
#
# Name: Bohdan Drahan
# Collaborators:
# Time: around 4 hours

from string import *

def isclose(a, b, rel_tol=1e-08, abs_tol=0.0):
    return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)


class Shape(object):
    def isShape(self):
        return True
    def area(self):
        raise AttributeException("Subclasses should override this method.")

class Square(Shape):
    def __init__(self, h):
        """
        h: length of side of the square
        """
        self.side = float(h)
    def area(self):
        """
        Returns area of the square
        """
        return self.side**2
    def __str__(self):
        return 'Square with side ' + str(self.side)
    def __eq__(self, other):
        """
        Two squares are equal if they have the same dimension.
        other: object to check for equality
        """
        return type(other) == Square and self.side == other.side

class Circle(Shape):
    def __init__(self, radius):
        """
        radius: radius of the circle
        """
        self.radius = float(radius)
    def area(self):
        """
        Returns approximate area of the circle
        """
        return 3.14159*(self.radius**2)
    def __str__(self):
        return 'Circle with radius ' + str(self.radius)
    def __eq__(self, other):
        """
        Two circles are equal if they have the same radius.
        other: object to check for equality
        """
        return type(other) == Circle and self.radius == other.radius

#
# Problem 1: Create the Triangle class
#
## TO DO: Implement the `Triangle` class, which also extends `Shape`.
class Triangle(Shape):
    def __init__ (self, base, height):
        """
        base -base
        height -height
        """
        self.base = float(base)
        self.height = float(height)
    def area(self):
        """area -area - NO WAY!"""
        return (self.base * self.height)/2
    def __str__(self):
        return 'Triangle with base {0:.2f} and height {1:.2f}'.format(self.base, self.height)
    def __eq__(self, other):
        """ Two triangles are equal when both base and height are equal""" 
        return type(other) == Triangle and self.base == other.base and self.height == other.height

##Test
#t = Triangle(1,2) 
#t2 = Triangle(1,2)
#t3 = Triangle(3,13)
#
#print "true, false expected"
#print t2 == t
#print t3 == t2
#print t
#print t.area(), t2.area(), t3.area()

#
# Problem 2: Create the ShapeSet class
#
## TO DO: Fill in the following code skeleton according to the
##    specifications.

class ShapeSet(set):
    """
    This is set of Shapes. It is unordered set 
    even though string representation of it is ordered by shaped
    """
    def __init__(self):
        """
        Initialize any needed variables
        """
        ## TO DO
        self = set() 

    def addShape(self, sh):
        """
        Add shape sh to the set; no two shapes in the set may be
        identical
        sh: shape to be added
        """
        ## TO DO
        try:
            if sh.isShape() == True:
                if sh in self:
                    print sh, " is already in a set."
                else: self.add(sh)
            else: print sh, " is not a shape"
        except: print sh, " is not a shape!"


## I don't really need to do this part of the code because 
#I mentioned in the line "class ShapeSet(set)" that ShapeSet is a 'set'
#which has bulit in methods __iter__ and next. If I needed,
#I would do the following:

#    def __iter__(self):
#        """
#        Return an iterator that allows you to iterate over the set of
#        shapes, one shape at a time
#        """
#        ## TO DO
#        self.i = 0
#        return self
#    def next(self):
#        if self.i >= len(self.shapes):
#            raise StopIteration
#        self.i += 1
#        return self[self.i -  1]




    def __str__(self):
        """
        Return the string representation for a set, which consists of
        the string representation of each shape, categorized by type
        (circles, then squares, then triangles) - cross that!!! 

        UPDATED!!!
        It is categorized by type, but order could be random
        (This is set, remember? It's unordered).
        I did it because I made possibility to add aditional kind of
        shapes in a future(for example 'Star' or 'Elips'), 
        and NO ADDITIONAL CHANGES NEEDED! Pure modularity, isn't it?

        """

        ## TO DO
        string = 'ShapeSet:\n'
        types_dict = dict()
        count = 0 #count - how many different types of shapes found in this set
        
        s = dict()


        for each in self:
            if not type(each) in types_dict:
                types_dict[type(each)] = count 
                count += 1
                s[types_dict[type(each)]] = ''
            
            #Creates a string for each type of shapes 
            s[types_dict[type(each)]] += str(each) +'\n'

        #Connect strings from different types together
        for i in range(0, len(s)):
            string += s[i]
        return string
        
#TEST
string1 = 'this_is_not_a_shape'
integer1 = 123213
sq1 = Square(123)
sq2 = Square(140.504448328)
c1 = Circle(13)
t1 = Triangle(1,2) 
t2 = Triangle(1,2)
t3 = Triangle(3,13)
t4 = Triangle(321,123)
t5 = Triangle(321,123)
s1 = ShapeSet()

s1.addShape(string1)
s1.addShape(integer1)
s1.addShape(t1)
s1.addShape(t2)
s1.addShape(t3)
s1.addShape(t4)
s1.addShape(t5)
s1.addShape(c1)
s1.addShape(sq1)
s1.addShape(sq2)
print s1


#
# Problem 3: Find the largest shapes in a ShapeSet
#
def findLargest(shapes):
    """
    Prints out the messege with the largest elements.
    Returns a tuple containing the elements of ShapeSet with the
       largest area.
    shapes: ShapeSet
    """
    ## TO DO
    maxShapes = list()
    maxArea = 0
    for each in shapes:
        if each.area() > maxArea:
            maxShapes = list([each])
            maxArea = each.area()
        elif isclose(each.area(), maxArea):
            maxShapes.append(each)
    print "The largest element(s): "
    for i in maxShapes:
        print i
    print "The largest area: ", maxArea
    
    return maxShapes

#Test
findLargest(s1)



#
# Problem 4: Read shapes from a file into a ShapeSet
#
def readShapesFromFile(filename):
    """
    Retrieves shape information from the given file.
    Creates and returns a ShapeSet with the shapes found.
    filename: string
    """
    ## TO DO
    shapes = ShapeSet()
    inputFile = open(filename)
    for line in inputFile:
        line_listed = line.split(',')
        if line_listed[0] == 'circle':
            shapes.addShape(Circle(line_listed[1].strip('\n')))
        if line_listed[0] == 'square':
            shapes.addShape(Square(line_listed[1].strip('\n')))
        if line_listed[0] == 'triangle':
            shapes.addShape(Triangle(line_listed[1], line_listed[2].strip('\n')))
    return shapes

#Test
filename = 'shapes.txt'
shapes_from_file = readShapesFromFile(filename)
print shapes_from_file
findLargest(shapes_from_file)

            

