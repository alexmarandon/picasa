# Import the os module, for the os.walk function
import os
# Import Regexp module
import re

#Import JSON module
import json

# Set the directory you want to start from
rootDir = '/Volumes/nasmedia/photos/master'
datalist = list()
for dirName, subdirList, fileList in os.walk(rootDir):
    #print('Found directory: %s' % dirName)
    for fname in fileList:
        if fname=="Picasa.ini" or fname==".picasa.ini": 
            fullfname = dirName+'/'+fname
            foldername = dirName.split('/')[6]
            year = dirName.split('/')[5]
            #print('processing url: %s' % (dirName, ))
            #print('processing foldername: %s' % (foldername, ))
            #print('processing year: %s' % (year, ))
            print('processing file: %s' % (fullfname, ))
            fhand = open(fullfname)
            header = ''
            for line in fhand:
                line = line.strip()
                if len(line) ==0 : continue
                if line.startswith('[') : 
                    header = line.strip('[] ')
                else : 
                    datarow = dict()
                    action = line
                    datarow['year'] = year
                    datarow['folder'] = foldername
                    datarow['header'] = header
                    datarow['action'] = action
                    datarow['file'] = fullfname
                    #print year, foldername, header, action
                    #print datarow
                    datalist.append(datarow)
                    
#print datalist


with open('picasa.ini.json', 'w') as outfile:
    json.dump(datalist, outfile)