import random

from Crypto.Hash import SHA256

dict = {}

msga = "Melbourne Cup: $5,000 on Horse A (Bondi Beach) [transaction id: {%d]"

for ID in range(0,999999):
    ma_dash = msga % ID
    ma_dash_hash = SHA256.new(ma_dash.encode("ascii")).hexdigest()[:32]
    dict[ma_dash_hash] = ma_dash


    


msgb = "Melbourne Cup: $5,000 on Horse B (Who Shot Thebarman) [transaction id: {%d}]"


for ID in range(0,999999):
    mb_dash = msgb % ID
    mb_dash_hash = SHA256.new(mb_dash.encode("ascii")).hexdigest()[:32]
    if mb_dash_hash in dict:
        print(mb_dash_hash)
        print(dict[mb_dash_hash])





