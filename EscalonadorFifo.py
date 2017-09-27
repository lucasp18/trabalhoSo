class EscalonadorFifo(object):

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

	def selecionarNovoProcessoProntoParaExecutar(self):
		#for processo in self.__filaProntos:			
		if(len(self.__filaProntos) > 0 ):
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