from random import randrange
import os, sys,subprocess,re 

####################################################################
##                                                                ##
##  Good for inputing specific widths and saving sets of widths.  ##
##  Typing RANDOM in all caps for "Input width:" will yield 20    ##
##  random numbers between 0 and the total width.                 ##
##                                                                ##
####################################################################

def inputwidth(itemWidths=[],totalWidth=0):
	if itemWidths==[] and totalWidth==0:
		try:
			totalWidth=int(input("Input total width: "))
		except ValueError:
			print("Try again!")
			inputwidth()
		item="DEFAULT"
		itemWidths=[]
		relev=0
		while item != "":
			item=input("Input width: ")
			if item=="RANDOM":
				for i in range(0,20):
					itemWidths.append((randrange(0,totalWidth),i))
			try:
				itemWidths.append((int(item),relev))
			except TypeError:
				print("Item not an Integer")
				inputwidth()

			except ValueError:
				break
			relev+=1

		print ("Current List:\n"+str(itemWidths))		
		saver=input("Save workspace (Y/N)? ")
		
		if saver.upper()=="Y":
			
			if not (os.path.exists('./spencer/')):
				os.mkdir('./spencer')
			savename=input("Savename?: ")
			x=open('./spencer/'+savename+'.txt', 'w')
			text="Total Width: "+str(totalWidth)+"\n"
			counter=0
			for i in itemWidths:
				text=text+"Item"+str(counter)+": "+str(i[0])+"\tRelevance: "+str(i[1])+"\n"
				counter=counter+1
			x.write(text)
			x.close()
			main()
		
		elif saver.upper()=="N":
			inputwidth(itemWidths,totalWidth)

		else:	
			print ("ERROR!")
			inputwidth(itemWidths,totalWidth)
	else:
		item="DEFAULT"
		relev=0
		while item != "":
			item=input("Input width: ")
			try:
				itemWidths.append(int(item),relev)
			except TypeError:
				print("Item not an Integer")
				inputwidth()
			except ValueError:
				break
			relev+=1
		print ("Current List:\n"+str(itemWidths))	
		saver=input("Save workspace (Y/N)? ")
		
		if saver.upper()=="Y":
			
			if not (os.path.exists('./spencer/')):
				os.mkdir('./spencer')
			savename=input("Savename?: ")
			x=open('./spencer/'+savename+'.txt', 'w')
			text="Total Width: "+str(totalWidth)+"\n"
			counter=0
			for i in itemWidths:
				text=text+"Item"+str(counter)+": "+str(i[0])+"\tRelevance: "+str(i[1])+"\n"
				counter=counter+1
			x.write(text)
			x.close()
			main()
		
		elif saver.upper()=="N":
			inputwidth(itemWidths,totalWidth)

		else:	
			print ("ERROR!")
			inputwidth(itemWidths,totalWidth)


# Will segment numbers into groups that try add up to the total width
# This function is where I program the algorithm that Spencer wants


#########################
###  edits start here ###
#########################


def list_sum(liste):
	liste=[x[0] for x in liste]
	results=0
	for item in liste:
		results+=item
	return results



def segmentWidths(totalW, itemW, option):

	# Solution1: Set up about 9 rows or so. Make it fill up the rows one
	# item at a time, going back and starting with the first row each
	# time.
	# Pro: it works with my current test set (no item above 3/4ths the total width)
	# and is linear time.
	# Con: it's not scalable. in the worst case scenario, where each item
	# is close to the total width, you would end up with 9 occupied rows
	# with the last one having 11 items, all too big

	if option==1:
		results=[]
		
		test1=[]
		buffer1=[]
		test2=[]
		buffer2=[]
		test3=[]
		buffer3=[]
		test4=[]
		buffer4=[]
		test5=[]
		buffer5=[]
		test6=[]
		buffer6=[]
		test7=[]	
		buffer7=[]
		test8=[]
		buffer8=[]
		buffer9=[]

		for item in itemW:
			test1.append(item)
			if list_sum(test1)<=totalW:
				buffer1.append(item)
			else:
				test1.pop()
				test2.append(item)
				if list_sum(test2)<=totalW:
					buffer2.append(item)
				else:
					test2.pop()
					test3.append(item)
					if list_sum(test3)<=totalW:
						buffer3.append(item)
					else:
						test3.pop()
						test4.append(item)
						if list_sum(test4)<=totalW:
							buffer4.append(item)
						else:
							test4.pop()
							test5.append(item)
							if list_sum(test5)<=totalW:
								buffer5.append(item)
							else:
								test5.pop()
								test6.append(item)
								if list_sum(test6)<=totalW:
									buffer6.append(item)
								else:
									test6.pop()
									test7.append(item)
									if list_sum(test7)<=totalW:
										buffer7.append(item)
									else:
										test7.pop()
										test8.append(item)
										if list_sum(test8)<=totalW:
											buffer8.append(item)
										else:
											buffer9.append(item)

		results.append(buffer1)
		results.append(buffer2)
		results.append(buffer3)
		results.append(buffer4)
		results.append(buffer5)
		results.append(buffer6)
		results.append(buffer7)
		results.append(buffer8)
		results.append(buffer9)
	
#################################################################

	# Solution 2: Start with a list within a list. Use a for loop 
	# to process each item separately with a recursive function
	# that works on a counting variable to keep track of which row 
	# to operate on.
	# Pro: it works and is a scalable solution. And it's ingenious
	# and totally my idea. 
	# Con: It's definitely not linear time. Calling the function
	# recursively until the problem is solved can't be good for
	# time complexity; at best it is O(n^2).
	
	if option==2:
		results=[[]]

		def magic(item,i=0):
			if list_sum(results[i])+item[0]<=totalW:
				results[i].append(item)
				i-=i
			else:
				i+=1
				if i==len(results):
					results.append([])
				magic(item,i)
				

		for item in itemW:
			magic(item,0)
	
##################################################################

	# Solution 3: List within a list. Nested for-loops. 
	# Outer loop iterates through items, inner loop 
	# iterates through result segments and pushes 
	# Pro: Works, is scalable, and is less lines of code.
	# Time complexity is also more predictable!
	# Con: Spencer came up with it and not me!!! Also,
	# it is definitely O(n^2)

	if option==3:

		results=[[]]
		for item in itemW:
			for result in results:
				if list_sum(result)+item[0]<=totalW:
					result.append(item)
					break
				elif results.index(result)==len(results)-1:
					results.append([item])
					break


########################							
##   edits end here   ##
########################

	print("The algo segments thusly:\n"+str(results))
	startover=input("Try again (Y/N)? ")
	if startover.upper()=="Y":
		main()
	elif startover.upper()=="N":
		print("Goodbye!")
		sys.exit(0)
	else:
		segmentWidths(totalW,itemW)

## loads data from .txt file in 'spencer' folder

def loadwidth():
	savename=input("Savename?: ")
	clean=re.search(r'.txt', savename)
	if clean is not None:
		savename=savename[0:-4]
	try:
		x=open('./spencer/'+savename+'.txt','r')
	except AttributeError:
		print("No such file!")
	find="DEFAULT"
	totalfind="DEFAULT"
	itemWidths=[]
	totalWidth=0
	while find is not None or totalfind is not None:
		line=x.readline()
		totalfind=re.search(r"([\d]+)\n",line)
		find=re.search(r"([\d]+)\tRelevance: ([\d]+)\n",line)
		if find is not None:
			itemWidths.append((int(find.group(1)),int(find.group(2))))
		else:
			try:
				totalWidth+=int(totalfind.group(1))
			except AttributeError:
				break

	print("Ready to segment!")
	print ("Total Width: "+str(totalWidth)+"\n"+"Items:\n"+str(itemWidths))
	pause=input("...")
	option=input("Option (1,2 or 3)? ")
	segmentWidths(totalWidth, itemWidths,int(option))

###################
#### main menu ####
###################

def main():
	print("Hello! Whatcha gonna do?")
	print("(I)nput widths!")
	print("(L)oad widths and Segment!")
	print("(E)xit!")
	option=input("")
	if option.upper()=="I":
		inputwidth()
	elif option.upper()=="L":
		loadwidth()
	elif option.upper()=="E":
		sys.exit(0)
	else:
		print("Try again!")
		main()


if __name__=='__main__':
	main()