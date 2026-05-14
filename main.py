import os
from dotenv import load_dotenv

# Get a env variable
load_dotenv()
CID = os.environ['CID']
print(CID)
