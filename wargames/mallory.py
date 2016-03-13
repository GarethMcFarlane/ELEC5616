from time import time
import string
import random

from Crypto.Hash import SHA256

# Get initial message and hash.
m = "Your friend Mallory changed her phone number to 027625"
m_hash = SHA256.new(m.encode("ascii")).hexdigest()[:7]



# We only want the first 7 hex characters of the hash.
shortened_to = 7

while True:
  # Generate random string and hash it.
  randomStr = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
  h_attempt = SHA256.new(randomStr.encode("ascii")).hexdigest()[:shortened_to]
  if (h_attempt == m_hash):
    print(randomStr)
    break







