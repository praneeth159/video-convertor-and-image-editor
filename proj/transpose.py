from PIL import Image 
  
def Transpose(a,b): 
    try: 
        #GIVE THE PATH AS INPUT
        i = Image.open(a)  
        #SAVING THE TRANSPOSED IMAGE IN A VARIABLE
        ti = i.transpose(Image.FLIP_LEFT_RIGHT) 
        #SAVE A TRANSPOSED IMAGE IN A FOLDER
        ti.save(b) 
        print("TRANSPOSE IS FINISHED")
        exit()
    except IOError: 
        pass
