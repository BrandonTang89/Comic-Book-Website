from flask import *
import os
import re
from math import ceil

#Variables
file_directory = "static/files"
files_per_page = 10

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
        page = int(request.form['page'])
    
    filenames = []
    filepics = []
    for filename in os.listdir(file_directory):
        comic = os.listdir(file_directory+"/"+filename)
        comic.sort()                                                #Sort to ensure the pages are displayed in the right order
        comic.remove("data.txt")                                    #remove data file from pages of comic

        with open (file_directory+"/"+filename+"/data.txt") as data:#opening data.txt
            tags = [line.rstrip() for line in data]                 #tags in a list, one on each line; removing trailing whitespace
        date = int(tags[0])                                         #date of the comic in the first line
                    
        filenames.append(((filename,comic[0]),date))

    def sortfn(element):
            return element[1]
        
    filenames.sort(key=sortfn, reverse=True)                        #sort by newest to oldest
    filenames = [filename[0] for filename in filenames]
    
    total_pages= ceil(len(filenames)/files_per_page)
    if page > total_pages or page < 1:
        page=1
    
    filenames= filenames[files_per_page*(page-1):files_per_page*(page)]
    total_files = len(filenames)
    try:
        return render_template('files.html', filenames=filenames, total_files=total_files, current_page=page, total_pages=total_pages)
    except:
        return redirect('/files')

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
            no_of_pages = len(os.listdir(filepath))
            
            if pageno < 1:
                raise "page number out of range"
       
            return render_template("file.html", pageno=pageno, filename=filename,pagename=pagename, no_of_pages=no_of_pages)
        except:
            return redirect('/files')

#Page for search
@app.route('/search', methods=['POST', 'GET'])
def search():
    if request.method == 'GET':
        return redirect("/files")
    else:
        search = request.form['search']     #Search stores the search phrase
        try:
            page = int(request.form['page'])        
        except:
            #go to first page if new search
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
                    
            if search in tags or search.lower() in filename.lower():
                filenames.append(((filename,comic[0]),date))

        def sortfn(element):
            return element[1]
        
        filenames.sort(key=sortfn, reverse=True)                        #sort by newest to oldest
        filenames = [filename[0] for filename in filenames]
        
        total_pages= ceil(len(filenames)/files_per_page)
        total_files = len(filenames)
        filenames = filenames= filenames[files_per_page*(page-1):files_per_page*(page)]
        
        
        return render_template('search.html', filenames=filenames, total_files=total_files, search=search, current_page=page,  total_pages = total_pages)
                               
