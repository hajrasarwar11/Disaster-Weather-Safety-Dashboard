import logging

# Configure logging
logging.basicConfig(
    filename='app.log',          # Log file name
    level=logging.INFO,           # Minimum level to log (INFO and above)
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Example usage in other files:
# logging.info("This is an info message")
# logging.error("This is an error message")
