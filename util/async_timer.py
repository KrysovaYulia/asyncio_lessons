import functools
import time
from typing import Callable, Any

def async_timed():
	def wrapper(func):
		@functools.wraps(func)
		async def wrapped(*args, **kwargs):
			print(f'выполняется {func}  с аргументами {args} {kwargs}')
			start = time.time()
			try:
				return await func(*args, **kwargs)
			finally:
				end = time.time()
				total = end - start
				print(f'{func} завершилаьс за {total:.4f}  c')
		return wrapped

return wrapper
