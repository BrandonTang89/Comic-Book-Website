#!/usr/bin/env python3
from flask import *
import os
import pytz
from datetime import datetime
from math import ceil
import sys
#Variables
file_directory = "static/files"
files_per_page = 12
restricted_tags = ["hentai", "porn"]

#Time settings
tz = pytz.timezone('Asia/Singapore')
fmt = "%Y-%m-%d %H:%M:%S %Z%z"                                      #format for time

##Main
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('home.html')

#About
@app.route('/about')
def about():
    return render_template('about.html')
#Main Files Page
@app.route('/files', methods=['GET', 'POST'])
def files():
    #TERMINOLOGY: "file" --> comic folder, each individual image file is called a page
    if request.method == 'GET':
        page=1
    else:
        try:
            page = int(request.form['page'])
        except:
            page = 1
    
    filenames = []
    filepics = []
    for filename in os.listdir(file_directory):
        comic = os.listdir(file_directory+"/"+filename)
        comic.sort()                                                #Sort to ensure the pages are displayed in the right order
        comic.remove("data.txt")                                    #remove data file from pages of comic

        with open (file_directory+"/"+filename+"/data.txt") as data:#opening data.txt
            tags = [line.rstrip() for line in data]                 #tags in a list, one on each line; removing trailing whitespace
        date = int(tags[0])                                         #date of the comic in the first line

        if any([tag for tag in tags if tag in restricted_tags]):    #Filter
            continue
                    
        filenames.append(((filename,comic[0]),date))

    def sortfn(element):
            return element[1]
        
    filenames.sort(key=sortfn, reverse=True)                        #sort by newest to oldest
    filenames = [filename[0] for filename in filenames]

    total_files = len(filenames)
    total_pages= ceil(total_files/files_per_page)
    if page > total_pages or page < 1:
        page=1

    next_filenames= filenames[files_per_page*(page):files_per_page*(page+1)]
    filenames= filenames[files_per_page*(page-1):files_per_page*(page)]
    
    

    return render_template('files.html', filenames=filenames, total_files=total_files, current_page=page, total_pages=total_pages, next_filenames = next_filenames)
    #except:
     #   return "Error occurred in 'files'"
        #return redirect('/files')

#Page for reading
@app.route('/file', methods=['GET', 'POST'])
def read():
    if request.method == 'get':
        redirect('/file')
    else:
        try:
            filename = request.form['filename']
            filepath = file_directory + "/" + filename
                    
            pageno = int(request.form['pageno'])
            
            #Sort to ensure the pages are displayed in the right order
            comic = os.listdir(filepath)
            comic.sort()
            comic.remove("data.txt") #remove data file from pages of comic
            pagename= comic[pageno -1]
            next_page = comic[pageno]
            no_of_pages = len(comic)
            
            if pageno < 1:
                raise "page number out of range"
       
            return render_template("file.html", pageno=pageno, filename=filename,pagename=pagename, no_of_pages=no_of_pages, next_page=next_page)
        except:
            return redirect('/files')

#Page for search
@app.route('/search', methods=['POST', 'GET'])
def search():
    if request.method == 'GET':
        return redirect("/files")
    else:
        search = request.form['search']     #Search stores the search phrase
        lower = search.lower()
        file = open("searches.txt","a+")
        file.write(search+ "," + request.remote_addr+ "," + datetime.now(tz).strftime(fmt)[:-9] + "\n")

        file.close()
        restricted = False if any([tag for tag in restricted_tags if tag in lower]) else True
        try:
            page = int(request.form['page'])
        except:
            #go to first page if new search
            page = 1
            
        filenames = []
        for filename in os.listdir(file_directory):

            comic = os.listdir(file_directory+"/"+filename)
            comic.sort()                                                #Sort to ensure the pages are displayed in the right order
            comic.remove("data.txt")                                    #remove data file from pages of comic
            
            with open (file_directory+"/"+filename+"/data.txt") as data:#opening data.txt
                tags = [line.rstrip() for line in data]                 #tags in a list, one on each line; removing trailing whitespace
            date = int(tags[0])                                         #date of the comic in the first line
            
            #Choosing whether to add the comic in search
            no_tags = 0
            add = False
            if any([tag for tag in tags if tag in restricted_tags]) and restricted:
                continue
            for tag in tags:
                if tag in lower:
                    no_tags += 1
                    add = True

            search_terms = lower.split()
            if any([match for match in search_terms if match in filename.lower()]):
                add = True
                
            if add:
                filenames.append(((filename,comic[0]),no_tags,date))

        def sortfn(element):
            return element[1]

        filenames.sort()
        filenames.sort(key=lambda filename: filename[2], reverse=True)#sort by date (secondary)
        filenames.sort(key=lambda filename: filename[1], reverse=True)#sort by relevance (primary)
        
        filenames = [filename[0] for filename in filenames]
        
        
        total_pages= ceil(len(filenames)/files_per_page)
        total_files = len(filenames)
        filenames = filenames= filenames[files_per_page*(page-1):files_per_page*(page)]
        
        #return str(filenames)
        return render_template('search.html', filenames=filenames, total_files=total_files, search=search, current_page=page,  total_pages = total_pages)
                               
