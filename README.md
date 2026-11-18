# Pyspark tutorial

Welcome to the Pyspark tutorial section.

The courses comprises of 4 folders containing notebooks. Folders and notebooks are sorted in order of difficulty given their name, so you should follow the numerotation. For example, you should finish all notebooks in `1-beginner` before starting `2-novice`. Likewise, when doing `2-novice` finish the `1-...` notebook before doing `2-...`.

Inside each notebook, we have documented a number of questions and unimplemented code cells answering the question, followed by a code cell which acts as test cases for the function called `Graded cell`. Your submission will be graded on how many test cases you pass given your implementation of the previous function. 

**PS**: The instructor has hidden test cases on his side so don't try to circumvent the system by just returning the expected value in your method.

## Setup

Follow the [Spark tutorial setup](https://andfanilo.github.io/lyon2/spark/). It shows how to install Java 17 or 21 and set `JAVA_HOME`, install the environment with `uv sync`, and open the notebooks in JupyterLab or VS Code.

In short, once Java is installed:

```sh
uv sync
uv run jupyter lab
```

You don't need to install Python or set `PYSPARK_PYTHON`. `uv` downloads the Python version in `pyproject.toml`, and the Spark setup cell at the top of each notebook sets `PYSPARK_PYTHON` for you. Always run that cell first.

> **Note on the Python version:** this project is pinned to Python 3.10. On Windows, PySpark's Python worker crashes on Python 3.11 and above when an RDD is only partially read (`take()`, `first()`, and the MLlib exercise in `3-advanced`). `uv` enforces the pin, so don't override it.

### Run it in Docker instead

Run the tutorial in a Docker container:

```sh
docker run -it --rm -p 8888:8888 -p 4040:4040 -v "[path_to_your_tutorial_folder]:/home/jovyan/work" jupyter/pyspark-notebook
```

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
