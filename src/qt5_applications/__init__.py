import os
import pathlib

import qt5_applications._applications


from ._version import get_versions
__version__ = get_versions()['version']
del get_versions


fspath = getattr(os, 'fspath', str)

root = pathlib.Path(__file__).absolute().parent
bin = root.joinpath('Qt', 'bin')
plugins = root.joinpath('Qt', 'plugins')


def application_names():
    return [*qt5_applications._applications.application_paths.keys()]


def application_path(name):
    return bin.joinpath(qt5_applications._applications.application_paths[name])
