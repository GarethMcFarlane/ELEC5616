import random

from Crypto.Hash import SHA256



msga = "Melbourne Cup: $5,000 on Horse A (Bondi Beach) [transaction id: {10]"
msgb = "Melbourne Cup: $5,000 on Horse B (Who Shot Thebarman) [transaction id: {10}]"


b_hash = SHA256.new(msgb.encode("ascii")).hexdigest()[:16]


print(b_hash)