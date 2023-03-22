# DE1-Group6
### Welcome to the repository of group 6!

#### How to run docker-compose setup:
1. Go to /docker-setup folder
2. Do <code>docker-compose up –build</code>.
3. Go to localhost/8888 for jupyter, if it’s not there you need to find the port by doing <code>docker-compose ps</code> and look for the jupyter node.

#### Data analys
The files that we used for analyzing are in /data-analysis.

#### Architecture
The /architecture folder contains the files for setting up the MongoDB data storage. 

#### Other
Our first try with figuring out HDF5 file structure are in /HDF5-files. Our old docker-compose file is in /spark-original and our try for making separate worker and master is in /separate-worker.
