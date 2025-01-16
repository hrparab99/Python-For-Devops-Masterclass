import datetime
import shutil
import os

def create_backup(source_path,destination_path):
    date_name = datetime.date.today()
    backup_name = os.path.join(destination_path,f"backup1_{date_name}")
    try:
        shutil.make_archive(backup_name,'gztar',source_path)
        print("Backup completed")
    except Exception as e:
        print("Backup not completed\nError :",e)
    
source_path = "D:/DevOps/Python-For-Devops/Python-03Day-Course"
destination_path = "D:/DevOps/Python-For-Devops/Backup"

create_backup(source_path, destination_path)