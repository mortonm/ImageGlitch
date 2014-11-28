#Image Glitch is a program that is designed to make glitch art. It glitches an image by
# sorting the blue value of pixels in each column. 
# This program was designed as an introduction to Python for beginners, and is not 
# meant to be efficient. 
# Because it is inefficient, please use small filesizes with this algorithm.
#
#author: Margo Morton
#version: 11/26/2014


def imageGlitch():
  #display filepicker, get chosen image
  filename=pickAFile()
  pic=makePicture(filename)
  
  #display image
  show(pic)
  
  #sort rows of pixels by blue value to get distortion effect
  height=getHeight(pic)
  width=getWidth(pic)
  
  for x in range(0,width):
    array = []
    for y in range(0,height):
      p=getPixel(pic,x,y)
      #make an array of all pixels in a column
      array.append(p)
    #for each row, sort the corresponding pixel column  
    array = sortBlue(array, height)
    #update the pixel ordering
    for y in range(0,height):
      p=getPixel(pic,x,y)
      pixColor = makeColor(getRed(array[y]), getGreen(array[y]), getBlue(array[y]))
      setColor(p, pixColor)
    
  #update display
  repaint(pic)
  
#sortBlue is a bubblesort algorithm (inefficient, but easy to understand) that 
#  sorts arrays of pixels based on blue value.
def sortBlue(array, length):
  length = length-1
  sorted = false
  
  while not sorted:
    sorted = true
    for i in range(length):
      #sort pixels in order of decreasing blue-ness
      if getBlue(array[i]) < getBlue(array[i+1]):
        sorted = false
        #swap two pixels if the former has less blue than the latter
        array[i], array[i+1] = array [i+1], array[i]
  #returns sorted pixel array
  return array
