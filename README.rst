UX-SAD's Documentation
======================

All of the documentation is built using Sphinx, and it is hosted at ReadTheDocs
http://uxsad.readthedocs.io/

How to Build the Documentation
------------------------------

First, you need to install the software needed to build the docs. You can
install it by running the following command in the ``docs`` directory (on
Windows, you may have to change ``pip3`` to ``pip``):

.. code-block:: shell
 
   pip3 install -r requirements.txt

If you are on OSX/Linux, you can build the docs using this command:

.. code-block:: shell

   make html

On Windows, you need to run this:

.. code-block:: shell

   make.bat html

Once this completes, you can open ``_build/html/index.html`` to view the
generated documentation.
