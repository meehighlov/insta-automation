import signal

from app.browser import chrome
from app.config import config
from app.exceptions import TimeoutAppError
from profile.subscriptions import subscribtions_info


def timeout_handler(signum, frame):
    raise TimeoutAppError()


def launch(*args, **kwargs):
    subscribtions_info(chrome, result_path=config.REPORT_PATH)


if __name__ == '__main__':
    signal.signal(signal.SIGALRM, timeout_handler)
    signal.alarm(config.TIMEOUT_FOR_INSTA_TASK_EXECUTION_SEC)
    launch()
    signal.alarm(0)
