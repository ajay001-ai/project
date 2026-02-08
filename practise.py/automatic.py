import os
import logging
from datetime import datetime

Backup_folder = "back_ups"
Archive_files = os.path.join(Backup_folder, "old_backups")
Report_file = "back_rep.txt"

Archive_days = 7
Delete_days = 30

logging.basicConfig(
    filename="back_rep.txt",
    level=logging.INFO,
    format="%(message)s",
    filemode="w"
)


os.makedirs(Archive_files, exist_ok=True)

today = datetime.now()

for file_name in os.listdir(Backup_folder):

    if not file_name.startswith("backup_") or not file_name.endswith(".zip"):
        continue

    date_text = file_name.replace("backup_", "").replace(".zip", "")
    file_date = datetime.strptime(date_text, "%Y-%m-%d")

    file_ages = (today - file_date).days

    source_path = os.path.join(Backup_folder, file_name)
    destination_path = os.path.join(Archive_files, file_name)

    if file_ages > Delete_days:
        os.remove(source_path)
        logging.info(f"Deleted: {file_name}")

    elif file_ages > Archive_days:
        os.rename(source_path, destination_path)
        logging.info(f"Archived: {file_name}")

    else:
        logging.info(f"Kept: {file_name}")

print("Backup cleaned")
print(f"Report Saved to {Report_file}")
