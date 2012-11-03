A Python implementation of the very secure and useful [#insecure]_ rotX (also known as caesar ciphers) family of encryption algorithms.

Usage
=====

rotx.py contains a single function, ``rot``. The signature for this function is as follows (where ``n`` is your encryption key)::

    rotx.rot(input, n, alphabetical_only=True)

To decrypt, invert ``n``. ``alphabetical_only`` decides whether to only encrypt the ASCII letters (like a true caesar cipher, leaving the other characters intact, including numbers) or to use the full spectrum of the encoding in use (all 8 bits if a bytestring, up to 0xFFFF or 0x10FFFF for unicode depending on whether your Python installation was compiled with UCS-2/UTF-16 or UCS-4/UTF-32).

Testing
=======
Testing is done using tox and Pythonbrew, run the following assuming both of these have been installed to run the tests::

    $ pythonbrew install 2.7.3
    $ pythonbrew install 2.6.6
    $ tox

.. [#insecure] Disclaimer: The rotX algorithms are neither actually secure nor useful.