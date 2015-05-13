from __future__ import print_function, absolute_import

import sys


# loaded as a content manager, we can check wether IPython/jupyter is in sys module,
# then the answer is unambiguous/
DEFINITIVELY_JUPYTER = 'jupyter_notebook' in sys.modules

# we might want to check wether this is in an IPython context (ie there is
# IPython is sys.modules, but then we need to check version)

MAYBE_IPYTHON = 'IPython' in sys.modules

if MAYBE_IPYTHON and not DEFINITIVELY_JUPYTER:
    import IPython
    # IPython 4.0+ context, so we definitively
    # should have Jupyter installed
    if IPython.version_info >= (4,0):
        DEFINITIVELY_JUPYTER = True

JUPYTER = False

if DEFINITIVELY_JUPYTER:
    JUPYTER = True
else:
    # none of above in sys.module,
    # we might be at install time.
    # guess for the best.
    try:
        # if jupyter is installed, assume jupyter
        import  jupyter_notebook.nbextensions
        # silence pyflakes
        jupyter_notebook.nbextensions
        JUPYTER = True
    except ImportError:
        pass


if JUPYTER:
    import  jupyter_notebook.nbextensions as nbe
else:
    import IPython.html.nbextensions as nbe

# silence pyflakes
nbe