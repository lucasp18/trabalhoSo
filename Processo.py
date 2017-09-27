class Processo(object):
	
	_pId = 1
	
	def get_pId(self):
	    return self._pId
	def set_pId(self,val):
	    self._pId = self._pId + 1
	pId = property(get_pId, set_pId)

	def __init__(self,status,tempoChegada,tempoExecucao,deadline = 0):
		self.__status = status
		self.__tempoChegada = tempoChegada
		self.__tempoExecucao = tempoExecucao
		self.__tempoDoProcesso = 0
		self.__tempoExecutando = 0
		self.__deadline = deadline
		self.__id = Processo._pId		
		Processo._pId = Processo._pId +1
		
	def getStatus(self):
		return self.__status

	def getTempoChegada(self):
		return self.__tempoChegada

	def getTempoExecucao(self):
		return self.__tempoExecucao

	def getTempoDoProcesso(self):
		return self.__tempoDoProcesso	
	
	def getId(self):
		return self.__id
	
	def setStatus(self,status):
		self.__status = status

	def getDeadline(self):
		return self.__deadline	

	def addTempoDoProcesso(self,instante):		
		self.__tempoDoProcesso = instante - self.__tempoChegada 
	
	def decrementaTempoExecucao(self):
		self.__tempoExecucao = self.__tempoExecucao - 1

	def decrementarDeadline(self):
		self.__deadline = self.__deadline - 1

	def toString(self):
		print("id =",self.__id," tempoDoProcesso = ", self.__tempoDoProcesso," tempo de chegada = ",self.__tempoChegada," status =", self.__status, " deadline =", self.__deadline)
