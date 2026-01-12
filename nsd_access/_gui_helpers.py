"""
Helper functions for environment detection
"""


def X_is_running():
    """Check if an X server is running
    Returns:
        True if an X server is running
    """
    try:
        from subprocess import Popen, PIPE
        p = Popen(["xset", "-q"], stdout=PIPE, stderr=PIPE)
        p.communicate()
        return p.returncode == 0
    except FileNotFoundError:
        # Non Linux GUI
        return False
    except Exception:
        # Avoiding blocking errors
        return False


def isnotebook():
    """Check if running in a Jupyter notebook
    Returns:
        True if running in a Jupyter notebook
    """
    try:
        shell = get_ipython().__class__.__name__
        return shell == 'ZMQInteractiveShell'
    except NameError:
        return False      # Probably standard Python interpreter
    except Exception:
        return False
