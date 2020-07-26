try:
    import jupyter_format
except ImportError as err:
    jupyter_format = None


def is_jupyter_format_available():
    """Whether the jupyter-format package is available."""
    return jupyter_format is not None
