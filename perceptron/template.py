import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:%(message)s:')

project_name = "perceptronBasics"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/_init_.py",
    f"src/{project_name}/components/_init_.py",
    f"src/{project_name}/utils/_init_.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/_init_.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/config/_init_.py",
    f"src/{project_name}/pipeline/_init_.py",
    f"src/{project_name}/constants/_init_py",
    f"src/{project_name}/entity/_init_.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "requirements.txt",
    "main.py",
    "Dockerfile",
    "setup.py",
    "research/trials.ipynb"
]

for file in list_of_files:
    filepath = Path(file)
    filedir, filename = os.path.split(filepath)
    
    if filedir != "":
        logging.info(f"Creating directory {filedir}")
        os.makedirs(filedir, exist_ok = True)
        logging.info(f"Created directory {filedir}")
        
    if (not os.path.exists(filepath)) or os.path.getsize(filepath) == 0:
        logging.info(f"Creating file {filepath}")
        with open(filepath, "w") as f:
            f.write("")
            logging.info(f"Created file {filepath}")
    
    else:
        logging.info(f"Skipping file {filepath}, Already exists !!!")