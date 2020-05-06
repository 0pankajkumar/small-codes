'''
Question​ : Implement N > 0 stacks using a single array to store all stack data (you may
use auxiliary arrays in your stack object, but all of the objects in all of the stacks must
be in the same array). No stack should be full unless the entire array is full.
'''

# class StackBuilder():
# 	def __init__(self,arraySize):
# 		self.array = [None]*arraySize

from math import ceil
class StackBox():
	def __init__(self, start, end):
		self.start=start
		self.end=end-1

class Stack():
	# return a list of objects of stack type
	def __init__(self,arraySize, noOfStacks):
		self.array = [None]*arraySize
		self.listOfStacks=list()

		intervals = ceil(arraySize/noOfStacks)

		try:
			start=0
			for i in range(noOfStacks):
				t = StackBox(start,start)
				self.listOfStacks.append(t)
				start+=intervals

			print(f"{noOfStacks} stacks created")
		except:
			print("Stack creation failed :P")


	

	def makeSomeSpace(self, stackNumber, start, end):
		def lookLeft(stackNumber, start, end):
			# loook for space in the left direction
			los = self.listOfStacks
			arr = self.array

			start = los[stackNumber].start
			end = los[stackNumber].end

			if start-1 < 0:
				return False

			if arr[los[stackNumber].start - 1] is None:
				# shift this stack one step left
				for i in range(start-1,end):
					arr[i] = arr[i+1]
				arr[end] = None
				los[stackNumber].start -= 1
				loc[stackNumber].end -= 1
				return True
				# If their is no gap between the this & next array update start of next array as well
				# if los[stackNumber+1].start == end+1:
			



		def lookRight(stackNumber, start, end):
			# look for space in right direction
			los = self.listOfStacks
			arr = self.array

			start = los[stackNumber].start
			end = los[stackNumber].end

			if end+1 == len(self.array):
				return False

			print("1.start,end",start,end)
			
			if arr[los[stackNumber].end + 1] is not None:
				start = los[stackNumber + 1].start
				end = los[stackNumber + 1].end
				if not lookRight(stackNumber+1, start, end):
					return False
			
			print("2.start,end",start,end)

			# shift this stack one step right
			for i in range(end+1, start,-1):
				arr[i] = arr[i-1]
			arr[start] = None
			los[stackNumber].start += 1
			los[stackNumber].end += 1
			return True


		if lookRight(stackNumber, start, end):
			return True
		elif lookLeft(stackNumber, start, end):
			return True
		else:
			return False

	def shiftRight(self):
		return True
		# This shifts elemets one step right if possible
		# if los[-1].end < len(los):

	# for pushing an element in ith stack, we are zero indexed to avoid confusion
	def pushAtI(self, stackNumber, element):
		los = self.listOfStacks
		arr = self.array

		start = los[stackNumber].start
		end = los[stackNumber].end

		# print("start,end",start,end)

		if start>end:
			arr[start] = element
			los[stackNumber].end += 1
		else:
			if arr[end+1] is None:
				arr[end+1] = element
				los[stackNumber].end += 1
			else:
				if self.makeSomeSpace(stackNumber, start, end):
					arr[end+1] = element
					los[stackNumber].end += 1
				else:
					print("Array is full, come another day")





s = Stack(10,2)

s.pushAtI(0,1)
s.pushAtI(0,2)
s.pushAtI(0,3)
s.pushAtI(0,4)
s.pushAtI(0,5)


s.pushAtI(1,11)
s.pushAtI(1,12)

s.pushAtI(0,6)

ss = s.listOfStacks
print("first", ss[0].start, ss[0].end)
print("second", ss[1].start, ss[1].end)
print(s.array)