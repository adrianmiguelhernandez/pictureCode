def picture():
    file = pickAFile()
    picture= makePicture(file)
    array = getPixels(picture)
    height = getHeight(picture)
    width = getWidth(picture)
    print "This picture has a height of ", (height)
    print "Thus picture has a width of ", (width)
    
    repaint (picture)