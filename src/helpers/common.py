"""common methods"""
import os

def parent_dir(path, levels=1) -> str:
    """Retourne le path du répertoire parent 
    jusqu'au niveau fourni en argument
    """
    for _ in range(levels):
        path = os.path.dirname(path)
    return path
