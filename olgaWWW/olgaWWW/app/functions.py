class json(object):
	""" Operations with json to string or opposite"""
	def __init__(self, messageError):
		self.messageError = messageError

	def getMessageFormCleanValidation(self):
		""" Message error has format { name : [ { } ] }
		    function get message errors from string, string has json format
		    param1 - string in json format
		    return - error message
		"""
		import json

		if not isinstance(self.messageError, str):
		    return None

		jsonObject = json.loads(self.messageError)
		ans=""
		for val in jsonObject.values():
		    for list in val:
		        for key,value in list.items():
		            if key=="message":
		                ans += value + ","
		return ans[:-1]

		def __str__(self):
			return str(self.messageError)