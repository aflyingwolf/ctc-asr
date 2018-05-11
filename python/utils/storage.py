"""Storage and version control helper methods."""

import os

from git import Repo


def git_revision_hash():
    """Return the git revision id/hash.

    Returns:
        str: Git revision hash.
    """
    repo = Repo('.', search_parent_directories=True)
    return repo.head.object.hexsha


def git_branch():
    """Return the active git branches name.

    Returns:
        str: Git branch.
    """
    repo = Repo('.', search_parent_directories=True)
    return repo.active_branch.name


def delete_file_if_exists(path):
    """Delete the file for the given path, if it exists.

    Args:
        path (str): File path.

    Returns:
        Nothing.
    """
    if os.path.exists(path) and os.path.isfile(path):
        os.remove(path)