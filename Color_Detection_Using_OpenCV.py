#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import cv2  # It is a computer vision library
# While in computer colors are stored in the form of R,G,B values, but in opencv colors are stored in the form of B,G,R format

df1 = pd.read_csv('colors.csv',names=['color','color_name','hex_value','R','G','B']) # Pandas is used for importing csv files

df1.head()# As you can see clearly it does not have any header we have to include it

# We are adding a header to our df1 so we are saying names = what we are planning to give while we are importing the file only

# Now are planning to check how many rows and coloums are present in the given datafile which is 
print(df1.shape)

# If we want to extract only a particular row in the df1 
# df1.loc[1]

# Since we have to used pandas for importing csv files we will use opencv to import images

df2 = cv2.imread('pic2.jpg')
df2 = cv2.resize(df2,(800,600)) # Since the actual image is larger we are reducing the size of the image


clicked = False   # When we have not clicked the left button yet
r=g=b=xpos=ypos=0  # Here when we click something when it goes inside the function these variables needs to be changed and
                   # these variables inside the fuction needs to be declared globally



#print(df2) # You can check that it is printing an array of numbers so we can say that we humans see images as a  see mix of colors
           # but computer sees it in the form of pixels in a array of R,G,B values

    
# Now you have to create a window so that you have to display your  pic2.jpg so that when we click on a particular spot 
# the corresponding color name with R,G,B values should appear. So, first we will create a window


def draw_function(event,x,y,flags,params): # Event is nothing but when you are pressing something on the image that is event
    if event == cv2.EVENT_LBUTTONDBLCLK:  # Here check properly that you  have to spelling of the events happening as there are inbuilt
        global clicked,r,g,b,xpos,ypos
        clicked = True
        xpos=x
        ypos=y
        #print(x,y)
        b,g,r = df2[y,x]
        #print(b,g,r)
        b=int(b)
        g=int(g)
        r=int(r)
        
def get_color_name(R,G,B):
    minimum = 1000
    for i in range(len(df1)):
        d = abs(R - int(df1.loc[i,'R'])) + abs(G - int(df1.loc[i,'G'])) + abs(B - int(df1.loc[i,'B']))
        if d<=minimum:
            minimum = d
            cname = df1.loc[i,'color_name']
            
    return cname
            
# Checking the function print(get_color_name(0,0,0)) -Black  print(get_color_name(255,255,255))-White
# (255,0,0) - Red
    
    

cv2.namedWindow('Window') # Here you are assigning a name to the window

cv2.setMouseCallback('Window',draw_function) 

#print(clicked,r,g,b,xpos,ypos)
while True:
    cv2.imshow('Window',df2)# Now you have to display your image in that window so the first argumnet in the name of the window
    if clicked ==True:                      # and the second argumnet is which image you wish to pass in it
        cv2.rectangle(df2,(20,20),(600,60),(b,g,r),-1)
        # This is when we click this will create a rectangle with initial position (20,20) and final position (600,60) and thickeness -1
        #Now we are creating a variable called text 
        text  = get_color_name(r,g,b) + ' R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)
        # So here first the color_name will be printed then the corresponding R,G,B component will be printed
        # Now we should keep this text on top of our rectangle which we had created
        cv2.putText(df2,text,(50,50),2,0.8,(255,255,255),2,cv2.LINE_AA)
        # This will put the text and it takes the input df2(image),text, font,font_phase,color,thickness,line_aa
        if r+g+b>=600: #(if the color is too light write it in black color)
            cv2.putText(df2,text,(50,50),2,0.8,(0,0,0),2,cv2.LINE_AA)
            
    if cv2.waitKey(20) & 0xFF==27:  #(If we do not press anything on the window for more than 20 seconds or if you press escape key) 
        break
    
#cv2.waitKey(0)       # Here you are saying that if I press the X button they only close the window otherwise do not close



cv2.destroyAllWindows()  # Here in waitKey the K is capital remember it is very important
# Since the size of the image is displaying in bigger size we have to reduce the size so after the df2 we write one extra
# line of code to resize the image 


# Now when you are taking your cursor on the image it was showing + sign so when you double click on a particular point 
# you should know the position of the cursor inorder to know the corresponding color where you clicked on

# We are creating a function and we have to bind it to our mouse so we have to create

# Now we are getting the corresponding x and y values of that mouse location now we want the R,G,B values of that location
 # so after print(x,y) we continue writing opencv stores values in the form of b,g,r values

# Now we are creating one more function to get the corresponding color name by taking the input R,G,B values


# In[20]:


df1.head()


# In[22]:


df1.loc[1,'R']


# In[ ]:




