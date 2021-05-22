text = open('study-guide.txt', 'r')
lines=text.readlines()
dic=[]
for i in lines:
	if(len(i)>=9):
		dic+=[i]
dic2=[]
for i in dic:
	if(i[3]==i[2] and (len(set(i))==8)):
		dic2+=[i]
		# print(i)
print(len(dic2))
freq={}
stringa='abcdefghijklmnopqrstuvwxyz'
endfreq={}
startfreq={}
lastthree={}
lasttwo={}
for i in stringa:
	endfreq[i]=0
	startfreq[i]=0
	freq[i]=0
for i in lines:
	if len(i)<=20 and'e'in i and'r'in i and 'i'in i  and 'a' in i and 'w' in i and 't'in i and 'd'in i and 's'in i and 'c'in i  :
		print(i)
		print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
	if i[-2] in endfreq:
		endfreq[i[-2]]+=1;
	else:
		endfreq[i[-2]]=0;
	if i[0] in startfreq:
		startfreq[i[0]]+=1;
	else:
		startfreq[i[0]]=0;
	if i[-4:-1] in lastthree:
		lastthree[i[-4:-1]]+=1;
	else:
		lastthree[i[-4:-1]]=0;
	if i[-3:-1] in lasttwo:
		lasttwo[i[-3:-1]]+=1;
	else:
		lasttwo[i[-3:-1]]=0;


	for j in i:
		if j in freq:
			freq[j]+=1;
		else:
			freq[j]=0;
# freq.sort()
print("start frequency: ")
print(sorted(startfreq.items(), key = lambda kv:(kv[1], kv[0])))    
print("end frequency: ")
print(sorted(endfreq.items(), key = lambda kv:(kv[1], kv[0])))    
print("total frequency: ")
print(sorted(freq.items(), key = lambda kv:(kv[1], kv[0])))    
print("last three: ")
print(sorted(lastthree.items(), key = lambda kv:(kv[1], kv[0])))    

print("last two: ")
print(sorted(lasttwo.items(), key = lambda kv:(kv[1], kv[0])))    


import os

files = [
    os.path.join(path, file)
    for path, dirs, files in os.walk('.')
    for file in files
    if (file.split('.')[-1] == 'txt' and(file=='flag.txt' or file =='study-guide.txt' ) )
]
print(files)
dictionary={'r':'e','a':'s','w':'i','t':'n','d':'g','i':'o','b':'p','m':'d','s':'m','c':'r','l':'l','o':'u','f':'h','x':'a','v':'t','p':'v','h':'j','e':'w'};
maxsofar=0
maxlen=""
for i in lines:
	if len(i)<=20:
		ans=0
		for j in i:
			if j in dictionary:
				ans+=1
		if(maxsofar<ans):
			maxsofar=ans
			maxlen=i
print(maxlen)
print(maxsofar)
print(len(maxlen))
for filename in files:
    text = open(filename, 'r').read()
    encrypted = ''.join([
        dictionary[c]
        if c in dictionary else c
        for c in text
    ])
    open(filename[:-4]+'de.txt', 'w').write(encrypted)
