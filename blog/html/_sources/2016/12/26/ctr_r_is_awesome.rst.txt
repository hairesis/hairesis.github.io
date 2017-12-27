#ctr-r-is-awesome
=================



.. author:: default
.. categories:: none
.. tags:: bash, zsh, tips-and-trics
.. comments::


I am a CTR+R addict. I love to search in my bash history back to the command I used to curl that API or just finding that command I-forgot-the-name-but-which-I-remember-the-path on that server.
Lately, I’ve also started tagging my commands by adding a hash-tag right before my command:

.. code-block:: bash

  $ #get-images curl -k -H “Content-Type=applicatio/json+somethingWeired” host000123.example.com/images?start=50&end=100&type=’imageType’&you%20egot%20ethe%20eidea/

In this way the command does not get executed (# is interpreted as a comment) and I also gain a sort of tagging somehow easier to remember than a hostname or a nasty parameter.
