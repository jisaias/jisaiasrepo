from PIL import Image

#opens the images
img1 = Image.open("1.png")
img2 = Image.open("2.png")
img3 = Image.open("3.png")
img4 = Image.open("4.png")
img5 = Image.open("5.png")
img6 = Image.open("6.png")
img7 = Image.open("7.png")
img8 = Image.open("8.png")
img9 = Image.open("9.png")

width, height = img1.size #assigns the height and width to use for the new image

final = Image.new("RGB", (width, height)) #creates new image for the final product

pixel1 = img1.load()
pixel2 = img2.load()
pixel3 = img3.load()
pixel4 = img4.load()
pixel5 = img5.load()
pixel6 = img6.load()
pixel7 = img7.load()
pixel8 = img8.load()
pixel9 = img9.load()

#lists for the RGB values and the final values
red = []
blue = []
green = []
finallist = []

            
for y in range (height):
    for x in range (width):
        #Goes through each individual pixel in each image and adds their rgb values to their respective lists
        red1, green1, blue1 = pixel1[x,y]
        red.append(red1)
        blue.append(blue1)
        green.append(green1)
        red2, green2, blue2 = pixel2[x,y]
        red.append(red2)
        blue.append(blue2)
        green.append(green2)
        red3, green3, blue3 = pixel3[x,y]
        red.append(red3)
        blue.append(blue3)
        green.append(green3)
        red4, green4, blue4 = pixel4[x,y]
        red.append(red4)
        blue.append(blue4)
        green.append(green4)
        red5, green5, blue5 = pixel5[x,y]
        red.append(red5)
        blue.append(blue5)
        green.append(green5)
        red6, green6, blue6 = pixel6[x,y]
        red.append(red6)
        blue.append(blue6)
        green.append(green6)
        red7, green7, blue7 = pixel7[x,y]
        red.append(red7)
        blue.append(blue7)
        green.append(green7)
        red8, green8, blue8 = pixel8[x,y]
        red.append(red8)
        blue.append(blue8)
        green.append(green8)
        red9, green9, blue9 = pixel9[x,y]
        red.append(red9)
        blue.append(blue9)
        green.append(green9)
            
        #sorts each list
        red.sort()
        blue.sort()
        green.sort()
        
        #gets the median values from the lists
        medianPixel = (red[4], green[4], blue[4])
        
        #adds this median value to final list
        finallist.append(medianPixel)
        
        #clears lists
        del red[:]
        del blue[:]
        del green[:]

#puts data into the image
final.putdata(finallist)
final.save("final.png")
            
            
            
            
