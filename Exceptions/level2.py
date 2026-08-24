
import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

format = logging.Formatter(
    "\n{\n Message   : %(message)s \n FileName  : %(name)s \n LevelName : %(levelname)s \n TimeStamp : %(asctime)s \n}\n"
)

file_handeler = RotatingFileHandler(
    "../logging/logs/app.log",
    maxBytes=10*1024,
    backupCount=3
)
file_handeler.setLevel(logging.DEBUG)
file_handeler.setFormatter(format)

logger.addHandler(file_handeler)


try:
    num = int(input("Enter number: "))
    if num<0:
        raise ZeroDivisionError("Zero se divide kyu kar rha hai")
    result = 100 / num

except ValueError:
    print("Invalid input")

except Exception as e:
    logger.error("Divide By Zero Error")
    raise

# overriding

# except Exception as e:
#     print("Cannot divide : ", e)

else:
    print("Success!")
    print("Result:", result)

finally:
    print("Program execution completed")