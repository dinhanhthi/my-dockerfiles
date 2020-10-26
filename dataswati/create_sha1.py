#! /usr/bin/python
"""
Password generation for the IPython notebook.
"""
import getpass
import hashlib
import random


salt_len = 12

def encode(u, encoding='ascii'):
    return u.encode(encoding, "replace")

def passwd(passphrase=None, algorithm='sha1'):
    """Generate hashed password and salt for use in notebook configuration.
    In the notebook configuration, set `c.NotebookApp.password` to
    the generated string.
    Parameters
    ----------
    passphrase : str
        Password to hash.  If unspecified, the user is asked to input
        and verify a password.
    algorithm : str
        Hashing algorithm to use (e.g, 'sha1' or any argument supported
        by :func:`hashlib.new`).
    Returns
    -------
    hashed_passphrase : str
        Hashed password, in the format 'hash_algorithm:salt:passphrase_hash'.
    Examples
    --------
    >>> passwd('mypassword')
    'sha1:7cf3:b7d6da294ea9592a9480c8f52e63cd42cfb9dd12'
    """
    if passphrase is None:
        for i in range(3):
            p0 = getpass.getpass('Enter password: ')
            p1 = getpass.getpass('Verify password: ')
            if p0 == p1:
                passphrase = p0
                break
            else:
                print('Passwords do not match.')
        else:
            raise UsageError('No matching passwords found. Giving up.')

    h = hashlib.new(algorithm)
    salt = ('%0' + str(salt_len) + 'x') % random.getrandbits(4 * salt_len)
    h.update(encode(passphrase, 'utf-8') + encode(salt, 'ascii'))

    return ':'.join((algorithm, salt, h.hexdigest()))
if __name__ == "__main__" :
    print(passwd())
