# Pyspark tutorial

Welcome to the Pyspark tutorial section.

The courses comprises of 4 folders containing notebooks. Folders and notebooks are sorted in order of difficulty given their name, so you should follow the numerotation. For example, you should finish all notebooks in `1-beginner` before starting `2-novice`. Likewise, when doing `2-novice` finish the `1-...` notebook before doing `2-...`.

Inside each notebook, we have documented a number of questions and unimplemented code cells answering the question, followed by a code cell which acts as test cases for the function called `Graded cell`. Your submission will be graded on how many test cases you pass given your implementation of the previous function.  Be careful as the instructor has hidden test cases on his side so don't try to circumvent the system by just returning the expected value, and learn nothing.

## Prerequisites 

* [Anaconda 5+](https://www.anaconda.com/download/)
* Java 8. You may experience difficulties with Java 9. You can set the `JAVA_HOME` environment variable to point to the Java folder you want to use for the project. You may also install Java JDK 8 **inside** your Anaconda environment with `conda install -c cyclus java-jdk`.

For those using the command line, all the following commands are written with Windows users in mind, Unix/MacOS users should only need to edit Anaconda activation/deactivation by prepending the commands with `source`.

## Install

We provide you with a `environment.yml` which Anaconda can use to create a Python environment named `pyspark`.

#### Using Anaconda Navigator

Go to `Environments` tab then tap `Import` button. Directly browse to the `environment.yml` file and press enter. You should now be able to select the environment.

#### Using Anaconda prompt

```
conda env create -f environment.yml
activate pyspark
```

## Run

#### Using Anaconda Navigator

Go to `Environments` tab, select the `pyspark` environment. When your mouse is over the environment, you should see a green arrow, click on it and select `Open with Jupyter notebook`. Then browse to the folder with all the notebooks.

#### Using Anaconda prompt

Run a Jupyter Notebook session : `jupyter notebook` from the root of your project, when in your `pyspark` conda environment.

When you are done with the environment, don't forget to deactivate your Anaconda environment : `deactivate`

## Submit

At the end of the course, send your assignemnts by email to the instructor. 

