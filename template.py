import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

project_name="mlproject1"

list_of_files=[
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/model_trainer.py",
    f"src/{project_name}/components/model_monitoring.py",
    f"src/{project_name}/pipelines/__init__.py",
    f"src/{project_name}/pipelines/training_pipeline.py",
    f"src/{project_name}/pipelines/prediction_pipeline.py",
    f"src/{project_name}/exception.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/utils.py",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py"
]

# for filepath in list_of_files:
#     filepath=Path(filepath)
#     filedir,filename=os.path.split(filepath)

#     if filedir!="":
#         os.makedirs(filedir,exist_ok=True)
#         logging.info(f"Creating directory: {filedir} for the file: {filename}")

#     if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
#         with open(filepath,"w") as f:
#             pass
#             logging.info(f"Creating empty file: {filename}")

#     else:
#         logging.info(f"{filename} already exists")

for file_str in list_of_files:
    filepath = Path(file_str)
    
    # Clean, modern handling of directory strings via pathlib
    if filepath.parent != Path("."):
        filepath.parent.mkdir(parents=True, exist_ok=True)
        logging.info(f"Verified directory path exists: {filepath.parent}")
        
    # Non-destructive file tracking initialization 
    if not filepath.exists():
        filepath.touch()
        logging.info(f"Initialized blank file resource: {filepath}")
    else:
        logging.info(f"File asset [ {filepath.name} ] already exists. Skipping securely.")