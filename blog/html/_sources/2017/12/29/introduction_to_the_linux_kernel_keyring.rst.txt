Introduction to the Linux Kernel Keyring
========================================


.. author:: default
.. categories:: Linux, Kernel, Security
.. tags:: none
.. comments::


Everyone faced at least once the problem of storing credentials (for a CLI, a ReST API, or whatnot).

Options are: exporting an environment variable or more conveniently store the secret in plaintext, perhaps with access permissions.

The latter is often encouraged by guidelines of tools providing user and password tuples (in CSVs) to store in *.ini* or *.conf* files leading to leaked passwords or why not `bitcoin wallets private keys <https://steemit.com/bitcoin/@defango/searching-for-bitcoin-with-bigquery-or-ai-systems>`_ in git repositories, logs, Jenkins build Jobs: secrets are NOT configuration.

There are few technologies out in the market either cloud providers or open source like `custodia <https://github.com/latchset/custodia>`_, however often we don’t have access to a Cloud specific service or we don't want to deploy another tool but we still want to store or cache credentials safely on a host. In this post I will then focus on the Linux Kernel Keyring.

The Linux Kernel Keyring is not a very publicised feature of the linux Kernel. It offers a C API interface that wraps the keyctl Linux syscall,
comes straight away on your Linux hosts since kernel 2.6.x and the keyutils library can be easily leveraged using bash, python, C ...

Keys are held in memory and secured by the kernel.

Create a new Key
----------------

.. code-block:: bash

    # keyctl add <type> <desc> <data> <keyring>

    [vagrant@localhost ~]$ keyctl add user "A Simple Keyring Demo" s3cret @u
    447071188

* *type* describes the type of key to be used. The user type used in the example can be used for arbitrary user-defined keys.
* *keyring* is the container in to which the key is going. In the example above we used @u.

  From man pages on @u:

        *This keyring is shared between all the processes owned by a particular user. It isn’t searched directly but is normally linked to from the session keyring.*
* The returned number is the Key identifier we can use in the future to retrieve the key.


Inspect the Keyring
-------------------

.. code-block:: bash

    [vagrant@localhost ~]$ keyctl show
    Session Keyring
            -3 --alswrv    500   500  keyring: _ses
     430216800 --alswrv    500    -1   \_ keyring: _uid.500
     447071188 --alswrv    500   500       \_ user: A Simple Keyring Demo


We can clearly see that the key has been linked to the vagrant’s user dedicated keyring.

Refer to `keyctl <http://man7.org/linux/man-pages/man1/keyctl.1.html>`_ and `keyutils <http://man7.org/linux/man-pages/man7/keyutils.7.html>`_ man pages for more details.


Print the key
-------------
.. code-block:: bash

    [vagrant@localhost ~]$ keyctl print 447071188
    s3cret

This just scratches the surface. It is possible to write resolvers to retrieve keys from external systems, setup permissions on a single key (interesting reading `here <https://mjg59.dreamwidth.org/37333.html>`_), set an expiry date on the keys, forget the key after the user session ends ...

Other interesting readings can be found at:


* `LWN <https://lwn.net/Articles/210502/>`_
* `pykeyctl/docs <https://github.com/jdukes/pykeyctl/blob/master/docs/Overview.org>`_
