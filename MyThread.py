import threading
class BaseThread(threading.Thread):
	def __init__(self,fun,args,name):
		threading.Thread.__init__(self):
		self.fun=fun
		self.args=args
		self.name=name
	
	def run(self):
		self.result=apply(self.fun,self.args)

	def getResult(self)
		return self.result
