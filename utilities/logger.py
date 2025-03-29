import logging
from functools import wraps

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def log_function_call(func):
    """Decorator to log function calls"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Calling function: {func.__name__} with arguments {args} {kwargs}")
        return func(*args, **kwargs)
    return wrapper
