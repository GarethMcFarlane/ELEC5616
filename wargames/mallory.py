from time import time
import string
import random

from Crypto.Hash import SHA256


m = "Your friend Mallory changed her phone number to 027625"
m_hash = SHA256.new(m.encode("ascii")).hexdigest()[:7]







# Try to find hash collisions for increasingly lengthier hashes
shortened_to = 7
dict = {}


while True:
  randomStr = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
  h_attempt = SHA256.new(randomStr.encode("ascii")).hexdigest()[:shortened_to]
  if (h_attempt == m_hash):
    print(randomStr)
    break







