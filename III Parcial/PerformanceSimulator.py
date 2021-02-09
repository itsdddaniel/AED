import random
from datetime import datetime

class Simulator:
	def createHTML(self,m,htmlFileName="html.html"):
		html=[]
		html.append("<meta charset='utf-8'>")
		html.append("<script src=table.html></script>")
		html.append("<script>")
		html.append("var m=%s;" %(m))
		html.append("document.write((new MyTable().draw(m));")

		f=open(htmlFileName,"w")
		f.write("".join(html))
		f.close()

class TestAlgorithm:
	def test(self,algorithm,data,execution):
		i=execution.getTime()
		algorithm.sort(data)
		f=execution.getTime()
		return (len(data),execution.diff(i,f))		

class ExecutionTime:
	def diff(self,i,f):
		diff=f-i
		m=diff.days*24*60*60*1000
		m+=diff.seconds*1000
		m+=diff.microseconds/1000
		return m
	
	def getTime(self):
		return datetime.now()

class ArrayGenerator:
	def create(self,n=1000,min=0,max=1000):
		array=[]
		for i in range(n):
			array.append(random.random()*(max-min)*(min))				
		return array

class BubbleSort:
	def sort(self,array=[]):
		for i in range(len(array)):
			for j in range(len(array)):
				if array[i] < array[j]:
					temp = array[i]
					array[i] = array[j]
					array[j] = temp		