import os
path = os.path.join(os.path.dirname(__file__), "./datatest2.txt")
from marker import Marker

mark=Marker()
mark.load()
with open("learningData.txt") as f:
    line = f.readline()  # skip header
    line = f.readline()
    i=0
    x1=[]
    x2=[]
    y=[]
    while line:
        word=line.split('\t')
        print([float(word[0]),float(word[1])])
        x1.append([float(word[1])])
        x2.append([float(word[2])])
        y.append(float(word[0]))
        #x1.append([float(word[0])])
        #x2.append([float(word[1])])
        #y.append(i%2.0)  # good and bud presents alternately
        line=f.readline()
        i+=1

store_keys=["x1","calculate_x1","x1","y","x2","calculate_x2","x2","y"]

with open(path, "wb") as outfile:
    line = "\t".join([str(v) for v in store_keys])
    outfile.write(line.encode("utf-8"))
    j=0
    analyzed={}
    while(j<=100):
        print(i)
        speed=j*1/10
        sentenceSpeed=j*2/1000
        analyzed["speed"]=float(speed)
        analyzed["sentenceSpeed"]=float(sentenceSpeed)
        cal_x1,cal_x2=mark.cal_score(analyzed)
        line ="\n" + str(speed)+"\t"+ str(cal_x1)
        if(j<i):
            line=line+"\t" + str(x1[j][0])+"\t"+ str(y[j])
        else:
            line=line+"\t"+""+"\t"+""
        line =line+"\t" + str(sentenceSpeed)+"\t"+ str(cal_x2)
        if(j<i):
            line=line+"\t" + str(x2[j][0])+"\t"+ str(y[j])
        outfile.write(line.encode("utf-8"))
        j+=1