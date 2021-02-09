#_*_coding: utf8 _*_
class Calculadora:
	def suma(self,a,b):
		return a+b
	def resta(self,a,b):
		return a-b
	def multiplicacion(self,a,b):
		return a*b
	def division(self,a,b):
		if b==0:
			print "Division entre cero"
		else:
			return a/b
calc=Calculadora()			
a,b=4,4			
print "El resultado de la suma es %s y %s es %s" % (a,b,calc.suma(a,b))
print "El resultado de la resta es %s y %s es %s" % (a,b,calc.resta(a,b))
print "El resultado de la multiplicacion es %s y %s es %s" % (a,b,calc.multiplicacion(a,b))
print "El resultado de la division es %s y %s es %s" % (a,b,calc.division(a,b))								