:orphan:

********
Download
********

Nengo runs on Windows, Mac OS X and Linux
and requires Python.
To install Nengo, we recommend using ``pip``.

.. code-block:: bash

   pip install nengo nengo-gui

If you do not have ``pip`` installed,
or if you run into any errors
when installing Nengo with ``pip``,
read on for more detailed instructions.

``pip`` will do its best to install
all of Nengo's requirements when it installs Nengo.
However, if anything goes wrong during this process,
you can install Nengo's requirements manually
before doing ``pip install nengo`` again.

Installing Python and NumPy
===========================

Nengo's only required dependency is NumPy,
and we recommend that you install it first.
The best way to install NumPy depends
on several factors, such as your operating system.
Briefly, what we have found to work best
on each operating system is:

- Windows: Use Anaconda_, Miniconda_ or
  the `official installer <https://www.python.org/downloads/>`_ and
  `unofficial binaries <http://www.lfd.uci.edu/~gohlke/pythonlibs/>`_.
- Mac OS X: Use Anaconda_, Miniconda_ or Homebrew_.
- Linux: Use Anaconda_, Miniconda_,
  your operating system's package manager, or install from source.

For more options, see
`SciPy.org's installation page <http://www.scipy.org/install.html>`_.
For our recommended options, read on.

Anaconda
--------

Anaconda_ provides an all-in-one solution
that will install Python, NumPy,
and other optional Nengo dependencies.
It works on all operating systems (Windows, Mac, Linux)
and does not require administrator privileges.
It includes GUI tools,
as well as a robust command line tool, ``conda``,
for managing your Python installation.

Run the graphical installer for your operating system
to install it.
Unless you have a reason to stay with Python 2,
opt for the Python 3 installer.
Once Anaconda is installed,
open the Anaconda command prompt and do

.. code-block:: bash

   pip install nengo nengo-gui

to complete Nengo installation.

Miniconda
---------

Miniconda_ gives you the convenience of
the ``conda`` command line tool
without having to download a ton of packages
you might not use.
After running the Miniconda_ installer,
open the command prompt and do

.. code-block:: bash

   conda install numpy pip
   pip install nengo nengo-gui

will install Nengo and its dependencies.

Package managers
----------------

If you are comfortable with the command line,
operating systems other than Windows
have package managers that can install Python and NumPy.

Mac OS X: Homebrew
^^^^^^^^^^^^^^^^^^

On Mac OS X, Homebrew_ has excellent Python support.
After installing Homebrew:

.. code-block:: bash

   brew install python
   pip install numpy
   pip install nengo nengo-gui

will install Nengo and its dependencies.

Debian, Ubuntu: apt
^^^^^^^^^^^^^^^^^^^

In Debian, Ubuntu, and other distributions with ``apt``, do:

.. code-block:: bash

   sudo apt-get install python-numpy python-pip
   pip install nengo nengo-gui

Fedora, CentOS: yum
^^^^^^^^^^^^^^^^^^^

In Fedora, CentOS, and others distributions with ``yum``, do:

.. code-block:: bash

   sudo yum install python-numpy python-pip
   pip install nengo nengo-gui

From source
-----------

If speed is an issue
and you know your way around a terminal,
installing NumPy from source
is flexible and performant.
See the detailed instructions
`here <http://hunseblog.wordpress.com/2014/09/15/installing-numpy-and-openblas/>`_.
Once NumPy is installed, you can install Nengo with
``pip install nengo nengo-gui``.

.. _Anaconda: https://store.continuum.io/cshop/anaconda/
.. _Miniconda: https://conda.io/miniconda.html
.. _Homebrew: http://brew.sh/

Installing optional packages
============================

While NumPy is the only hard dependency,
some optional Nengo features require other packages.
These can be installed either through
Anaconda, a package manager, or through ``pip``.
Other packages that Nengo can interact with include

- `SciPy <https://www.scipy.org/scipylib/index.html>`_
- `Matplotlib <https://matplotlib.org/>`_
- `Jupyter <http://jupyter.org/>`_
- `scikit-learn <http://scikit-learn.org/stable/>`_
- `pytest <https://docs.pytest.org/en/latest/>`_

Other parts of the :ref:`Nengo ecosystem`
may interact with other packages.
See their documentation for details.
