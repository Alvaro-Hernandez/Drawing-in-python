import turtle
from pikachu import *

tt= turtle.Screen()
tt.setup(width=800, height=800)
p = Pikachu()
p.body()
p.cap(-134.07, 147.81)
p.mouth(-5, 25)
p.leftCheek(-126, 32)
p.rightCheek(107, 63)
p.colorLeftEar(-250, 100)
p.colorRightEar(140, 270)
p.leftEye(-85, 90)
p.rightEye(50, 100)
turtle.mainloop()