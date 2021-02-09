from PerformanceSimulator import(Simulator,ExecutionTime,BubbleSort,ArrayGenerator,TestAlgorithm)

resultTable=[["Algoritmo","Tamano","Tiempo"]]
OriginalArray=ArrayGenerator().create()
OriginalArray=OriginalArray
TestAlgorithm=TestAlgorithm()
ExecutionTime=ExecutionTime()
bubble=BubbleSort()
Simulador=Simulator()

l,t=TestAlgorithm.test(
	algorithm = bubble,
	data = OriginalArray[:],
	execution = ExecutionTime
	)

Simulador.createHTML(resultTable)
resultTable.append(["BubbleSort",l,t])