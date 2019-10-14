import os
from sys import argv

dic = {}

with open (argv[1],'r') as f:
    for line in f:
        line = line.strip().split('\t')
        va = [int(line[1]), int(line[2])]
        if line[0] not in dic:
            dic[line[0]] = [va]
        else:
            dic[line[0]].append(va)
    print(dic)    
r = open(argv[3], 'w')

with open(argv[2]) as f:
    for lineL in f:
        line = lineL.strip().split('\t')
        try:
            pos = dic[line[1]]
        except:
            continue
        for k in pos:
            if int(line[3]) < k[0]:
                distance = k[0]-int(line[3])
                r.write(lineL.strip()+"\t"+"upstream"+"\t"+str(distance)+"\t"+str(k[0])+"\t"+str(k[1])+"\n")
            elif int(line[2]) > k[1]:
                distance = int(line[2])-k[1]
                r.write(lineL.strip()+"\t"+"downstream"+"\t"+str(distance)+"\t"+str(k[0])+"\t"+str(k[1])+"\n")
            elif k[0] < int(line[3]) < k[1] and int(line[2]) < k[0]:
                distance = int(line[3])-k[0]
                r.write(lineL.strip()+"\t"+"upstream_overlap"+"\t"+str(distance)+"\t"+str(k[0])+"\t"+str(k[1])+"\n")
            elif k[1] < int(line[3]) and k[0] < int(line[2]) < k[1]:
                distance = k[1]-int(line[2])
                r.write(lineL.strip()+"\t"+"downstream_overlap"+"\t"+str(distance)+"\t"+str(k[0])+"\t"+str(k[1])+"\n")
            elif k[0] < int(line[3]) < k[1] and k[0] < int(line[2]) < k[1]:
                r.write(lineL.strip()+"\t"+"binggo"+"\t"+"0"+"\t"+str(k[0])+"\t"+str(k[1])+"\n")
        
r.close()