import hmac
from hashlib import sha1
from time import time


def hmac_sha1(key, msg):
    return hmac.new(key, msg, sha1).hexdigest()


method = "GET"
duration_in_seconds = 60 * 60 * 24
expires = int(time() + duration_in_seconds)
path = "/v1/my_account/container/object"
key = "MYKEY"
hmac_body = "%s\n%s\n%s" % (method, expires, path)
signature = hmac.new(key, hmac_body, sha1).hexdigest()
