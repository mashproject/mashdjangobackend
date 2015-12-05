from celery.task import task


@task
def do_something_with_form_data(data):
    pass
