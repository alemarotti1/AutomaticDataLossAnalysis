import os
import re
from pathlib import Path

def get_work_dir():
    """return the current working directory
    Returns
    -------
    path : pathlib.Path
        the path to the current working directory
    """
    return Path('../')

def get_project_directory():
    """return the directory where the projects are stored
    Returns
    -------
    path : pathlib.Path
        the path to the directory where the projects are stored
    """
    return get_work_dir() / 'projetos'

def get_model_directory():
    """return the directory where the models are stored
    Returns
    -------
    path : pathlib.Path
        the path to the directory where the models are stored
    """
    return get_work_dir() / 'modelos'

def get_all_projects():
    """ return a list of all projects directories
    Returns
    -------
    list : list
        list of all directories of the projects
    """
    return [x for x in get_project_directory().iterdir() if x.is_dir()]


def get_list_from_project(project):
    """ return a list of all files in a project 
    Parameters
    ----------
    project : str
        the name of the project directory
    
    Returns
    -------
    list : list
        list of all names of the files in the project
    """

    dir = get_project_directory() / project / 'dataloss'
    var_instances =  [x for x in dir.iterdir() if x.is_dir()]
    #iterate over all instances and get the list of files
    files = []
    for instance in var_instances:
        files.extend([x for x in instance.iterdir() if x.is_file()])
    #pass the name of the files through a regex in the following format: "4digits-2digits-2digits space 2digits-2digits-2digits"
    files = [re.findall(r'\d{4}-\d{2}-\d{2} \d{2}-\d{2}-\d{2}', x.name)[0] for x in files]
    return files



