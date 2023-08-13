import math
import requests
import numpy as np # aliasing libraries for clarity or avoiding conflicts
print(math.sqrt(16))  # Outputs: 4.0

from math import sqrt # Example of pulling a specific function from a library, rather than the whole library.
print(sqrt(16))  # Outputs: 4.0

# pandas
# numpy
# SQLAlchemy
# PySpark - Distributed workload processing, nodes with Cluster/Spark Manager and SparkWorkers. Improved fault tolerance, data partioning for parallel processing.
# Requests - HTTP requests, abstracts complexity of making requests behind a simple API

web_output = requests.get("https://www.example.com")
print(web_output) # Status code 200 "Successful Request"
print(web_output.text) # Text attribute from the request get 
