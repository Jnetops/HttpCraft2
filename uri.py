
class uriParse(object):

	def uriIter(request_custom_dict, request_uri, current_val):
		urIVar = request_uri.split(str(request_custom_dict["url"]))
		iter_request_uri = ""
		for val in urIVar:
			if (val != ""):
				if (urIVar.index(val) == 0):
					# first in list
					iter_request_uri = val + str(current_val)
				elif (urIVar.index(val) == len(urIVar) - 1):
					# last in list
					iter_request_uri = iter_request_uri + val
				else:
					# all others
					iter_request_uri = iter_request_uri + val + str(current_val)

		return iter_request_uri