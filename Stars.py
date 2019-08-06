import sys

sys.stdout.write("\n")

class Pyramid:
	def __init__(self):
		pass
	def normalSquare(self):
		stars = []
		for i in range(5):
			if i != 0 :
				sys.stdout.write("\n")
			for y in range(5):
				sys.stdout.write("*")

	def drawPyramidNormal(self):
		i = 1
		rows = 2
		while i <= rows:
			j = 1
			while j <= (rows - i) * 2:
				sys.stdout.write(" ")
				j += 1
			k = i
			while k >= 1:
				sys.stdout.write(" " + "*")
				k -= 1
			l = 2
			while l <= i:
				sys.stdout.write(" " + "*")
				l += 1
			sys.stdout.write("\n")   
			i += 1 

	def drawPyramidNormalNew(self):
		i = 1
		k = 0
		rows = 5
		while i <= rows:
			space = 1
			while space <= (rows - i):
				sys.stdout.write("  ")
				space += 1
			while k != (2 * i - 1):
				sys.stdout.write("* ")
				k += 1
			sys.stdout.write("\n")
			k = 0
			i += 1


	def drawPyramidLeftHandSide(self):
		i = 0
		rows = 5
		while i <= rows:
			j = 0
			while j <= i:
				sys.stdout.write("* ")
				j += 1
			sys.stdout.write("\n")
			i += 1

	def drawPyramidLeftHandSideCustom(self):
		i = 0
		k = 1
		rows = 5 
		while i <= rows:
			j = 0
			while j < k:
				sys.stdout.write("* ")
				j += 1
			k += 2
			sys.stdout.write("\n")
			i += 1
	def drawPyramidRightHandSide(self):
		i = 0
		j = 0
		rowk = 8
		rowI = 5
		while i < rowI:
			j = 0
			while j <= rowk:
			  sys.stdout.write(" ")
			  j += 1
			rowk -= 2
			j = 0
			while j <= i:
				sys.stdout.write("* ")
				j += 1
			i += 1	
			sys.stdout.write("\n")

	def drawPyramidRightHandSideCustom(self):
		i = 0
		j = 0
		k = 16
		tim = 1
		rows = 5
		while i < rows:
			j = 0
			while j < k :
				sys.stdout.write(" ")
				j += 1
			k -= 4
			j = 0
			while j < tim: 
				sys.stdout.write("* ")
				j += 1
			tim += 2
			i += 1
			sys.stdout.write("\n")

	def diamond(self):
		i = 1
		j = 1
		rowI = 4
		while i <= rowI:
			j = 1
			while j <= rowI - i :
				sys.stdout.write(" ")
				j += 1 
			j = 1
			while j <= i * 2 - 1:
				sys.stdout.write("*")
				j += 1
			sys.stdout.write("\n")
			i += 1

		i = rowI - 1
		while i > 0:
			j = 1
			while j <= rowI - i:
				sys.stdout.write(" ")
				j += 1
			j = 1
			while j <= i * 2 - 1:
				sys.stdout.write("*")
				j += 1
			sys.stdout.write("\n")
			i -= 1

	def newDiamond(self):
		i = 1
		rowI = 5 
		while i <= rowI:
			j = i
			while j < rowI:
				sys.stdout.write(" ")
				j += 1
			j = 1	
			while j <= 2 * i - 1:
				sys.stdout.write("*")
				j += 1
			i += 1
			sys.stdout.write("\n")
		i = rowI
		while i >= 1:
			j = i 
			while j <= rowI:
				sys.stdout.write(" ")
				j += 1
			j = 2
			while j < 2 * i - 1:
				sys.stdout.write("*")
				j += 1
			i -= 1
			sys.stdout.write("\n")

	def invertDiamond(self):
		j = 1
		space = 0
		rowI = 5
		i = rowI
		while i >= 1:
			j = i
			while j >= 1:
				sys.stdout.write("*")
				j -= 1 
			j = 1
			while j <= space:
				sys.stdout.write(" ")
				j += 1
			j = i
			while j >= 1 :
				sys.stdout.write("*")
				j -= 1
			sys.stdout.write("\n")
			i -= 1
			space += 2
		space = 8
		i = 1
		while i <= rowI:
			j = 1
			while j <= i:
				sys.stdout.write("*")
				j += 1
			j = 1
			while j <= space:
				sys.stdout.write(" ")
				j += 1
			j = 1
			while j <= i :
				sys.stdout.write("*")
				j += 1
			sys.stdout.write("\n")
			i += 1
			space -= 2
	
	def Xstars(self):
		i = 1
		rowI = 5
		i = rowI
		while i >= 1:
			j = i
			while j < rowI:
				sys.stdout.write(" ")
				j += 1 
			j = 1
			while j <= 2 * i -1:
				if j == 1 or j == (2 * i - 1):
					sys.stdout.write("*")
				else:
					sys.stdout.write(" ")
				j += 1
			sys.stdout.write("\n")
			i -= 1
		i = 2
		while i <= rowI:
			j = i
			while j < rowI:
				 sys.stdout.write(" ")
				 j += 1
			j = 1
			while j <= 2 * i - 1:
				if j == 1 or j == (2 * i - 1):
					sys.stdout.write("*")
				else:
					sys.stdout.write(" ")
				j += 1

			sys.stdout.write("\n")
			i += 1

	def arrowStarsleft(self):
		i = 1
		rowI = 5
		while i <= rowI:
			j = 1
			while j <= i:
				sys.stdout.write("*")
				j +=1 
			sys.stdout.write("\n")
			i += 1 
		i = rowI
		while i >= 1:
			j = 1
			while j < i:
				sys.stdout.write("*")
				j += 1
			i -= 1
			sys.stdout.write("\n")

	def leftTriangle(self):
		i = 1
		rowI = 5
		while i <= rowI:
			j = 1
			while j <= i:
				sys.stdout.write("*")
				j += 1

			i += 1
			sys.stdout.write("\n")


	def invertLeft(self):
		i = 1
		rowI = 5
		while i <= rowI:
			j = i
			while j <= rowI:
				sys.stdout.write("*")
				j += 1

			i += 1	
			sys.stdout.write("\n")

	def invertRight(self):
		i = 1
		rowI = 5 
		while i <= rowI:
			j = 1
			while j < i:
				sys.stdout.write(" ")
				j += 1
			j = i 
			while j <= rowI:
				sys.stdout.write("*")
				j += 1

			i += 1 
			sys.stdout.write("\n")

	def invertRightTop(self):
		i = 1
		rowI = 5 
		while i <= rowI:
			j = i
			while j < rowI:
				sys.stdout.write(" ")
				j += 1
			j = 1
			while j <= i:
				sys.stdout.write("*")
				j += 1
			i += 1 
			sys.stdout.write("\n")

pyramid = Pyramid()
#pyramid.newDiamond()

pyramid.invertLeft()
pyramid.leftTriangle()

pyramid.invertRight()
pyramid.invertRightTop()

#pyramid.invertLeft()

#pyramid.invertDiamond()
#pyramid.drawPyramidNormalNew()
#pyramid.drawPyramidLeftHandSide()
#pyramid.drawPyramidLeftHandSideCustom()
#pyramid.drawPyramidRightHandSide()
#pyramid.drawPyramidRightHandSideCustom()

