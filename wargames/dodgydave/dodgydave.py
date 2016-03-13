import random
import sys

from Crypto.Hash import SHA256

# Initialise dictionary and messages.
dict = {}
msga = "Melbourne Cup: $5,000 on Horse A (Bondi Beach) [transaction id: %d]"
msgb = "Melbourne Cup: $5,000 on Horse B (Who Shot Thebarman) [transaction id: %d]"


# Create sufficiently large dictioanry of good hashes.
print("Generating dictionary")
for ID in range(0,999999):
    ma_dash = msga % ID
    ma_dash_hash = SHA256.new(ma_dash.encode("ascii")).hexdigest()[:8]
    dict[ma_dash_hash] = ma_dash


    



# Generate new hashes and check if they exist in the dictionary.  If they do we have a collision.
print("Dictionary created.  Checking for collisions.")
id = 0

while True:
    mb_dash = msgb % id
    mb_dash_hash = SHA256.new(mb_dash.encode("ascii")).hexdigest()[:8]
    if mb_dash_hash in dict:
    	print("Found collision with hash: %s" % mb_dash_hash)
    	print("Message A:")
    	print(dict[mb_dash_hash])
    	print("Message B:")
    	print(mb_dash)
    	sys.exit()
    id += 1

    






