class EscalonadorEDF(object):

	def __init__(self,processos):
		self.__processos = processos
		self.__filaProntos = []
		self.__quantum = 4
		self.__processoConcluiu = False

	"""	
	def executar(self):		
		quantum = self.__quantum
		instante = 0
		preempcao = False
		while self.existemProcessosNaoConcluidos():															
			self.chegouNovoProcesso(instante)
			if( preempcao ):
				#print("preempcao", instante)
				quantum = self.__quantum
				self.selecionarNovoProcessoProntoParaExecutar()
				preempcao = False
			else:				
				if( self.processoExecutandoConcluiu(instante) or quantum == 0 ):					
					if(quantum == 0 and self.__processoConcluiu != True):
						preempcao = True
						self.processoSofreuPreempcao()						
					else:
						quantum = self.__quantum
						self.__processoConcluiu = False	
					self.selecionarNovoProcessoProntoParaExecutar()						
				quantum = quantum - 1 	
			instante = instante + 1
			#print("instante ",instante)
			self.decrementarPrioridadeProcessos()
	"""

	def executar(self):		
		quantum = self.__quantum
		instante = 0
		preempcao = False
		while self.existemProcessosNaoConcluidos():																					
			self.chegouNovoProcesso(instante)			
			if(preempcao == False):
				if(self.processoExecutandoConcluiu(instante)):				
					self.selecionarNovoProcessoProntoParaExecutar()
					quantum = self.__quantum 																			
				else:
					quantum = quantum - 1
					if(quantum == 0):
						preempcao = True						
						self.processoSofreuPreempcao()
						#print("edf preempcao inicio ", instante)
			else:
				preempcao = False
				self.selecionarNovoProcessoProntoParaExecutar()
				#print("edf preempcao fim ", instante)
				quantum = self.__quantum								
			instante = instante + 1
			self.decrementarPrioridadeProcessos()

	def processoSofreuPreempcao(self):
		for processo in self.__processos:
			if(processo.getStatus() == "EXECUTANDO"):
				processo.setStatus("PRONTO")
				self.__filaProntos.append(processo)
			
	def listagemProcessos(self):
		for processo in self.__processos:
			processo.toString()

	def processoExecutandoConcluiu(self,instante):
		for processo in self.__processos:
			if(processo.getStatus() == "EXECUTANDO"):
				if(processo.getTempoExecucao() == 1):
					self.atualizarStatusProcesso(processo.getId(),"FINALIZADO",instante)		
					self.__processoConcluiu = True
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
	
	def decrementarPrioridadeProcessos(self):
		#print("decrementarPrioridadeProcessos")
		for processo in self.__filaProntos:
			processo.decrementarDeadline()
		
		for processo in self.__processos:
			if(processo.getStatus() == "EXECUTANDO"):
				processo.decrementarDeadline()


	def ordenarListaProcessosProntos(self):		
		self.__filaProntos = sorted(self.__filaProntos, key=lambda processo: processo.getDeadline())
		
	def selecionarNovoProcessoProntoParaExecutar(self):				
		self.ordenarListaProcessosProntos()
		#for processo in self.__filaProntos:			
		if( len(self.__filaProntos) > 0 ):
			processo = self.__filaProntos.pop(0)			
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
