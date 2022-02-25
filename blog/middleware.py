from django.shortcuts import HttpResponse
# def my_middleware(get_response):
# 	print("One time initialize")
# 	def myfunction(request):
# 		print("This is before view")
# 		response = get_response(request)
# 		print("This is after view")
# 		return response
# 	return myfunction




# class MyMiddleware:
# 	def __init__(self,get_response):
# 		self.get_response = get_response
# 		print("One time initialize")
# 		# One-time configuration and initialization
# 	def __call__(self,request):
# 		print("This is before view")
# 		response = self.get_response(request)
# 		print("This is after view")
# 		return response


class MyMiddleware:
	def __init__(self,get_response):
		self.get_response = get_response
		print("One time initialize")
		# One-time configuration and initialization
	def __call__(self,request):
		print("This is before view")
		response = self.get_response(request)
		print("This is after view")
		return response

	def process_view(request,*args,**kwargs):
		print("This is a process_view before view")
		#return HttpResponse("This is a before view")
		return None




class MyExceptionMiddleware:
	def __init__(self,get_response):
		self.get_response = get_response
		print("One time initialize")
		# One-time configuration and initialization
	def __call__(self,request):
		print("This is before view")
		response = self.get_response(request)
		print("This is after view")
		return response

	def process_exception(self,request,exception):
		cls = exception.__class__.__name__
		print(cls)
		return HttpResponse(exception)
