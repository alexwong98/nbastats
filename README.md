# nbastats

<p>nbastats is a Flask-based web application that uses D3.js, nvd3.js, py_goldsberry, and nba_py libraries in order to graphically represent NBA player career statistics. pylibmc was used to cache the large amounts of data collected, and pandas was used to organize said data.</p>

Hosted at : http://nbastats-dev.us-east-1.elasticbeanstalk.com/ (note caching may not be working, as I am currently working on implementing the automatic restart of the memcached service everytime it crashes). 
