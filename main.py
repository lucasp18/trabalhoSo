from Processo import Processo 
from EscalonadorFifo import EscalonadorFifo
from EscalonadorSJF import EscalonadorSJF
from EscalonadorRoundRobin import EscalonadorRoundRobin
from EscalonadorEDF import EscalonadorEDF

import copy

if __name__ == "__main__":
	#STATUS | TEMPO CHEGADA | TEMPO EXECUCAO | deadline
	#p0 = Processo("CHEGANDO",6,3,10)
	#p1 = Processo("CHEGANDO",0,4,2)	
	#p2 = Processo("CHEGANDO",2,2,5)
	#p3 = Processo("CHEGANDO",4,1,8)
	#p4 = Processo("CHEGANDO",0,8,0)
	#p4 = Processo("CHEGANDO",8,3)
	processos = []
	
	qtdProcessos = int(input('Digite a quantidade de processos : ') )
	qtdProcessosInseridos = 1;
	while(qtdProcessos >= qtdProcessosInseridos):
		print("informações do processo id = ",qtdProcessosInseridos)
		tempoChegada = int(input("Tempo de chegada do processo: ") )		
		tempoExecucao = int(input('Tempo de execução do processo: ') )
		prioridade = int(input('deadline do processo: ') )
		processo = Processo("CHEGANDO",tempoChegada,tempoExecucao,prioridade)
		qtdProcessosInseridos = qtdProcessosInseridos + 1
		processos.append(processo)
	"""
	processos.append(copy.copy(p0))
	processos.append(copy.copy(p1))
	processos.append(copy.copy(p2))
	processos.append(copy.copy(p3))
	"""
	
	"""
	processos.append(p0)
	processos.append(p1)
	processos.append(p2)
	processos.append(p3)
	#processos.append(p4)	
	"""
	"""
	processos1 = []
	processos1.append(p0)
	processos1.append(p1)
	processos1.append(p2)
	processos1.append(p3)
	"""
	
	#processos1 = copy.copy(processos)
	#processos2 = copy.copy(processos)
	print("-----------------------RESULTADOS:---------------------------")
	escalonadorFifo = EscalonadorFifo(copy.deepcopy(processos))
	escalonadorFifo.executar()
	escalonadorFifo.listagemProcessos()
	print("Média da execução dos processos escalonador FIFO = ",escalonadorFifo.calcularMedia())
	print("------------------------------------------------------------")
	escalonadorSJF = EscalonadorSJF(copy.deepcopy(processos))
	escalonadorSJF.executar()
	escalonadorSJF.listagemProcessos()
	print("Média da execução dos processos escalonador SJF = ",escalonadorSJF.calcularMedia())
	print("------------------------------------------------------------")
	escalonadorRoundRobin = EscalonadorRoundRobin(copy.deepcopy(processos))
	escalonadorRoundRobin.executar()
	escalonadorRoundRobin.listagemProcessos()
	print("Média da execução dos processos escalonador Round Robin = ",escalonadorRoundRobin.calcularMedia())
	print("------------------------------------------------------------")
	escalonadorEDF = EscalonadorEDF(copy.deepcopy(processos))
	escalonadorEDF.executar()
	escalonadorEDF.listagemProcessos()
	print("Média da execução dos processos escalonador EDF = ",escalonadorEDF.calcularMedia())
