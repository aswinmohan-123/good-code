/*modified on Jul 25, 2018*/
class can:
    def __init__(self, width, height):				//constructor
        self.w = width						//height definig
        self.h = height
        self.d = [[' '] * width for i in range(height)]		
    def sp(self, r, c):
        self.d[r][c] = '*'
    def gp(self,row, col)
        return self.d[r][c]
    def dis(self):
        print "\n".join(["".join(r) for r in self.d])
class s:
    def p(self,canvas): pass
class rec(s):
    def __init__(self, x, y, w, h)
        self.x = x
        self.y = y self.w = w self.h = h
    def hl(self, x, y, w):  //it was used for horizondal line.
        pass
    /*def vl(self, x, y, h):	//it was used for vertical line.
        pass*/
    def p(self, canvas):
            hline(self.x, self.y, self.w)
      hline(self.x, self.y + self.h, self.w)
        vline(self.x, self.y, self.h)
      	  				vline(self.x + self.w, self.y, self.h)
class squ(rectangle):def __init__(self, x, y, size):rectangle.__init__(self, x, y, size, size)
class cs(s):
    def __init__(self, shapes):
        self.shapes = shapes
    def p(self, canvas):
    for s in self.shapes:
           s.paint(canvas);
sp=s();				//object creation
rect=rec(5,6,8,9);//object creation
sq=squ(6,5,9);//object creation

