from prefect import flow, get_run_logger

TESTING = 'hello'

@flow
def my_docker_flow():
    logger = get_run_logger()
    logger.info(f"Hello from Docker!, the variable is {TESTING}")
