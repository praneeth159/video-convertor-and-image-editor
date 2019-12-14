#PYTHON IMAGING LIBRARY
from PIL import Image 
def Rotate(a,b,angl): 
	try: 
		#GIVE IMAGE PATH
		img = Image.open(a)
		 
		#GIVE ANGLE TO STORE
		img = img.rotate(angl) 
		
		#GIVE FOLDER TO STORE 
		img.save(b) 
		print("ROTATION IS FINISHED")
		exit()
	except IOError: 
		pass
