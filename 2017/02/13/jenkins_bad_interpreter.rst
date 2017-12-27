Jenkins Bad Interpreter
=======================

.. author:: default
.. categories:: none
.. tags:: Jenkins, CI, build
.. comments:: 


If the Jenkins build breaks and the error is: `bad interpreter: No such file or directory`, you likely reached the maximum number of character allowed in a she-bang (#! executable).
In many many modern linux implementations such value is set in the kernel variable `BINPRM_BUF_SIZE` to 127.

This limit is also mentioned in `man execve <https://linux.die.net/man/2/execve>`_
	      
.. code-block:: bash

     ... /data/jenkins/workspace/smoke_tests/environment/prod-az1-env-region/label: bad interpreter: No such file or directory

It frequently happens with the `Matrix Jenkins Plugin <https://wiki.jenkins-ci.org/display/JENKINS/Matrix+Project+Plugin>`_ that concatenate every variable in the path name.

There is no silver bullet for this issue. Using /var/tmp might be a good approach but be aware that it will be out of the Jenkins control.


