# PYMIR

Music Information Retrieval Experimentation Framework Based on Python.

## What this Project is About?

This project is a Music Information Retrieval (MIR) experimentation framework that
has been built to run machine learning experiments for automatic detection
of keys in songs.

It uses the [musicNet dataset](https://homes.cs.washington.edu/~thickstn/musicnet.html)
wich is  a collection of 330 freely-licensed classical music recordings,
together with over 1 million annotated labels indicating the precise time of each note for every
recording, the instrument that plays each note, and the note's position in the metrical
structure of the composition.


## Instalation

This application is meant to run inside a virtual machine. Therefore, you can use any operative
system. All you need to do is to install [Virtual Box](https://www.virtualbox.org/wiki/Downloads) and [Vagrant](https://www.vagrantup.com/downloads.html).

Be aware that the virtual machine requires 8GB of RAM because the musicnet dataset is huge (11 GB).


## Initalizing Vagrant Machine

The following command will install a linux virtual machine with all required dependencies in place:


```
vagrant plugin install vagrant-vbguest
vagrant up

```

## Downloading the Musicnet Dataset

This dataset is too big to upload it to github (11GB). The following command will download the dataset
and will store it in the data directory of the virtual machine:


```
vagrant up
vagrant ssh
/project/code/scripts/download_musicnet.sh
```


## Information About the Key for Songs

Original metadata for musicnet dataset does not containt the key for each some, thereore, a new metadata
file was generated with they key annotations added manually for each song, this metadata file can be found
in the folder *data/musicnet/musicnet_metadata.csv*



## Transforming the Musicnet Dataset for Sequence of Notes Representation

Some of the experiments use the sequence of notes representation, which representens every song with a label
(key) and the sequence of notes as letters from A to G, the following table shows 3 examples of this 
representation:

Key   |  Notes
------|-----------------------------------------------------------------
A+    | E E E C C A# A# E E E C# G# A D A F# F# E G A C# E G C# C
C+    | G# D D G A# C G F# E G# D G# C# F F A# C# F# F# F F F A# F# C#
B+    | E E E C C B# B# E E E C# G# B D B F# F# E G B C# E G C# C


In order to transform the musicnet dataset to the respresentation mentioned above, the following command
must be executed:

```
vagrant up
vagrant ssh
cd /project/code/python
python3 manage.py format_sequence_representation

```

The musicnet dataset in the sequence of notes represation is stored in the directory *data/musicnet/representations/sequence_of_notes*


### Splitting the Musicnet Dataset, Sequence of Notes Representation, Into Train and Test Sets

There some keys that have more representation than others in the dataset, this means the dataset is umbalanced. If
we generate a random split train/test it is possible to generate a train or test set with not enough examples for some
labels. To avoid that the following command can be used, it generates a split/test by key and then it merges all the data
in order to create a test of 20% and train set of 80%:

```
vagrant up
vagrant ssh
cd /project/code/python
python3 manage.py split_musicnet_sequence_representation --train_size 0.9

```

The test and train datasets are created in the directory *data/musicnet/representations/sequence_of_notes*


### Transforming MusicNet Dataset Sequence of Notes Representation Into Multiple Binary Classification Problems for SEQL Sequence Learner

Automatic key detection is a classification problem with multiple classes (i.e, keys). SEQL Sequency Learner has
been designed to deal with binary classification, for this reason
we transform the Musicnet dataset in order to generate 24 binary datasets, one for every key. For example
If we have 3 songs with different key:

Key   |  Notes
------|-----------------------------------------------------------------------
A+    | E E E C C A# A# E E E C# G# A D A F# F# E G A C# E G C# C
C+    | G# D D G A# C G F# E G# D G# C# F F A# C# F# F# F F F A# F# C#
B+    | E E E C C B# B# E E E C# G# B D B F# F# E G B C# E G C# C


We need to generate 3 datasets, each dataset will use +1 for positive examples and -1 for negative examples:

Key   |  Notes
------|---------------------------------------------------------------------
+1    | E E E C C A# A# E E E C# G# A D A F# F# E G A C# E G C# C
-1    | G# D D G A# C G F# E G# D G# C# F F A# C# F# F# F F F A# F# C#
-1    | E E E C C B# B# E E E C# G# B D B F# F# E G B C# E G C# C



In order to transform the musicnet dataset the following command must be used:

```

vagrant up
vagrant ssh
cd /project/code/python
python3 manage.py format_musicnet_sequence_representation_seql

```

## Transforming the Musicnet Dataset for Time Series, Time Domain Representation

Some of the experiments use the time series, time domain representation, which represetns every song with a label
(key) and the time series of the samples, the following table shows 3 examples of this 
representation:

Key   |  Notes
------|------------------------------------------------------------------------------------------------------------------------
A+    | 241 2084 3136 4178 5218 6263 7303 8335 9365 10390 11416 12446 13473 14503 15531 16557 17584
C+    | 240 2077 3108 4143 5178 6208 7242 8279 9307 10336 11366 12401 13432 14466 15492 16517 17550 18577
B+    | 258 2114 3194 4252 5296 6334 7383 8427 9485 10523 11566 12591 13625 14661 15688 16716 17740 18764 19791


In order to transform the musicnet dataset to the representation mentioned above, the following command
must be executed:

```
vagrant up
vagrant ssh
cd /project/code/python
python3 manage.py format_musicnet_time_series_representation --resample_size=1024

```

Time series data is too long, the --resample_size parameter, generates a smaller dataset taking one sample every --resample_size samples

The musicnet dataset in the time series representation is stored in the directory *data/musicnet/representations/time_series/time_domain*


### Splitting the Musicnet Dataset, Time Series, Time Domain Representation, Into Train and Test Sets

There some keys that have more representation than others in the dataset, this means the dataset is umbalanced. If
we generate a random split train/test it is possible to generate a train or test set with not enough examples for some
labels. To avoid that the following command can be used, it generates a split/test by key and then it merges all the data
in order to create a test of 20% and train set of 80%:

```
vagrant up
vagrant ssh
cd /project/code/python
python3 manage.py split_musicnet_time_series_representation --train_size 0.8

```

### Transforming MusicNet Dataset Time Series, Time Domain Representation Into Multiple Binary Classification Problems for SAX-SEQL Sequence Learner

Automatic key detection is a classification problem with multiple classes (i.e, keys). SEQL Sequency Learner has
been designed to deal with binary classification, for this reason
we transform the Musicnet dataset in order to generate 24 binary datasets, one for every key. For example
If we have 3 songs with different key:

Key   |  Notes
------|------------------------------------------------------------------------------------------------------------------------
A+    | 0.125671386719 -0.110504150391 -0.0445556640625 0.182922363281 -0.143768310547 -0.213714599609 0.138580322266
C+    | -0.00314331054688 -0.0169372558594 0.00762939453125 -0.00662231445312 0.024658203125 0.0107727050781 -0.0247497558594 -0.00518798828125 -0.0167846679688 -0.0158996582031
B+    | 0.0140686035156 0.0105285644531 -0.00982666015625 -0.0096435546875 -0.0159606933594 0.000518798828125 0.0143432617188 0.0160217285156 0.0105285644531


We need to generate 3 datasets, each dataset will use +1 for positive examples and -1 for negative examples:

Key   |  Notes
------|------------------------------------------------------------------------------------------------------------------------
+1    | 0.125671386719 -0.110504150391 -0.0445556640625 0.182922363281 -0.143768310547 -0.213714599609 0.138580322266
-1    | -0.00314331054688 -0.0169372558594 0.00762939453125 -0.00662231445312 0.024658203125 0.0107727050781 -0.0247497558594 -0.00518798828125 -0.0167846679688 -0.0158996582031
-1    | 0.0140686035156 0.0105285644531 -0.00982666015625 -0.0096435546875 -0.0159606933594 0.000518798828125 0.0143432617188 0.0160217285156 0.0105285644531




In order to transform the musicnet dataset the following command must be used:

```

vagrant up
vagrant ssh
cd /project/code/python
python3 manage.py  format_musicnet_time_series_representation_sax_seql --test_dataset /project/data/musicnet/representations/time_series/time_domain/musicnet_test.csv  --train_dataset /project/data/musicnet/representations/time_series/time_domain/musicnet_train.csv


```

## Transforming the Musicnet Dataset for Time Series, Frequency Domain Representation

Some of the experiments use the time series, frequency domain representation, which represetns every song with a label
(key) and the time series that represents the fourier trasnform, the following table shows 3 examples of this 
representation:

Key   |  Notes
------|------------------------------------------------------------------------------------------------------------------------
A+    | 241 2084 3136 4178 5218 6263 7303 8335 9365 10390 11416 12446 13473 14503 15531 16557 17584
C+    | 240 2077 3108 4143 5178 6208 7242 8279 9307 10336 11366 12401 13432 14466 15492 16517 17550 18577
B+    | 258 2114 3194 4252 5296 6334 7383 8427 9485 10523 11566 12591 13625 14661 15688 16716 17740 18764 19791


In order to transform the musicnet dataset to the representation mentioned above, the following command
must be executed:

```
vagrant up
vagrant ssh
cd /project/code/python
python3 manage.py format_musicnet_time_series_frequency_representation --window_size=512

```


### Splitting the Musicnet Dataset, Time Series, Frequency Domain Representation, Into Train and Test Sets

```
vagrant up
vagrant ssh
cd /project/code/python
python3 manage.py split_musicnet_time_series_frequency_representation --train_size 0.9

```

### Transforming MusicNet Dataset Time Series, Frequency Domain Representation Into Multiple Binary Classification Problems for SAX-SEQL Sequence Learner

```

vagrant up
vagrant ssh
cd /project/code/python
python3 manage.py  format_musicnet_time_series_frequency_representation_sax_seql --test_dataset /project/data/musicnet/representations/time_series/frequency_domain/musicnet_test.csv  --train_dataset /project/data/musicnet/representations/time_series/frequency_domain/musicnet_train.csv


```





## Machine Learning Models for Sequence of Notes Representation


### Baseline Model Based on Random Forest

The first baseline model for sequence of notes is based on random forest, it can be executed with
the following command:

```

vagrant up
vagrant ssh
cd /project/code/python
python3 manage.py random_forest_sequence_notes_representation --n_estimators 200 --ngram_size 5
```

### Baseline Model Based on KNN

The second baseline model for sequence of notes is based on KNN, it can be executed with
the following command:

```

vagrant up
vagrant ssh
cd /project/code/python
python3 manage.py knn_sequence_notes_representation --k 1 --ngram_size 5
```


### SEQL Model with Default Parameters

The following script will execute SEQL Learner with defatul parameters:

```

vagrant up
vagrant ssh
 /project/code/scripts/run_seql_default.sh
```


### SEQL Model with Custom Parameters

```
vagrant up
vagrant ssh
/project/code/scripts/run_seql_custom.sh
```

## Machine Learning Models for Time Series, Time Domain Representation


### Baseline Model Based on KNN and Euclidean Distances

### SAX-SEQL Model with Default Parameters

The following script will execute SEQL Learner with defatul parameters:

```

vagrant up
vagrant ssh
 /project/code/scripts/run_sax_seql_time_domain_default.sh
```




## Citations

This framework is released as open software, nevertheless, if you plan to use it to support your research,
please make a reference to our work ** An Empirical Analysis of Machine Learning Techniques for Automatic Key Detection of Songs **


## External Resources

* [MusicNet Dataset](https://homes.cs.washington.edu/~thickstn/musicnet.html)

* [Python](https://www.python.org/)

* [Scilab](http://www.scilab.org/)

* [SciKit Learn](http://scikit-learn.org)

* [SEQL Sequence Learner](https://github.com/heerme/seql-sequence-learner)

* [SAX SEQL Sequence Learner](https://github.com/lnthach/SAX-SEQL)

* [Vagrant](https://www.vagrantup.com/)
