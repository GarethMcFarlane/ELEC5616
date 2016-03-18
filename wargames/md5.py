from time import time
import string
import random

from Crypto.Hash import MD5

hash = "f85ea6afca086f6cda7d9ceb05545cab"


while True:
  # Generate random string and hash it.
  randomStr = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(20))
  h_attempt = MD5.new(randomStr.encode("ascii")).hexdigest()
  if (h_attempt == hash):
    print(randomStr)
    break


