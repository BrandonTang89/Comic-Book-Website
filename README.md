# Comic-Book-Website
A sample website for viewing web comics
<ul>
  <li>Uses python flask as a back-end</li>
  <li>Uses semantic UI as HTML framework</li>
</ul>

<b>Dependencies</b>
<ul>
  <li>Python 3.7+</li>
  <li>pytz python library</li>
  <li>flask python library</li>
  <li>gunicorn3 (for deployment on linux machines)</li>
</ul>

<b>Installing python libraries</b>
<pre>pip3 install flask pytz</pre>
<i>Use 'pip' instead of pip3 for windows</i>

<b>Installing gunicorn</b>
<pre>sudo apt-get install gunicorn3</pre>

<b>Instructions for use</b>
<ul>
  <li>Comics come as directories with jpgs and a data file containing "tags" for that comic (first tag is the release date)</li>
  <li>Comics go in the 'static/files' folder</li>
  <li>Start the server with 'run application.cmd" or "run.sh" for development</li>
  <li>Start the server with 'pro.sh' for actual deployment (only for unix-based OS)</li>
  <li>Go to localhost:5000 to view website</li>
</ul>

<b>Logging</b><br>
Searchs are logged in 'searches.txt'. <br>
Format:
<pre>[Search Term], [Public IP], [YYYY-MM-DD] [HH-MM-SS]</pre>

<b>Comic File Format</b><br>
<ul>
  <li>Comics are directories containing images in jpg format.</li>
  <li>Images are displayed in lexicographical order.</li>
  <li>Each comic directory has a 'data.txt' file to store tags associated with the comic.</li>
  <li>The first tag always has to be the date of release (in YYYYMMDD).</li>
  <li>Some tags label the comic as being of restricted access and are thus hidden unless such tags are searched for (read the code to figure out more).</li>
</ul>
  
<b><i>Note: Only a few sample comics have been placed here. If you want to try the website with more comics, find more on your own.</i></b>
