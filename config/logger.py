import logging
import os


class Logger:
    _loggers = {}

    @classmethod
    def get_logger(cls, name=None):
        if name is None:
            name = cls.__get_caller_name()

        if name in cls._loggers:
            return cls._loggers[name]

        logger = logging.getLogger(name)
        logger.setLevel(logging.WARNING)

        formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(name)s - %(message)s'
        )

        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
        log_path = os.path.join(project_root, 'tests', 'test_logs.log')

        file_handler = logging.FileHandler(log_path, encoding="utf-8")
        file_handler.setFormatter(formatter)
        file_handler.setLevel(logging.DEBUG)

        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        stream_handler.setLevel(logging.INFO)

        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)

        cls._loggers[name] = logger
        return logger

    @staticmethod
    def __get_caller_name():
        import inspect
        frame = inspect.stack()[2]
        module = inspect.getmodule(frame[0])
        if module:
            return os.path.splitext(os.path.basename(module.__file__))[0]
        return "default"
