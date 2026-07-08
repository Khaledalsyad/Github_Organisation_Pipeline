def retry(retries=3):
    def retry_decorator(func):
        def inner(*args, **kwargs):
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempt + 1}/{retries} failed: {e}")
                    if attempt == retries - 1:
                        raise
            return None
        return inner
    return retry_decorator