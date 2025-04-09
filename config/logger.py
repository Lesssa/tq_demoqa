import inspect
import logging
import os


class Logger:
    __loggers = {}

    @classmethod
    def __setup_logger(cls, name: str) -> logging.Logger:
        if name in cls.__loggers:
            raise RuntimeError(f"Logger '{name}' is already set up")

        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)

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
        stream_handler.setLevel(logging.WARNING)

        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)

        return logger

    @classmethod
    def __get_logger(cls) -> logging.Logger:
        caller_name = cls.__get_caller_name()
        if caller_name not in cls.__loggers:
            cls.__loggers[caller_name] = cls.__setup_logger(caller_name)
        return cls.__loggers[caller_name]

    @staticmethod
    def __get_caller_name() -> str:
        for frame_info in inspect.stack():
            frame = frame_info.frame
            if 'self' in frame.f_locals:
                return frame.f_locals['self'].__class__.__name__
        module = inspect.getmodule(inspect.stack()[2].frame)
        return module.__name__ if module else "default"

    @classmethod
    def info(cls, msg, *args, **kwargs):
        cls.__get_logger().info(msg, *args, **kwargs)

    @classmethod
    def debug(cls, msg, *args, **kwargs):
        cls.__get_logger().debug(msg, *args, **kwargs)

    @classmethod
    def warning(cls, msg, *args, **kwargs):
        cls.__get_logger().warning(msg, *args, **kwargs)

    @classmethod
    def error(cls, msg, *args, **kwargs):
        cls.__get_logger().error(msg, *args, **kwargs)

    @classmethod
    def critical(cls, msg, *args, **kwargs):
        cls.__get_logger().critical(msg, *args, **kwargs)
