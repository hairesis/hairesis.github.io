Deal with side-effects in Python unittests
==========================================

.. author:: default
.. categories:: programming, python
.. tags:: programming, python, unittests
.. comments::

It’s not infrequent (especially during refractories) the case where is necessary to deal with side-effects.
I came across this situation recently and here is how I’ve approached it.

Let’s take pycurl as an example. We don’t want to test pycurl (hopefully is tested somewhere else) but we want to know if at some point our code sets the right options in the pycurl object.
Since there is no easy way to inspect the pycurl object, I came out with the solution in the snippet below:

.. code-block:: python

    pycurl_obj = Mock()
    # Create a named function that intercepts the setopt and
    # store the values in a dictionary rather than the object itself,
    # in this way asserts will be handy.
    def setopt(k, v): options[k] = v
    pycurl_obj.setopt = setopt

    # Tip: Allowing an optional param in classes where
    # you are going to side instantiate internal objects,
    # helps in tests and makes the class refactoring-friendly
    s = Session(backend=pycurl_obj)

    # Assumption: verify = True should trigger the setopt on the pycurl object
    # filling as side-effect the 'options' dictionary we defined above.
    s.post('https://example.com', verify=True)

    # Assert our assumption
    assert options[pycurl.SSL_VERIFYPEER] == 1
    assert options[pycurl.SSL_VERIFYHOST] == 2
