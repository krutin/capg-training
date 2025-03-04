class Logger:
    def log(self, message, error="info"):
        if error == "error":
            print(f"ERROR: {message}")
        elif error == "warning":
            print(f"WARNING: {message}")
        elif error == "info":
            print(f"INFO: {message}")
        else:
            print(f"UNKNOWN: {message}")

logger = Logger()
logger.log("This is an info message.")  
logger.log("This is a warning message.", "warning")
logger.log("This is an error message.", "error")
logger.log("This is an unknown message.", "unknown")