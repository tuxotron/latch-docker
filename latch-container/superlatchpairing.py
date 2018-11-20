#Latch pairing
#Export first LATCH_APP_ID, LATCH_SECRET_KEY and LATCH_ACCOUNT_ID before pairing

import json
import os
import latch
import time

class DockerLatch():


	def __init__(self):
		self.app_id = os.environ.get('LATCH_APP_ID', '')
		self.secret_key = os.environ.get('LATCH_SECRET_KEY', '')
		self.account_id = os.environ.get('LATCH_ACCOUNT_ID', '')
		self.api = latch.Latch(self.app_id, self.secret_key )

	def latch_pairing(self):
		pair_code = input("Type Pairing code:")
		response = self.api.pair(pair_code)
		responseData = response.get_data()
		responseError = response.get_error()
		print ("Respuesta: ", responseData)
		if responseError != "" :
 			print ("Error:" , responseError)

		try:
    			salida=json.dumps(responseData)
		except (TypeError, ValueError) as err:
    			print ('ERROR:', err)

if __name__ == '__main__':
	
	superlatch = DockerLatch()	
	superlatch.latch_pairing()


