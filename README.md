# Pyspark tutorial

Welcome to the Pyspark tutorial section.

The courses comprises of 4 folders containing notebooks. Folders and notebooks are sorted in order of difficulty given their name, so you should follow the numerotation. For example, you should finish all notebooks in `1-beginner` before starting `2-novice`. Likewise, when doing `2-novice` finish the `1-...` notebook before doing `2-...`.

Inside each notebook, we have documented a number of questions and unimplemented code cells answering the question, followed by a code cell which acts as test cases for the function called `Graded cell`. Your submission will be graded on how many test cases you pass given your implementation of the previous function. 

**PS**: The instructor has hidden test cases on his side so don't try to circumvent the system by just returning the expected value in your method.

## Prerequisites

- [Anaconda 2019+](https://www.anaconda.com/download/)
- Required Java 8/11. 
    - You can set the `JAVA_HOME` environment variable to point to the Java 8/11 folder you want to use for the project, from `Edit the system environment variables` window or `set JAVA_HOME=<path_to_java>` in command-line before running `jupyter notebook`. 
    - You may also install Java OpenJDK **inside** your Anaconda environment with `conda install openjdk`. The `JAVA_HOME` variable should be automatically updated for this environment only.

## Run

We provide you with a `requirements.txt` which is used to download dependencies in a conda environment we will name `pyspark-tutorial`.

#### Using Anaconda Navigator

Go to `Environments` tab then tap `Import` button. Name it `pyspark-tutorial`. In the dropdown type of file select `Pip requirement file .txt` and browse to the `requirements.txt` file and press enter to create the environment. You should now be able to select the environment.

Go to `Environments` tab, select the `pyspark-tutorial` environment. When your mouse is over the environment, you should see a green arrow, click on it and select `Open with Jupyter notebook`. Then browse to the folder with all the notebooks.

- you may need to define the `PYSPARK_PYTHON` environment variable so Spark workers can point to the correct Python command.

#### Using Anaconda prompt

Create Environment:

```sh
conda create -n pyspark-tutorial python=3.8
conda activate pyspark-tutorial
pip install -r requirements.txt
# pip install bokeh jupyter numpy pandas psutil pyspark seaborn
```

Run Notebook:

```sh
set PYSPARK_PYTHON=python
jupyter lab
```

Run a JupyterLab session : `jupyter lab` from the root of your project, when in your `pyspark-tutorial` conda environment.

Notes: 
- you may run into `java.io.FileNotFoundException: HADOOP_HOME and hadoop.home.dir are unset.` warnings on Windows. Do not worry about it, they are necessary for remote connections only.
- you may need to define the `PYSPARK_PYTHON` environment variable so Spark workers can point to the correct Python command.

When you are done with the environment, don't forget to deactivate your Anaconda environment : `conda deactivate`

## Submit

At the end of the course, send your assignments by email to the instructor.

**BEFORE SENDING:**

- Check that your Jupyter notebook runs from start to finish when you run it from top to bottom, using `Kernel > Restart & Run All`. Clean up all unecessary cells. Your grade is based on how far the execution of the notebook goes from top to bottom without me going in.
- Don't rename the files, and preserve the folder structure when sending the zipped project, even if you did not complete the notebook. It should look like:

```
├── 1-beginner
│   └── 1-Initiation.ipynb
├── 2-novice
│   ├── FL_insurance.csv
│   ├── 1-Initiation-RDD.ipynb
│   └── 2-Pagerank-RDD.ipynb
└── 3-advanced
    ├── FL_insurance.csv
    ├── titanic.csv
    ├── 1-Initiation-SparkSQL.ipynb
    └── 2-Advanced-SQL-and-ML.ipynb
```

# Contributing guide

This repo is generated from a private [nbgrader](https://nbgrader.readthedocs.io) project with the solutions to the problems, which I use to autograde the students solutions.

You may create a pull request with the change in the notebook so I copy-paste it in the private repo and overwrite the files. It is normal if I close and don't merge your PR while overwriting the file with your change. Hopefully I find a better way to regenerate the release folder.
