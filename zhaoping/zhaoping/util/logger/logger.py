import logging
def get_logger(logging=None):
    """
    创建日志实例
    """
    LOG_LEVEL = logging.INFO  # 日志等级
    POOL_MAXSIZE = 8  # 线程池最大容量

    logger = get_logger()
    import logging
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename='/tmp/test.log',
                        filemode='w')
    logger = logging.getLogger("monitor")
    logger.setLevel(LOG_LEVEL)

    ch = logging.StreamHandler()
    logger.addHandler(ch)
    return logger