class Robot:
#class variable counting the number of robots
   population = 0

   def __init__(self, name):
       self.name = name
       print('(initializing {0})'.format(self.name))

       Robot.population += 1

   def __del__(self):
       print('{0} is being destroyed'.format(self.name))

       Robot.population -= 1

       if(Robot.population == 0):
           print('{0} was the last one'.format(self.name))
       else:
           print('there are still {0:d} robots working'.format(Robot.population))

   def sayhi(self):
       print('greeting my masters call me {0}'.format(self.name))

   def howMany(self):
       print('we have {0:d} robots'.format(Robot.population))

   howMany = staticmethod(howMany)

   @staticmethod
   def countNumber():
       print('we have {0:d} robots'.format(Robot.population))


droid1 = Robot('r2-d2')
droid2 = Robot('c-3p0')

Robot.howMany()

del droid1
del droid2


