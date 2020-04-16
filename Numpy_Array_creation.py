#In this Article i gone Elaborate, How to create 1,2,3D Array Manually in Numpy And HOW we Create 1,2,3D Random Number Numpy Array.

import Numpy as np

#creation of 1,2,3D Arrays Manually

#1D Array
#Example 
a = np.array([1,2,3])
#output
array([1,2,3])


#2D Array(it is list of lists)
a = np.array([[1,2,3],[4,5,6]])
#output
array([[1, 2, 3],
       [4, 5, 6]])


#3D Array(it is list of lists)
#Example
a =np.array([[[ 0,  1,  2,  3],
			[ 4,  5,  6,  7],
			[ 8,  9, 10, 11]],
		
			[[12, 13, 14, 15],
			[16, 17, 18, 19],
			[20, 21, 22, 23]]])

#output
array([[[ 0,  1,  2,  3],
        [ 4,  5,  6,  7],
        [ 8,  9, 10, 11]],

       [[12, 13, 14, 15],
        [16, 17, 18, 19],
        [20, 21, 22, 23]]])





#Let's start how to create random Numpy Array (Three ways to get random Array in numpy)

#first way Using numpy.random.rand()
#(By this we can create Random number Array and all the numbers in between 0,1)
#Syntex
#numpy.random.rand(Number_of_element)

#1D
#Example
a=np.random.rand(10)
#0utput
array([0.75949924, 0.74095427, 0.34015197, 0.56072509, 0.89868613,
       0.69668163, 0.39279344, 0.9526768 , 0.70190667, 0.7174709 ])

#2D
#Syntex()
#array.reshape(Number_of_Rows,Number_of_colunms)
#Example
a=np.random.rand(10).reshape(5,2)
#output
array([[0.68913462, 0.83423355],
       [0.10921744, 0.1763927 ],
       [0.61704659, 0.78346715],
       [0.32894712, 0.15371008],
       [0.91811983, 0.26804518]])



#3D
#Syntex()
#array.reshape(Number_of_Shells,Number_of_Rows,Number_of_colunms)
#Example
a=np.random.rand(10).reshape(2,5,1)
#output
array([[[0.37309086],
        [0.60845936],
        [0.08477469],
        [0.24664619],
        [0.5952841 ]],

       [[0.69214336],
        [0.01647356],
        [0.44701429],
        [0.00341365],
        [0.85179774]]])

#---------------------------------------------------------------------------------------End oF random.rand()


#Second way Using numpy.random.randn()
#this creation of random number is related to Gaussian(Normal Distribution)
#Syntex
#numpy.random.randn(Number_of_element)

#1D
a = np.random.randn(10)
#0utput
array([-0.9556195 , -0.14664267,  0.64162251, -1.93828885, -0.74021555,
       -1.12030846,  0.3758513 , -1.23587265,  0.56822024,  0.63788132])



# For 2D and 3D creation See the Above Methods mention in First_way(Random.rand)

#---------------------------------------------------------------------------------------End oF random.randn()

#third way Using numpy.random.randint()
#this is use to create Array of Random numnber the Random number is in between Low and high number
#syntex
#numpy.random.randint(Low_numer,high_number,Number_of_elements)

#1D
a = np.random.randint(2,4,10)
#0utput
array([2, 2, 1, 3, 2, 1, 1, 3, 2, 2])

#Here One Thin Important when we Create a random Array using Ranint it never includes High number in the array but lower Can be included


# For 2D and 3D creation See the Above Methods mention in First_way(Random.rand)


#---------------------------------------------------------------------------------------End oF random.randint()

#Thank You.......Regards ALI AHMAD

