#!/usr/bin/python3
import time
import hashlib


def call():
	process()

def shaFunc(string):
    """
    Return a SHA-256 hash of the given string
    """
    return hashlib.sha256(string.encode('utf-8')).hexdigest()	
