# 6.00 Problem Set 12
#
# Name:
# Collaborators:
# Time:

import numpy as np
import random
import pylab as plt
from matplotlib import style
class NoChildException(Exception):
    """
    NoChildException is raised by the reproduce() method in the SimpleVirus
    and ResistantVirus classes to indicate that a virus particle does not
    reproduce. You can use NoChildException as is, you do not need to
    modify/add any code.
    """    

#
# PROBLEM 1
#

class SimpleVirus(object):
    """
    Representation of a simple virus (does not model drug effects/resistance).
    """
    
    def __init__(self, maxBirthProb, clearProb):
        """
        Initialize a SimpleVirus instance, saves all parameters as attributes
        of the instance.        
        
        maxBirthProb: Maximum reproduction probability (a float between 0-1)        
        
        clearProb: Maximum clearance probability (a float between 0-1).
        """
        # TODO
        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb
        
    def doesClear(self):
        """
        Stochastically determines whether this virus is cleared from the
        patient's body at a time step. 

        returns: Using a random number generator (random.random()), this method
        returns True with probability self.clearProb and otherwise returns
        False.
        """
        # TODO
        if random.random() <= self.clearProb:
            return True
        else: return False
    
    def reproduce(self, popDensity):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the SimplePatient and
        Patient classes. The virus particle reproduces with probability
        self.maxBirthProb * (1 - popDensity).
        
        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring SimpleVirus (which has the same
        maxBirthProb and clearProb values as its parent).         

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population.         
        
        returns: a new instance of the SimpleVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.               
        """
        # TODO
        if random.random() <= self.maxBirthProb*(1 - popDensity):
            return SimpleVirus(self.maxBirthProb, self.clearProb)

        else: NoChildException() 

class SimplePatient(object):
    """
    Representation of a simplified patient. The patient does not take any drugs
    and his/her virus populations have no drug resistance.
    """
    
    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes.

        viruses: the list representing the virus population (a list of
        SimpleVirus instances)
        
        maxPop: the  maximum virus population for this patient (an integer)
        """
        # TODO
        self.viruses = list(viruses)
        self.maxPop = int(maxPop)

    def getMaxPop(self):
        """ Custom method
        retun max Pop
        """
        return self.maxPop

    def getTotalPop(self):
        """
        Gets the current total virus population. 

        returns: The total virus population (an integer)
        """
        # TODO        
        return len(self.viruses)

    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute the following steps in this order: 
        1- Determine whether each virus particle survives and updates the list
          of virus particles accordingly.

        2- The current population density is calculated. This population density
          value is used until the next call to update() 

        3- Determine whether each virus particle should reproduce and add
          offspring virus particles to the list of viruses in this patient.                    

        returns: the total virus population at the end of the update (an
        integer)
        """
        # TODO
        #1
        survived_viruses = list()
        for each in self.viruses:
            if not each.doesClear():
                survived_viruses.append(each)
        self.viruses = survived_viruses

        #2
        popDensity = self.getTotalPop() / float(self.maxPop)


        #3
        for each in self.viruses:
            child = each.reproduce(popDensity)
            if child != None:
                self.viruses.append(child)


        return len(self.viruses)

#TEST
#v1 = SimpleVirus(0.3, 0.1)
#v2 = SimpleVirus(0.1, 0.08)
#viruses = (v1, v2)
#p = SimplePatient(viruses, 1000)
#for x in range(100):
#    print p.update()

#
# PROBLEM 2
#

def problem2():
    """
    Run the simulation and plot the graph for problem 2 (no drugs are used,
    viruses do not have any drug resistance).    

    Instantiates a patient, runs a simulation for 300 timesteps, and plots the
    total virus population as a function of time.    
    """
    # TODO    
    viruses = list()
    for i in xrange(100):
        viruses.append(SimpleVirus(0.1, 0.05))

    sp = SimplePatient(viruses, 1000)
    x = list()
    y = list()
    maxPopList = list()
    for i in xrange(300):
        x.append(i)
        y.append(sp.getTotalPop())
        sp.update()
        maxPopList.append(sp.getMaxPop())

    #Plot
    style.use('ggplot')
    plt.plot(x, y, label = "Population")
    plt.plot(x, maxPopList, label = "Limit of population")
    plt.ylim([0, 1.1*sp.getMaxPop() ])
    plt.xlabel('Time')
    plt.ylabel('Population of Viruses')
    plt.legend(loc = 'lower right')
    plt.title('Population of viruses over time')
    plt.grid(True)
    plt.show()


    
        
#TEST
#problem2()
    
#
# PROBLEM 3
#

class ResistantVirus(SimpleVirus):
    """
    Representation of a virus which can have drug resistance.
    """    
    
    def __init__(self, maxBirthProb, clearProb, resistances, mutProb):
        """
        Initialize a ResistantVirus instance, saves all parameters as attributes
        of the instance.
        
        maxBirthProb: Maximum reproduction probability (a float between 0-1)        
        
        clearProb: Maximum clearance probability (a float between 0-1).
        
        resistances: A dictionary of drug names (strings) mapping to the state
        of this virus particle's resistance (either True or False) to each drug.
        e.g. {'guttagonol':False, 'grimpex',False}, means that this virus
        particle is resistant to neither guttagonol nor grimpex.

        mutProb: Mutation probability for this virus particle (a float). This is
        the probability of the offspring acquiring or losing resistance to a drug.        
        """
        # TODO
        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb
        self.resistances = resistances
        self.mutProb = mutProb
        
    def getResistance(self, drug):
        """
        Get the state of this virus particle's resistance to a drug. This method
        is called by getResistPop() in Patient to determine how many virus
        particles have resistance to a drug.        

        drug: the drug (a string).

        returns: True if this virus instance is resistant to the drug, False
        otherwise.
        """
        # TODO
        if self.resistances[drug]:
            return True
        else: return False

    def reproduce(self, popDensity, activeDrugs):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the Patient class.

        If the virus particle is not resistant to any drug in activeDrugs,
        then it does not reproduce. Otherwise, the virus particle reproduces
        with probability:       
        
        self.maxBirthProb * (1 - popDensity).                       
        
        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring ResistantVirus (which has the same
        maxBirthProb and clearProb values as its parent). 

        For each drug resistance trait of the virus (i.e. each key of
        self.resistances), the offspring has probability 1-mutProb of
        inheriting that resistance trait from the parent, and probability
        mutProb of switching that resistance trait in the offspring.        

        For example, if a virus particle is resistant to guttagonol but not
        grimpex, and `self.mutProb` is 0.1, then there is a 10% chance that
        that the offspring will lose resistance to guttagonol and a 90% 
        chance that the offspring will be resistant to guttagonol.
        There is also a 10% chance that the offspring will gain resistance to
        grimpex and a 90% chance that the offspring will not be resistant to
        grimpex.#

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population        

        activeDrugs: a list of the drug names acting on this virus particle
        (a list of strings). 
        
        returns: a new instance of the ResistantVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.         
        """
        # TODO

        if random.random() <= self.maxBirthProb*(1 - popDensity):
            sterile = False
            for drug in activeDrugs:
                if self.resistances[drug] == False:
                    sterile = True
            if not sterile:
                new_resistance = dict()
                for drug in self.resistances:
                    if random.random() <= self.mutProb:
                        new_resistance[drug] = not self.resistances[drug]
                    else: new_resistance[drug] = self.resistances[drug]
                return ResistantVirus(self.maxBirthProb, self.clearProb, new_resistance, self.mutProb)
        else: NoChildException() 
            
class Patient(SimplePatient):
    """
    Representation of a patient. The patient is able to take drugs and his/her
    virus population can acquire resistance to the drugs he/she takes.
    """
    
    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes. Also initializes the list of drugs being administered
        (which should initially include no drugs).               

        viruses: the list representing the virus population (a list of
        SimpleVirus instances)
        
        maxPop: the  maximum virus population for this patient (an integer)
        """
        # TODO
        self.prescription = list()
        self.viruses = list(viruses)
        self.maxPop = int(maxPop)
        
    def addPrescription(self, newDrug):
        """
        Administer a drug to this patient. After a prescription is added, the 
        drug acts on the virus population for all subsequent time steps. If the
        newDrug is already prescribed to this patient, the method has no effect.

        newDrug: The name of the drug to administer to the patient (a string).

        postcondition: list of drugs being administered to a patient is updated
        """
        # TODO
        if not newDrug in self.prescription:
            self.prescription.append(str(newDrug))

    def getPrescriptions(self):
        """
        Returns the drugs that are being administered to this patient.

        returns: The list of drug names (strings) being administered to this
        patient.
        """
        # TODO

        return self.prescription
        
    def getResistPop(self, drugResist):
        """
        Get the population of virus particles resistant to the drugs listed in 
        drugResist.        

        drugResist: Which drug resistances to include in the population (a list
        of strings - e.g. ['guttagonol'] or ['guttagonol', 'grimpex'])

        returns: the population of viruses (an integer) with resistances to all
        drugs in the drugResist list.
        """
        # TODO
        resistant_viruses = list(self.viruses)
        for drug in drugResist:
            nonresistant_viruses = list()
            for virus in resistant_viruses:
                if not virus.getResistance(drug):
                    nonresistant_viruses.append(virus)
            for each in nonresistant_viruses:
                resistant_viruses.remove(each)
        return len(resistant_viruses)
        
    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute these actions in order:

        1- Determine whether each virus particle survives and update the list of 
          virus particles accordingly
          
        2- The current population density is calculated. This population density
          value is used until the next call to update().

        3- Determine whether each virus particle should reproduce and add
          offspring virus particles to the list of viruses in this patient. 
          The listof drugs being administered should be accounted for in the
          determination of whether each virus particle reproduces. 

        returns: the total virus population at the end of the update (an
        integer)
        """
        # TODO
        #1
        survived_viruses = list()
        for each in self.viruses:
            if not each.doesClear():
                survived_viruses.append(each)
        self.viruses = survived_viruses

        #2
        popDensity = self.getTotalPop() / float(self.maxPop)


        #3
        for each in self.viruses:
            child = each.reproduce(popDensity, self.getPrescriptions())
            if child != None:
                self.viruses.append(child)


        return len(self.viruses)
#TEST
#viruses = list()
#for i in xrange(100):
#viruses.append(ResistantVirus(0.1, 0.05,{'guttagonol':False},0.005))
#
#p = Patient(viruses, 1000)
#print p.getResistPop(['guttagonol'])


#
# PROBLEM 4
#

def problem4():
    """
    Runs simulations and plots graphs for problem 4.

    Instantiates a patient, runs a simulation for 150 timesteps, adds
    guttagonol, and runs the simulation for an additional 150 timesteps.

    total virus population vs. time  and guttagonol-resistant virus population
    vs. time are plotted
    """
    # TODO
    #take a pill - Time when a patient take a drug
    take_a_pill = 150
    time_steps = 300

    viruses = list()
    for i in xrange(100):
        viruses.append(ResistantVirus(0.1, 0.05,{'guttagonol':False},0.005))

    p =Patient(viruses, 1000)
    x = list()
    y = list()
    y2 = list()
    maxPopList = list()
    for i in xrange(time_steps):
        if i == take_a_pill:
            p.addPrescription('guttagonol')
        x.append(i)
        y.append(p.getTotalPop())
        y2.append(p.getResistPop(['guttagonol']))
        p.update()
        maxPopList.append(p.getMaxPop())

    #Plot
    style.use('ggplot')
    plt.plot(x, y, label = "Population")
    plt.plot(x, y2, label = "Population, resistant to guttagonol")
    plt.plot(x, maxPopList, label = "Limit of population")
    plt.plot(take_a_pill, y[take_a_pill],"ob", label = "time when drug was added")
    plt.ylim([0, 1.1*p.getMaxPop() ])
    plt.xlabel('Time')
    plt.ylabel('Population of Viruses')
    plt.legend(loc = 'upper center')
    plt.title('Population of viruses over time')
    plt.grid(True)
    plt.show()


#TEST
#problem4()

#
# PROBLEM 5
#
        
def problem5():
    """
    Runs simulations and make histograms for problem 5.

    Runs multiple simulations to show the relationship between delayed treatment
    and patient outcome.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).    
    """
    # TODO
    take_a_pill = [300, 150, 75, 0]
    trials = 50 

    for each in take_a_pill:
        print "Loading histogram for delay of", each, "timesteps"
        time_steps = each + 150
        end_pop = list()
        for trial in xrange(trials):
            viruses = list()
            for i in xrange(100):
                viruses.append(ResistantVirus(0.1, 0.05,{'guttagonol':False},0.005))
            p =Patient(viruses, 1000)

            for i in xrange(time_steps):
                if i == each:
                    p.addPrescription('guttagonol')
                p.update()
                if i == time_steps - 1:
                    end_pop.append(p.update())


        #Plot
        ttl = "Histogram of final total virus population for delayed treatment of " + str(each) + " timesteps(followed by an additional 150 timesteps of simulation"
        style.use('ggplot')
        plt.hist(end_pop,bins = 10)
        plt.title(ttl)
        plt.xlabel("Final total virus population")
        plt.ylabel("Number of patients")
        plt.show()

#TEST
#problem5()

#
# PROBLEM 6
#


def problem6():
    """
    Runs simulations and make histograms for problem 6.

    Runs multiple simulations to show the relationship between administration
    of multiple drugs and patient outcome.
    
    Histograms of final total virus populations are displayed for lag times of
    150, 75, 0 timesteps between adding drugs (followed by an additional 150
    timesteps of simulation).
    """
    # TODO
    
    take_a_pill = 150 
    take_another_pill = [300, 150,75, 0]
    trials = 30 

    for each in take_another_pill:
        print "Loading histogram for delay of", each, "timesteps"
        time_steps = each + take_a_pill + 150 
        end_pop = list()
        x=list()
        y=list()
        for trial in xrange(trials):
            viruses = list()
            for i in xrange(100):
                viruses.append(ResistantVirus(0.1, 0.05,{'guttagonol':False, 'grimpex':False},0.005))
            p =Patient(viruses, 1000)

            for i in xrange(time_steps):
                if i == take_a_pill:
                    p.addPrescription('guttagonol')
                if i == each + take_a_pill:
                    p.addPrescription('grimpex')
                p.update()
                if trial == trials - 1:
                    x.append(i)
                    y.append(p.getTotalPop())
                if i == time_steps - 1:
                    end_pop.append(p.update())

        #Plot
        ttl = "Histogram of final total virus population for lag times \n of " + str(each) + " timesteps between adding drugs \n (followed by an additional 150 timesteps of simulation"
        style.use('ggplot')
        plt.hist(end_pop,bins = 10)
        plt.title(ttl)
        plt.xlabel("Final total virus population")
        plt.ylabel("Number of patients")

        plt.figure()
        plt.title("additional plot")
        plt.xlabel("timesteps")
        plt.ylabel("population")
        plt.plot(x,y)
        plt.show()

#TEST
#problem6()
    

#
# PROBLEM 7
#
     
def problem7():
    """
    Run simulations and plot graphs examining the relationship between
    administration of multiple drugs and patient outcome.

    Plots of total and drug-resistant viruses vs. time are made for a
    simulation with a 300 time step delay between administering the 2 drugs and
    a simulations for which drugs are administered simultaneously.        
    """
    # TODO
    take_a_pill = 150 
    take_another_pill = [300, 0]
    trials = 1

    for each in take_another_pill:
        print "Loading histogram for delay of", each, "timesteps"
        time_steps = each + take_a_pill + 150 
        end_pop = list()
        x=list()
        yTotal=list()
        yGrimRes = list()
        yGutRes =list()
        yBothRes = list()
        for trial in xrange(trials):
            viruses = list()
            for i in xrange(100):
                viruses.append(ResistantVirus(0.1, 0.05,{'guttagonol':False, 'grimpex':False},0.005))
            p =Patient(viruses, 1000)

            for i in xrange(time_steps):
                if i == take_a_pill:
                    p.addPrescription('guttagonol')
                if i == each + take_a_pill:
                    p.addPrescription('grimpex')
                p.update()
                x.append(i)
                yTotal.append(p.getTotalPop())
                yGrimRes.append(p.getResistPop(['grimpex']))
                yGutRes.append(p.getResistPop(['guttagonol']))
                yBothRes.append(p.getResistPop(['grimpex','guttagonol']))

                if i == time_steps - 1:
                    end_pop.append(p.update())

        #Plot
        style.use('ggplot')
        plt.title("Problem 7. Simulation")
        plt.xlabel("timesteps")
        plt.ylabel("population")
        plt.plot(x,yTotal,label = "Total population")
        plt.plot(x,yGrimRes,label = "grimpex-resistant population")
        plt.plot(x,yGutRes,label = "guttagonol-resistant population")
        plt.plot(x,yBothRes,label = "population resistant to both" )
        plt.legend(loc = 'upper left')
        plt.show()
#TEST
#problem7()
