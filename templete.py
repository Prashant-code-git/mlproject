import os 
from pathlib import Path 
import logging 

logging.basicConfig(level=logging.INFO)
project_name ="mlproject"
list_of_file=[
#".github/workflows/.gitkeep",
f"src/{project_name}/__init__.py",
f"src/{project_name}/components/__init__.py",
f"src/{project_name}/components/data_ingestion.py",
f"src/{project_name}/components/data_tranformation.py",
f"src/{project_name}/components/model_tranier.py",
f"src/{project_name}/components/model_monitering.py",
f"src/{project_name}/pipelines/__init__.py",
f"src/{project_name}/pipelines/training_pipeline.py",
f"src/{project_name}/pipelines/predication_pipeline.py",
f"src/{project_name}/exception.py",
f"src/{project_name}/logger.py",
f"src/{project_name}/utils.py",
"apps.py",
"dockerfile",
]

for filepath in list_of_file:
    filepath=Path(filepath)
    filepath,filename=os.Path.split(filepath)

    if filedir !="":
        os.maredir(filedir,exist_ok=True)
        logging.info(f"Creating directory:{filedir} for thr file {filename}")

    if (not os.Path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file:{filepath}")

    else:
        logging.info(f"{filename} is alreday exists")

