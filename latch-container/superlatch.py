import json
import os
import latch
import time

class DockerLatch():

	def __init__(self):
		self.LATCH_INFO_PATH = "/usr/share/latch/latch-info.json"
		self.app_id = os.environ.get('LATCH_APP_ID', '')
		self.secret_key = os.environ.get('LATCH_SECRET_KEY', '')
		self.account_id = os.environ.get('LATCH_ACCOUNT_ID', '')
		self.api = latch.Latch(self.app_id, self.secret_key )

		self.refresco = os.environ.get('REFRESCO', '2')

	def latch_pairing(self):
		pair_code = input("Type Pairing code:")
		response = self.api.pair(pair_code)
		responseData = response.get_data()
		responseError = response.get_error()
		# print ("Respuesta: ", responseData)
		if responseError != "" :
 			print ("Error:" , responseError)

		try:
    			salida=json.dumps(responseData)
		except (TypeError, ValueError) as err:
    			print ('ERROR:', err)


	def latch_status(self):
		response = self.api.status(self.account_id)
		responseData = response.get_data()
		responseError = response.get_error()
		#print ("Respuesta: ", responseData)
		if responseError != "" :
 			print ("Error:" , responseError)
		try:
    			salida=json.dumps(responseData)
		except (TypeError, ValueError) as err:
    			print ('ERROR:', err)

		response = json.loads(salida)

		statuslatch = response['operations'][self.app_id]['status']
		print ("Estado:", statuslatch)

		return statuslatch


	def latch_update(self, stlatch):
		data = {}
		# data['Docker Latch']=[]
		# data['Docker Latch'].append({
		# 	'status': stlatch
		# })
		data['latched'] = stlatch == 'off'
		data['lastUpdate'] = time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime())

		with open(self.LATCH_INFO_PATH,'w') as outfile:
			json.dump(data, outfile)



if __name__ == '__main__':
	
	superlatch = DockerLatch()
	#superlatch.latch_pairing()
	while True:
		latchstatus = superlatch.latch_status()
		superlatch.latch_update(latchstatus)
		time.sleep(int(superlatch.refresco))

