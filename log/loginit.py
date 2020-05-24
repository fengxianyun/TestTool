# coding: utf-8
'''
Created on 2020年4月9日

@author: 10226475
'''
import os
import logging
import traceback
import time
from multiprocessing import Process
from log.logprocess import _log_listener_process


class LogInit:
    # 默认日志存储路径（相对于当前文件路径）
    default_log_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'logs')
    
    # 记录当前实际的日志所在目录
    current_log_path = ''
    
    # 记录当前实际的日志完整路径
    current_log_file = ''

    # 日志文件内容格式
    log_format = '[%(asctime)s.%(msecs)03d][%(process)s][%(levelname)s][%(filename)s:%(lineno)d] %(message)s'

    # 日志中时间格式
    log_time_format = '%Y%m%d %H:%M:%S'

    # 日志进程
    log_process = None

    def __init__(self):
        pass

    @staticmethod
    def print_console_log(level, message):
        print('--------------------------------------------------')
        if level == logging.WARN:
            level_str = '[WARN]'
        elif level == logging.ERROR:
            level_str = '[ERROR]'
        elif level == logging.FATAL:
            level_str = '[FATAL]'
        else:
            level_str = '[INFO]'
        print('\t%s %s' % (level_str, message))
        print('--------------------------------------------------')

    @staticmethod
    def init(clear_logs=True, log_path=''):
        #
        console = logging.StreamHandler()
        console.setLevel(logging.FATAL)
        logger = logging.getLogger()
        logger.addHandler(console)

        try:
            # 如果外部没有指定日志存储路径则默认在common同级路径存储
            if log_path == '':
                log_path = LogInit.default_log_path
                if not os.path.exists(log_path):
                    os.makedirs(log_path)
            LogInit.current_log_path = log_path

            # 清理旧的日志并初始化当前日志路径
            if clear_logs:
                LogInit.clear_old_log_files()
            LogInit.current_log_file = LogInit._get_latest_log_file()

            socket_handler = logging.handlers.SocketHandler('localhost', logging.handlers.DEFAULT_TCP_LOGGING_PORT)
            logging.getLogger().setLevel(logging.INFO)
            logging.getLogger().addHandler(socket_handler)

            #
            LogInit.start()

        except Exception as ex:
            LogInit.print_console_log(logging.FATAL, 'init() exception: %s' % str(ex))
            traceback.print_exc()

    @staticmethod
    def start():
        if LogInit.log_process is None:
            LogInit.log_process = Process(target=_log_listener_process, name='LogRecorder', args=(LogInit.log_format, LogInit.log_time_format, LogInit.current_log_file))
            LogInit.log_process.start()
        else:
            pass

    @staticmethod
    def stop():
        if LogInit.log_process is None:
            pass
        else:
            LogInit.log_process.terminate()
            LogInit.log_process.join()

    @staticmethod
    def _get_latest_log_file():
        latest_log_file = ''
        try:
            if os.path.exists(LogInit.current_log_path):
                for maindir, subdir, file_name_list in os.walk(LogInit.current_log_path):
                    for file_name in file_name_list:
                        apath = os.path.join(maindir, file_name)
                        if apath > latest_log_file:
                            latest_log_file = apath

            if latest_log_file == '':
                latest_log_file = LogInit.current_log_path + os.sep + 'system_'
                latest_log_file += time.strftime("%Y%m%d_%H%M%S", time.localtime(time.time())) + '.log'

        except Exception as ex:
            logging.error('EXCEPTION: %s' % str(ex))
            traceback.print_exc()

        finally:
            return latest_log_file

    @staticmethod
    def get_log_file():
        return LogInit.current_log_file

    @staticmethod
    def clear_old_log_files():
        if not os.path.exists(LogInit.current_log_path):
            logging.warning('clear_old_log_files() Not exist: %s' % LogInit.current_log_path)
            return

        try:
            for maindir, subdir, file_name_list in os.walk(LogInit.current_log_path):
                for file_name in file_name_list:
                    apath = os.path.join(maindir, file_name)
                    if apath != LogInit.current_log_file:
                        logging.info('DEL -> %s' % str(apath))
                        os.remove(apath)
                    else:
                        with open(LogInit.current_log_file, 'w') as f:
                            f.write('')

            logging.debug('Clear log done.')

        except Exception as ex:
            logging.error('EXCEPTION: %s' % str(ex))
            traceback.print_exc()
