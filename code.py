/*
**
*This program is for creating geometrical object.
*The program mainly contain four classes.
*The class sqaure is child class which inherits from rectangle class
*/

class canvas:

    def __init__( self, width, height ):
        self.width = width
        self.height = height
        self.data = [[' '] * width for i in range( height )]    //creating an array of width*height as canvas

    def setpixel( self, row, col ):
        self.data[row][col] = '*'

    def getpixel( self, row, col ) :
        return self.data[row][col]

    def display( self ) :
        print "\n".join(["".join( row ) for row in self.data])

class rectangle():

    def __init__( self, cordinates, width, height ) :
        self.x = cordinates.x
        self.y = cordinates.y
        self.width = width
        self.height = height

class square( rectangle ) :

    def __init__( self, coordinates, size ) :
        rectangle.__init__(self, coordinated.x, coordinates.y, size, size)

class coordinates ( x,y ) :
    self.x=x
    self.y=y

coordinatesObject = coordinates(5,6)
rectangleObject = rectangle(cord,8,9);
squareObject = square(cord,9);

