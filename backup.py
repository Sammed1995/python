import shutil
import datetime
import os


def backup_file(source, destination):
    today = datetime.date.today()
    backup_file = os.path.join(destination, f"backup_{today}.tar.gz")
    shutil.make_archive(backup_file.replace('.tar.gz',''),"gztar",source)

source="."
destination = "."

backup_file(source, destination)