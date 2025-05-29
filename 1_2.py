import os
import threading

print(f'исполняется python-процесс с идентификатором: {os.getpid()}')

total_threads = threading.active_count()
thread_name = threading.current_thread().name


print(f'В данный момент Python испоняет {total_threads} поток(ов)')
print(f'имя текущего потока {thread_name}')
