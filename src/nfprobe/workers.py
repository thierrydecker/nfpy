"""workers module
"""

import inspect
import multiprocessing
import logging
import logging.config


class LoggingWorker(multiprocessing.Process):
    """Logging worker
    """

    def __init__(self, logger, queue):
        super().__init__()
        self.config = logger
        self.queue = queue

    def run(self):
        logging.config.dictConfig(self.config)
        logger = logging.getLogger()

        fn_name = inspect.stack()[0][3] + " " + str(self.name)
        logger.debug(('DEBUG', __name__, fn_name, 'Logging process starts'))

        while True:
            message = self.queue.get()
            if message == None:
                break
            level, module, function, msg = message
            if level == 'DEBUG':
                logger.debug(message)
            elif level == 'INFO':
                logger.info(message)
            elif level == 'WARNING':
                logger.warning(message)
            elif level == 'ERROR':
                logger.error(message)
            elif level == 'CRITICAL':
                logger.critical(message)
            else:
                logger.critical(message)

        logger.debug(('DEBUG', __name__, fn_name, 'Logging process stops'))
