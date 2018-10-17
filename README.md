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
  <li>Start the server with 'pro.sh' for actual deployment</li>
  <li>Go to localhost:5000 to view website</li>
</ul>
