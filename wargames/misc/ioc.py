#!/usr/bin/env python

import sys
from sys import argv
import collections
import math

# Gets the average IOC for some ciphertext when split into different periods (or key lengths)
def get_avg_ioc(cipher_flat, cipher_period):
	strings = ["" for x in range(cipher_period)]

	strindex = 0
	counter = 0
	chindex = 0
	for ch in cipher_flat:
		strings[counter] += ch
		counter += 1
		if (counter >= cipher_period):
			counter = 0	
		
	#print(strings)
	avgioc = 0
	for s in strings:
		avgioc += compute_IOC(s)
	avgioc /= len(strings)
	print("Avg IOC for period of " + str(cipher_period) + " was: " + str(avgioc))

# Computes the IOC for a piece of ciphertext 
#  from practicalcryptography
def compute_IOC(cipher_flat):
	# Tag em
	N            = len(cipher_flat)
	freqs        = collections.Counter( cipher_flat )
	alphabet     =  map(chr, range( ord('A'), ord('Z')+1))
	freqsum      = 0.0

	# Do the math
	for letter in alphabet:
	    freqsum += freqs[ letter ] * ( freqs[ letter ] - 1 )

	IC = freqsum / ( N*(N-1) )

	#print(N)	
#	print "%.3f" % IC, "({})".format( IC )
	return IC

cipher_text = "WOYFN ZCMSH VUVTG BFUTW ABTZP FHIMF TFOSU UXFQC HKVKG MPUUQ MHRXI OVBRZ EPJYF KKVJW GEIOV HUKEB JUNSM THIMF TFKUB ULMMQX"

# remove all non alpha and whitespace and force uppercase
# SOTHATCIPHERTEXTLOOKSLIKETHIS
cipher_flat  = "".join( 
                        [x.upper() for x in cipher_text.split() \
                                   if  x.isalpha() ]
                     )
cipher_len = len(cipher_flat)
cipher_period = int(argv[1])
for y in range(1, cipher_period + 1):
	get_avg_ioc(cipher_flat, y)

