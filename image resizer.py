from PIL import Image
import numpy
im = Image.open('test.jpg')

iterations = 10
adjustment = 50


for i in range(0, iterations):
    pix = im.load() 
    im2 = im.copy()
    im3 = im.copy()
    size = im.size


    #Calculating the Energy of Each Pixel: Result = im2
    for x in range(0, im.size[0]):
        for y in range(0, im.size[1]):
            pixel1 = pix[x,y]
            if y == 0:
                sumupvalue = 0
            else:        
                pixelup = pix[x,y - 1]
                upvalueR = abs(pixel1[0] - pixelup[0])
                upvalueG = abs(pixel1[1] - pixelup[1])
                upvalueB = abs(pixel1[2] - pixelup[2])
                sumupvalue = upvalueR + upvalueG + upvalueB        
            if y == size[1] - 1:
                sumdownvalue = 0
            else:
                pixeldown = pix[x, y + 1]
                downvalueR = abs(pixel1[0] - pixeldown[0])
                downvalueG = abs(pixel1[1] - pixeldown[1])
                downvalueB = abs(pixel1[2] - pixeldown[2])
                sumdownvalue = downvalueR + downvalueG + downvalueB
            if x == 0:
                sumleftvalue = 0
            else:
                pixelleft = pix[x - 1, y]
                leftvalueR = abs(pixel1[0] - pixelleft[0])
                leftvalueG = abs(pixel1[1] - pixelleft[1])
                leftvalueB = abs(pixel1[2] - pixelleft[2])
                sumleftvalue = leftvalueR + leftvalueG + leftvalueB            
            if x == size[0] - 1:
                sumrightvalue = 0
            else:
                pixelright = pix[x + 1, y]
                rightvalueR = abs(pixel1[0] - pixelright[0])
                rightvalueG = abs(pixel1[1] - pixelright[1])
                rightvalueB = abs(pixel1[2] - pixelright[2])
                sumrightvalue = rightvalueR + rightvalueG + rightvalueB
            pixelenergy = sumupvalue + sumdownvalue + sumleftvalue + sumrightvalue
            im2.putpixel((x, y), (0, 0, int((pixelenergy)/adjustment)))

    

 
    
 
 
    
    #Bottom Row Starting Cumulative Energy
    pix2 = im2.load()
    pix3 = im3.load()
    for x2 in range(0, im.size[0]):
        pe2 = pix2[x2, im.size[1]-1]
        initial = pe2[2]
        im3.putpixel((x2, im.size[1]-1), (initial, 0 , 0))   
    #Rest of the Image Cumulative Energy: Result = im3
    for y3 in reversed(range(0, im.size[1] - 1)):
        for x3 in range(0, im.size[0]):
            pe3 = pix2[x3, y3]   
            if x3 == 0:
                pe3below_middle = pix3[x3, y3 + 1]
                pe3below_right = pix3[x3 + 1, y3 + 1]
                p2me = pe3below_middle[0]
                p2re = pe3below_right[0]
                choice = [p2me, p2re]
                decision = min(choice)
            elif x3 == im.size[0] - 1:
                pe3below_left = pix3[x3 - 1, y3 + 1]
                pe3below_middle = pix3[x3, y3 + 1]
                p2me = pe3below_middle[0]
                p2re = pe3below_right[0]
                choice = [p2me, p2re]
                decision = min(choice)
            else:
                pe3below_left = pix3[x3 - 1, y3 + 1]
                pe3below_middle = pix3[x3, y3 + 1]
                pe3below_right = pix3[x3 + 1, y3 + 1]
                p2le = pe3below_left[0]
                p2me = pe3below_middle[0]
                p2re = pe3below_right[0]
                choice = [p2le, p2me, p2re]
                decision = min(choice)
            cumulative3 = ((pe3[2] + decision))
            im3.putpixel((x3, y3), (int(cumulative3), 0, 0))
            
    

    
    
    #Finding Starting Point to Remove Slice
    im5 = im3.copy()
    startval = []
    for x4 in range(0, im.size[0]):
        pe4 = pix3[x4, 0]
        startval.append(pe4[0])
    xstart = min(startval)
    route = []   
    while True:
        for x4 in range(0, im.size[0]):
            pe4 = pix3[x4, 0]
            if  pe4[0] != xstart:
                continue
            else:
                startco_ord = x4
                break  
        break
    #Finding Actual Slice to Remove: Result = im5
    for y5 in range(0, im.size[1]):
            if y5 == im.size[1] - 1:
                im5.putpixel((startco_ord, y5), (0, 100, 0))
                route.append(startco_ord)
            else:
                if startco_ord == 0:
                    pe5below_middle = pix3[startco_ord, y5 + 1]
                    pe5below_right = pix3[startco_ord + 1, y5 + 1]
                    p5me = pe5below_middle[0]
                    p5re = pe5below_right[0]
                    p5le = -1
                    choice2 = [p5me, p5re]
                    decision2 = min(choice2)
                    
                elif startco_ord == im.size[0] - 1:
                    pe5below_left = pix3[startco_ord - 1, y5 + 1]
                    pe5below_middle = pix3[startco_ord, y5 + 1]
                    p5le = pe5below_left[0]
                    p5me = pe5below_middle[0]
                    p5re = -1
                    choice2 = [p5me, p5le]
                    decision2 = min(choice2)
                    
                else:
                    pe5below_left = pix3[startco_ord - 1, y5 + 1]
                    pe5below_middle = pix3[startco_ord, y5 + 1]
                    pe5below_right = pix3[startco_ord + 1, y5 + 1]
                    p5le = pe5below_left[0]
                    p5me = pe5below_middle[0]
                    p5re = pe5below_right[0]
                    choice2 = [p5me, p5re, p5le]
                    decision2 = min(choice2)

                im5.putpixel((startco_ord, y5), (0, 100, 0))
                if decision2 == p5me:
                    startco_ord = startco_ord 
                    route.append(startco_ord)
                elif decision2 == p5le:
                    startco_ord = startco_ord - 1
                    route.append(startco_ord)
                elif decision2 == p5re:
                    startco_ord = startco_ord + 1
                    route.append(startco_ord)
    im5.show()

    
    
    #Editing Original Image: Result = im
    for y8 in range(0, im.size[1]):
        for x8 in range(0, im.size[0]):
            if x8 == im.size[0] - 1:
                im.putpixel((x8, y8), (0, 100, 0))
            elif x8 > route[y8]:
                shift = pix[x8 + 1, y8]
                im.putpixel((x8, y8), shift)
            elif x8 < route[y8]:
                continue
    
    a = numpy.array(im)
    b = numpy.delete(a, -1, axis=1)
    im = Image.fromarray(b)





im.show()
