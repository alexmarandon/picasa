import json
import re
import sqlite3

conn = sqlite3.connect('picasadb.sqlite')
cur = conn.cursor()


with open('picasa.ini.json') as data_file:    
    data = json.load(data_file)

unique_header = list()
unique_album_ids = list()
unique_contacts = list()
albums = list()
starredfiles = list()
file_albums = list()
file_faces = list()
contacts = list()
for row in data:
	if re.search('album', row['header'], re.IGNORECASE) and re.search('name', row['action'], re.IGNORECASE): 
		ID = row['header'].split(':')[1]
		name = row['action'].split('=')[1]
		if ID not in unique_album_ids:
			#print "Album ID & Name:",ID, name
			album = dict()
			album['id'] = ID
			album['name'] = name
			unique_album_ids.append(ID)
			albums.append(album)
		
	if re.search('Contacts2', row['header'], re.IGNORECASE): 
		id = row['action'].split('=')[0]
		name = row['action'].split('=')[1].split(';')[0]
		#print row['action']
		if id not in unique_contacts:
			print "Contact ID & Name:",id, name
			contact = dict()
			contact['id'] = id
			contact['name'] = name
			unique_contacts.append(id)
			contacts.append(contact)
	
		
	elif re.search('jpe*g', row['header'], re.IGNORECASE) and re.search('star=yes', row['action'], re.IGNORECASE):
		#print "Starred File:", row['year'], row['folder'], row['header']
		starred = dict()
		starred['file'] = row['header']
		starred['folder'] = row['folder']
		starred['year'] = row['year']
		starredfiles.append(starred)
	
	elif re.search('jpe*g', row['header'], re.IGNORECASE) and re.search('albums', row['action'], re.IGNORECASE):
		ids = row['action'].split('=')[1].split(',')
		for id in ids:
			#print row['year'], row['folder'], row['header'], id
			file_album = dict()
			file_album['file'] = row['header']
			file_album['folder'] = row['folder']
			file_album['year'] = row['year']
			file_album['id'] = id
			file_albums.append(file_album)
	
	elif re.search('jpe*g', row['header'], re.IGNORECASE) and re.search('faces', row['action'], re.IGNORECASE):
		faces = row['action'].split('=')[1].split(';')
		#print faces
		for face in faces:
			#print row['year'], row['folder'], row['header'], face.split(',')[1]
			file_face = dict()
			file_face['file'] = row['header']
			file_face['folder'] = row['folder']
			file_face['year'] = row['year']
			file_face['id'] = face.split(',')[1]
		
	elif not re.search('backuphash|date|token|redo|iidlist|rotate|filters|crop|faces', row['action'], re.IGNORECASE) and not re.search('picasa|encoding|album|contacts', row['header'], re.IGNORECASE) and not re.search('originals', row['file'], re.IGNORECASE):
		print row['header'], row['action']
		#print "Shouldn't be here"
		
		
