from PIL import Image 
def Croping(a,b,m,n):  
		try: 
			#GIVE THE PATH OF IMAGE
			img = Image.open(a)  
			width,height = img.size
			area = (0, 0, width/m, height/n) 
			img = img.crop(area) 
			#GIVE PATH TO SAVE THE IMAGE IN DESIRED LOCATION
			img.save(b)
			print("CROPPING IS FINISHED")
			exit()  
          
		except IOError: 
			pass
