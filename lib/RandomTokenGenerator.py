'''
Created on 23-Feb-2015

@author: asawari.vaidya
'''

import random
import string


class RandomTokenGenerator(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        
    def generateId(self):
        token = ''.join(random.choice(string.ascii_lowercase + string.digits) for x in range(4)) +"-"+ ''.join(random.choice(string.ascii_lowercase + string.digits) for x in range(4)) # @UnusedVariable
        return (token.upper())
    

    def generateToken(self):
        token = ''.join(random.choice(string.ascii_lowercase + string.digits) for x in range(10)) # @UnusedVariable
        return (token)

    def generateNumber(self):
        number = random.randint(1,9999999999) 
        return (number)

    def generateUID(self):
        num1 = random.randint(1111111111,9999999999)
        num2 = random.randint(1111111111,9999999999)
        # print(num1 , str(num1)[-3:])
        num1_str = str(num1)[:3]
        num2_str = str(num2)[-3:]
        # print("num2", num2_str)
        uid = (''.join(num1_str))+""+(''.join(num2_str))
        return (uid)

    def generateTransIds(self):
        num1 = random.randint(1111111111,9999999999)
        num2 = random.randint(1111111111,9999999999)
        num1_str = str(num1)[:4]
        num2_str = str(num2)[-4:]

        trans_id = "T-"+(''.join(num1_str))+"-"+''.join(random.choice(string.ascii_lowercase + string.digits) for x in range(4)) # @UnusedVariable
        return (trans_id.upper())

        # pass
    def generatePasswordPin(self):
        token = ''.join(random.choice(string.ascii_lowercase + string.digits) for x in range(6)) # @UnusedVariable
        return (token)