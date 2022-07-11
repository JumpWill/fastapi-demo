import os

from loguru import logger
from ..conf import settings


class Logger:
    @staticmethod
    def log() -> logger:
        if not os.path.exists(settings.LogPath):
            os.mkdir(settings.LogPath)

        # 日志文件
        log_file = os.path.join(settings.LogPath, "FastAutoTest.log")
        logger.add(
            log_file,
            encoding='utf-8',
            level="DEBUG",
            rotation='00:00',  # 每天 0 点创建一个新日志文件
            retention="7 days",  # 定时自动清理文件
            enqueue=True,  # 异步安全
            backtrace=True,  # 错误跟踪
            diagnose=True,
        )

        return logger


logger = Logger.log()
