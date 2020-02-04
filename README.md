# Pyspark tutorial

Welcome to the Pyspark tutorial section.

The courses comprises of 4 folders containing notebooks. Folders and notebooks are sorted in order of difficulty given their name, so you should follow the numerotation. For example, you should finish all notebooks in `1-beginner` before starting `2-novice`. Likewise, when doing `2-novice` finish the `1-...` notebook before doing `2-...`.

Inside each notebook, we have documented a number of questions and unimplemented code cells answering the question, followed by a code cell which acts as test cases for the function called `Graded cell`. Your submission will be graded on how many test cases you pass given your implementation of the previous function. Be careful as the instructor has hidden test cases on his side so don't try to circumvent the system by just returning the expected value, and learn nothing.

## Prerequisites

- [Anaconda 2019+](https://www.anaconda.com/download/)
- Java 8. You may experience difficulties with Java 9. You can set the `JAVA_HOME` environment variable to point to the Java folder you want to use for the project. You may also install Java JDK 8 **inside** your Anaconda environment with `conda install -c cyclus java-jdk`.

## Run

We provide you with a `requirements.txt` which is used to download dependencies in a conda environment we will name `pyspark-tutorial`.

#### Using Anaconda Navigator

Go to `Environments` tab then tap `Import` button. Name it `pyspark-tutorial`. In the dropdown type of file select `Pip requirement file .txt` and browse to the `requirements.txt` file and press enter to create the environment. You should now be able to select the environment.

Go to `Environments` tab, select the `pyspark-tutorial` environment. When your mouse is over the environment, you should see a green arrow, click on it and select `Open with Jupyter notebook`. Then browse to the folder with all the notebooks.

#### Using Anaconda prompt

```
conda create -n pyspark-tutorial python=3.6
conda activate pyspark-tutorial
pip install -r requirements.txt
jupyter notebook
```

Run a Jupyter Notebook session : `jupyter notebook` from the root of your project, when in your `pyspark-tutorial` conda environment.

When you are done with the environment, don't forget to deactivate your Anaconda environment : `conda deactivate`

## Submit

At the end of the course, send your assignments by email to the instructor.

# Contributing guide

This repo is generated from a private [nbgrader](https://nbgrader.readthedocs.io) project with the solutions to the problems, which I use to autograde the students solutions.

You may create a pull request with the change in the notebook so I copy-paste it in the private repo and overwrite the files. It is normal if I close and don't merge your PR while overwriting the file with your change. Hopefully I find a better way to regenerate the release folder.
