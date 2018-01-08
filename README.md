# Pyspark tutorial

Welcome to the Pyspark tutorial section.

The courses comprises of 4 folders containing notebooks. Folders and notebooks are sorted in order of difficulty given their name, so you should follow the numerotation. For example, you should finish all notebooks in `1-beginner` before starting `2-novice`. Likewise, when doing `2-novice` finish the `1-...` notebook before doing `2-...`.

Inside each notebook, we have documented a number of questions and unimplemented code cells answering the question, followed by a code cell which acts as test cases for the function called `Graded cell`. Your submission will be graded on how many test cases you pass given your implementation of the previous function.  Be careful as the instructor has hidden test cases on his side so don't try to circumvent the system by just returning the expected value, and learn nothing.

## Prerequisites 

* Anaconda
* a `bin/spark` folder at the root of your project, containing Spark 2.2.0. The best way to do it is to download the archive from [Spark downloads](https://spark.apache.org/downloads.html) and uncompress it as `bin/spark`.

All the following commands are written with Windows users in mind, Unix/MacOS users should only need to edit Anaconda activation/deactivation by prepending the commands with `source`.

## Install

We provide you with a `environment.yml` which Anaconda can use to create a Python environment named `pyspark-tutorial`.

```
conda env create -f environment.yml
activate pyspark-tutorial
```

## Run

Run a Jupyter Notebook session : `invoke notebook`.

The invoke command will automatically send `bin/spark` as the `SPARK_HOME` environment variable so you need to have downloaded Spark inside `bin/spark` before, which is normally easily done in the previous section. If you wish to change that use the `--spark_home` flag : `invoke notebook -s path/to/spark.`

When you are done with it, don't forget to deactivate your Anaconda environment : `deactivate`

## Submit

At the end of the course, send your assignemnts by email to the instructor. 

