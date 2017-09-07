# Problem Set 11: Simulating robots
# Name: BOHDAN DRAHAN

import math
import random
import ps11_visualize
import numpy as np
from matplotlib import pyplot as plt

# === Provided classes

class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).

        x: a real number indicating the x-coordinate
        y: a real number indicating the y-coordinate
        """
        self.x = x
        self.y = y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: integer representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)


# === Problems 1 and 2

class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.
        Initially, no tiles in the room have been cleaned.
        self.tiles is a dictionary with coordinates as keys and status of "Clean"/"Dirty" as a values

        width: an integer > 0
        height: an integer > 0
        """
        # TODO: Your code goes here
        if width <= 0 or height <= 0:
            print "Check the size of the room"

        tile_list = list()
        tile_dict = dict()
        for x in range(0, width):
            for y in range(0,height):
                tile_list.append((x,y))
        for x_y in tile_list:
            tile_dict[x_y] = "Dirty"

        self.tile_list = tile_list
        self.tiles = tile_dict
        self.width = width
        self.height = height

    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.
        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """
        # TODO: Your code goes here
        self.tiles[(int(pos.getX()),int(pos.getY()))] = "Clean"

    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        # TODO: Your code goes here
        if self.tiles[(m,n)] == "Clean":
            return True
        elif self.tiles[(m,n)] == "Dirty":
            return False
        else: print "Error with Room.isTitleCleaned"
        
       
    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """
        # TODO: Your code goes here
        return int(self.width * self.height)

    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        # TODO: Your code goes here
        n = 0
        for key in self.tiles:
            if self.tiles[key] == "Clean":
                n += 1
        return n
    def getCoverage(self):
        """ Return the coverage of the room
        Float 0 <= x <= 1
        0 == 0% is "Clean"
        1 == 100% is "Clean"
        """
        return float(self.getNumCleanedTiles())/ self.getNumTiles()

    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """
        # TODO: Your code goes here
        return Position(random.uniform(0,self.width), random.uniform(0,self.height))

    def isPositionInRoom(self, pos):
        """
        Return True if POS is inside the room.

        pos: a Position object.
        returns: True if POS is in the room, False otherwise.
        """
        # TODO: Your code goes here
        if pos.getX() >=0 and pos.getX() < self.width and pos.getY() >=0 and pos.getY() < self.height:
            return True
        else: return False



##TEST

#pos1 = Position(2.1,2.2)
#pos2= Position(5,5)
#room1 = RectangularRoom(3,4) 
#print room1.isTileCleaned(2,2)
#print room1.getNumCleanedTiles()
#room1.cleanTileAtPosition(pos1)
#print room1.isTileCleaned(2,2)
#print room1.getNumCleanedTiles(), " <== '1' is expected"
#print room1.getRandomPosition().getX(), " <== random <3 expected" 
#print room1.isPositionInRoom(pos2), " <== False expected"
#print room1.isPositionInRoom(pos1), " <== True expected"
#print room1.getCoverage(), "<== Coverage"

class BaseRobot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in
    the room.  The robot also has a fixed speed.

    Subclasses of BaseRobot should provide movement strategies by
    implementing updatePositionAndClean(), which simulates a single
    time-step.
    """
    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified
        room. The robot initially has a random direction d and a
        random position p in the room.

        The direction d is an integer satisfying 0 <= d < 360; it
        specifies an angle in degrees.

        p is a Position object giving the robot's position.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """

        # TODO: Your code goes here
        self.d = random.randint(0,360)
        self.p = room.getRandomPosition()
        self.room = room
        self.speed = float(speed)
        self.room.cleanTileAtPosition(self.p)

        
    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        # TODO: Your code goes here
        return self.p

    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        # TODO: Your code goes here
        return self.d
    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """
        # TODO: Your code goes here
        self.p = position

    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """
        # TODO: Your code goes here
        self.d = direction

    def setNewRandomDirection(self):
        """
        Set the new random direction of the robot.
        """
        self.d = random.randint(0,360)


    def isHit(self):
        """return True if next step leads to hit to the wall
        return False otherwise
        """
        if self.room.isPositionInRoom(self.p.getNewPosition(self.d,self.speed)):
            return False
        else: return True
                



class Robot(BaseRobot):
    """
    A Robot is a BaseRobot with the standard movement strategy.

    At each time-step, a Robot attempts to move in its current
    direction; when it hits a wall, it chooses a new direction
    randomly.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        # TODO: Your code goes here
        while self.isHit():
            self.setNewRandomDirection()
        self.p = self.p.getNewPosition(self.d,self.speed)
        self.room.cleanTileAtPosition(self.p)
        
##TEST
#room1 = RectangularRoom(3,4)
#Rob = Robot(room1,1)
#Rob2 = Robot(room1,1)
#print Rob.room.tiles
#print Rob.p.getX()
#print Rob.p.getY()
#for x in range(10):
#    Rob.updatePositionAndClean()

# === Problem 3

def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type, visualize):
    """
    Runs NUM_TRIALS trials of the simulation and returns a list of
    lists, one per trial. The list for a trial has an element for each
    timestep of that trial, the value of which is the percentage of
    the room that is clean after that timestep. Each trial stops when
    MIN_COVERAGE of the room is clean.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE,
    each with speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    Visualization is turned on when boolean VISUALIZE is set to True.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. Robot or
                RandomWalkRobot)
    visualize: a boolean (True to turn on visualization)
    """
    # TODO: Your code goes here

    result = list()
    for trial in range(num_trials):
        if visualize: anim = ps11_visualize.RobotVisualization(num_robots, width, height)
        room = RectangularRoom(width,height)
        coverage = list()
        list_of_robots = list()
        for each in range(num_robots):
            list_of_robots.append(robot_type(room,speed))
        while room.getCoverage() < min_coverage:
            if visualize: anim.update(room,list_of_robots)
            coverage.append(room.getCoverage())
            for each in list_of_robots:
                each.updatePositionAndClean()
        result.append(coverage)
        if visualize: anim.done()
    return result



#TEST
        
#runSimulation(3,1.0,20,20,0.9,3,Robot,True) 


# === Provided function
def computeMeans(list_of_lists):
    """
    Returns a list as long as the longest list in LIST_OF_LISTS, where
    the value at index i is the average of the values at index i in
    all of LIST_OF_LISTS' lists.

    Lists shorter than the longest list are padded with their final
    value to be the same length.
    """
    # Find length of longest list
    longest = 0
    for lst in list_of_lists:
        if len(lst) > longest:
           longest = len(lst)
    # Get totals
    tots = [0]*(longest)
    for lst in list_of_lists:
        for i in range(longest):
            if i < len(lst):
                tots[i] += lst[i]
            else:
                tots[i] += lst[-1]
    # Convert tots to an array to make averaging across each index easier
    tots = pylab.array(tots)
    # Compute means
    means = tots/float(len(list_of_lists))
    return means

def avrgList(list_of_lists):
    """ Retun an avarage lenght of all the lists in the list of list #my school grammar teacher would kill me for this sentance. 
    """
    tot_len = 0 
    for each in list_of_lists:
        tot_len += len(each)
    avrg = tot_len/float(len(list_of_lists))
    return avrg

#TEST

#sim1 = runSimulation(3,1.0,5,5,0.9,2,Robot,True) 
#print avrgList(sim1)

# === Problem 4
def showPlot1():
    """
    Produces a plot showing dependence of cleaning time on room size.
    """
    # TODO: Your code goes here
    avrg_list = list()
    room_area = list()
    for i in range(5):
        room_sizes = (i+1) * 5
        room_area.append(room_sizes**2)
        sim = runSimulation(1,1,room_sizes,room_sizes, 0.75, 10, Robot, False)
        avrg_list.append(avrgList(sim))

    #plt.style.use('fivethirtyeight')
    plt.plot(room_area,avrg_list,
             room_area,avrg_list,"or")
    plt.title('Dependence of cleaning time on room size')
    plt.xlabel('area')
    plt.ylabel('time')
    plt.grid(True)

    plt.show()

#TEST
#showPlot1()



def showPlot2():
    """
    Produces a plot showing dependence of cleaning time on number of robots.
    """
    # TODO: Your code goes here
    avrg_list = list()
    num_robot_list = list()
    for i in range(9):
        num_robot = i + 1
        num_robot_list.append(num_robot)
        sim = runSimulation(num_robot,1,25,25,0.75,10,Robot,False)
        avrg_list.append(avrgList(sim))

    plt.plot(num_robot_list, avrg_list,
             num_robot_list, avrg_list,("or"))
    plt.title("Dependence of cleaning time on number of robots")
    plt.xlabel('qty of robots')
    plt.ylabel('time')
    plt.grid(True)
    plt.show()

#TEST
#showPlot2()
        
        

def showPlot3():
    """
    Produces a plot showing dependence of cleaning time on room shape.
    """
    # TODO: Your code goes here
    room_dimensions = ((20,20),(25,16),(40,10),(50,8),(80,5),(100,4))
    avrg_list = list()
    proportions = list()
    for each in room_dimensions:
        width = each[0]
        height = each[1]
        proportions.append(width/float(height))
        sim = runSimulation(2, 1, width, height, 0.75,50, Robot, False)
        avrg_list.append(avrgList(sim))
    plt.plot(proportions, avrg_list,)
    plt.plot(proportions, avrg_list,("or"))
    plt.title('Dependence of cleaning time on room shape')
    plt.xlabel('propotions of sides of the room')
    plt.ylabel('time')
    plt.grid(True)
    plt.show()

#TEST
#showPlot3()
    

def showPlot4():
    """
    Produces a plot showing cleaning time vs. percentage cleaned, for
    each of 1-5 robots.
    """
    # TODO: Your code goes here

    avrg_list_of_lists = list()
    min_coverage_list_of_lists = list()
    for i in range(5):
        num_rob = i + 1
        avrg_list = list()
        min_coverage_list = list()
        for min_coverage in np.linspace(0,1,11):
            min_coverage_list.append(min_coverage)
            sim = runSimulation(num_rob,1,25,25,min_coverage,3,Robot,False)
            avrg_list.append(avrgList(sim))
        avrg_list_of_lists.append(avrg_list)
        min_coverage_list_of_lists.append(min_coverage_list)

    for each in range(len(avrg_list_of_lists)):
        plt.plot(min_coverage_list_of_lists[each],avrg_list_of_lists[each], label = ('Qty of robots:' + str(each + 1)))
    #plt.plot(min_coverage_list_of_lists[1],avrg_list_of_lists[1],("or"))
    plt.title('Cleaning time vs. prcantage cleaned for each of 1-5 robots')
    plt.xlabel('Min coverage')
    plt.ylabel('Time')
    legend = plt.legend(loc = 'upper center')
    plt.grid(True)
    plt.show()

#TEST
showPlot4()

# === Problem 5

class RandomWalkRobot(BaseRobot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement
    strategy: it chooses a new direction at random after each
    time-step.
    """
    # TODO: Your code goes here
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        # TODO: Your code goes here
        self.setNewRandomDirection()
        while self.isHit():
            self.setNewRandomDirection()
        self.p = self.p.getNewPosition(self.d,self.speed)
        self.room.cleanTileAtPosition(self.p)

#TEST
#runSimulation(1,1,3,4,1,1,RandomWalkRobot,True)


# === Problem 6

def showPlot5():
    """
    Produces a plot comparing the two robot strategies.
    """
    # TODO: Your code goes here

    avrg_list = list()
    avrg_list1 = list()
    room_area = list()
    for i in range(5):
        room_sizes = (i+1) * 5
        room_area.append(room_sizes**2)
        sim = runSimulation(1,1,room_sizes,room_sizes, 0.75, 10, Robot, False)
        sim1 = runSimulation(1,1,room_sizes,room_sizes,0.75,10,RandomWalkRobot,False)
        avrg_list.append(avrgList(sim))
        avrg_list1.append(avrgList(sim1))

    #plt.style.use('fivethirtyeight')
    plt.plot(room_area,avrg_list, label = 'Robot')
    plt.plot(room_area,avrg_list,"or")
    plt.plot(room_area,avrg_list1, label = 'RandomWalkRobot')
    plt.plot(room_area,avrg_list1,"or")
    plt.title('Dependence of cleaning time on room size')
    plt.xlabel('area')
    plt.ylabel('time')
    legend = plt.legend(loc = 'upper center')
    
    plt.grid(True)

    plt.show()

#TEST
showPlot5()
