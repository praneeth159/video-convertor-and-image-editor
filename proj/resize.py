from PIL import Image 
  
def Resize(a,b,width,height): 
    try: 
         #GIVE THE PATH OF IMAGE
        img = Image.open(a) 
   
        img = img.resize((width, height)) 
          
        #SET THE PATH TO SAVE LOCATION 
        img.save(b)  
        print("Resizing is finished ")
        exit()
    except IOError: 
        pass
