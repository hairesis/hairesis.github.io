Prevent command being logged in your shell history
==================================================

.. author:: default
.. categories:: none
.. tags:: bash, zsh, shell
.. comments::

Sometime happens that I have to test something which requires to insert a password.
Being reluctant to write down my password in a source/text files (I would hate to rotate leaked passwords on github), I typically use environment variables, but still the password leaks in the bash_history.


A way (though not the only one) to overcome this type of leaking is to set the `HISTCONTROL`_ environment variable. It works either under bash or zsh.


Values for `HISTCONTROL`_ are:

- ignorespaceflag: tells your shell to not record commands that start with spaces
- ignoredups:  tells your shell to not record duplicate commands.
- ignoreboth: if you wish to specify both values


.. code-block:: bash
		
  echo "HISTCONTROL=ignoreboth" >> ~/.bashrc && source ~/.bashrc

.. _HISTCONTROL: http://man7.org/linux/man-pages/man1/bash.1.html
