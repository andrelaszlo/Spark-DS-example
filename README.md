# Spark-DS-example
Illustration of how to use Apache Spark to analyse raw data, for MLDS meetup GBG 2015

The example is an attempt to do unsupervised graph clustering of Västtrafik stops using timetable pdfs converted to txt files (stored in timetables.tar.gz). The model is a power iteration graph clustering algorithm. 

![alt tag](https://github.com/jotsif/Spark-DS-example/blob/master/plots/graph.png)

# Running

1) Download apache spark binary suitable for your OS, and R if not installed either. 

Mac OS X example: 

```brew install apache-spark``` 

```brew tap homebrew/science```

```brew install gcc```

```brew install Caskroom/cask/xquartz```

```brew install r```


2a) Optionally create a [virtualenv](https://pypi.python.org/pypi/virtualenv)

```virtualenv env```

```source env/bin/activate```

This will make the next step install all needed Python packages in an isolated environment, not affecting the rest of your system.

2b) Install the required python packaged

```pip install -r requirements.txt```

3a) Create a tmp directory

```mkdir tmp```

3a) Run the following code to execute the spark python script from a terminal:

```spark-submit --driver-memory=6G py/readPdfs.py```

The code automatically extracts the timetable files so no need to do it manually.

This might take a while, since it parses more than 5k files, parses them and trains a model. 

3b)

Download spark binary from spark.apache.org (http://apache.mirrors.spacedump.net/spark/spark-1.5.2/spark-1.5.2-bin-hadoop2.6.tgz) and unpack

```

./sbin/start-master.sh
./sbin/start-slave.sh spark://yourhostname:7077

spark-submit --driver-memory=6G py/readPdfs.py spark://yourhostname:7077

```

This way you can access webui from `yourhostname:8080` and watch progress of the app.



4) Install R libraries 

```R -f R/install_libs.R```

5) Visualise the result and compare PIC with Louvain graph clustering done in R.

```R -f R/plotgraph.R```

Plots saved in plots/ directory.
