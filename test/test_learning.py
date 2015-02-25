from marker import Marker
import random

learn=Marker()
learn.load()
x={"speed":0,"sentenceSpeed":0}
i=0
while i<10:
    x["speed"]=random.random()*5+3
    x["sentenceSpeed"]=random.random()*3/15
    i+=1
    y0,y1=learn.cal_score(x)
    print (str(x["speed"])+"word/s : score"+str(y0*100))
    print (str(x["sentenceSpeed"])+"space/s : score"+str(y1*100))