#IMPORT ALL LIBRARIES THAT ARE NEEDED 
import cv2 
import os 
#GIVE THE SPECIFIED PATH
def Converting(a,b):
	vid = cv2.VideoCapture(a) 
	try: 
      
		#CREATE A NEW FOLDER AND STORE IN IT 
		if not os.path.exists(b): 
			os.makedirs(b) 
  
	#ERROR THROWS AS FOLDER IS NOT CREATED 
	except OSError: 
		print ('Error: Creating directory of data') 
	#FRAME
	f = 0
  
	while(True):  
		frame1,frame = vid.read() 
  
		if frame1:  
			name = './%s/frame'%b + str(f) + '.jpg'
			print ('Created' + name) 
  
			#THIS IS USED TO WRITE THE EXTRACTED IMAGES 
			cv2.imwrite(name, frame)  
			# COUNT OF NUMBER OF FRAMES 
			f += 1
		else: 
			print("Coverting is finished")
			break
  
	#WINDOW AND SPACE IS TO BE FREED AFTER COMPLETION 
	vid.release() 
	cv2.destroyAllWindows() 
	exit()
