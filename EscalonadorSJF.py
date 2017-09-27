class EscalonadorSJF(object):

	def __init__(self,processos):
		self.__processos = processos
		self.__filaProntos = []

	def executar(self):		
		instante = 0;
		while self.existemProcessosNaoConcluidos():															
			self.chegouNovoProcesso(instante)
			if( self.processoExecutandoConcluiu(instante) ):
				self.selecionarNovoProcessoProntoParaExecutar()						
			instante = instante + 1 			

	def listagemProcessos(self):
		for processo in self.__processos:
			processo.toString()

	def processoExecutandoConcluiu(self,instante):
		for processo in self.__processos:
			if(processo.getStatus() == "EXECUTANDO"):
				if(processo.getTempoExecucao() == 1):
					self.atualizarStatusProcesso(processo.getId(),"FINALIZADO",instante)		
					return True
				else:
					processo.decrementaTempoExecucao()
					return False
		return True					

	def existemProcessosNaoConcluidos(self):
		for processo in self.__processos:
			if(processo.getStatus() != "FINALIZADO"):
				return True
		return False

	def getProcessoPronto(self):
		for processo in self.__filaProntos:
			return processo

	def chegouNovoProcesso(self,instante):		
		for processo in self.__processos:
			if(processo.getTempoChegada() == instante):
				processo.setStatus("PRONTO")
				self.__filaProntos.append(processo)		
	
	def ordenarListaProcessosProntos(self):		
		#print( "antes de ordenar")
		'''if(len(self.__filaProntos) > 0):
			for processo in self.__filaProntos:
				processo.toString()
			print(self.__filaProntos[0].getTempoExecucao())
			print("comprimento vetor = ",len(self.__filaProntos))
		'''
		self.__filaProntos = sorted(self.__filaProntos, key=lambda processo: processo.getTempoExecucao())
		#print( "depois de ordenar")
		#if(len(self.__filaProntos) > 0):
			#for processo in self.__filaProntos:
			#	processo.toString()
			#print(self.__filaProntos[0].getTempoExecucao())
			#print("comprimento vetor = ",len(self.__filaProntos))

	def selecionarNovoProcessoProntoParaExecutar(self):		
		self.ordenarListaProcessosProntos()		
		if(len(self.__filaProntos) > 0):		
			processo = self.__filaProntos.pop(0)			
			#print("processo escolhido ")
			#processo.toString()
			self.atualizarStatusProcesso(processo.getId(),"EXECUTANDO")			
    
	def atualizarStatusProcesso(self,id,status,instante = 0):
		for processo in self.__processos:
			if(processo.getId() == id):
				processo.setStatus(status)				
				if(status == "FINALIZADO"):
					processo.addTempoDoProcesso(instante)

	def calcularMedia(self):
		soma = 0 
		for processo in self.__processos:
			soma = soma + processo.getTempoDoProcesso()
		return soma/len(self.__processos)	