from invoke import task
from path import Path


@task
def notebook(ctx, spark_home=Path.getcwd() / 'bin/spark'):
    """Launch jupyter notebook to edit notebook files."""
    cmd = ['jupyter notebook']
    ctx.run('{}'.format(' '.join(cmd)), env={'SPARK_HOME': spark_home})
