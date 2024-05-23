import os
import shutil
import datetime
import schedule
import time

class FolderBackupScheduler:
    def __init__(self, source_dir, destination_dir):
        self.source_dir = source_dir
        self.destination_dir = destination_dir

    def copy_folder_to_directory(self, source, dest):
        today = datetime.date.today()
        dest_dir = os.path.join(dest, str(today))

        try:
            shutil.copytree(source, dest_dir)
            print(f"Folder copied to: {dest_dir}")
        except FileExistsError:
            print(f"Folder already exists in: {dest}")

    def schedule_backup(self):
        schedule.every().day.at("23:10").do(lambda: self.copy_folder_to_directory(self.source_dir, self.destination_dir))

        while True:
            schedule.run_pending()
            time.sleep(60)

def main():
    source_dir = "Samples"
    destination_dir = "Backups"

    scheduler = FolderBackupScheduler(source_dir, destination_dir)
    scheduler.schedule_backup()

if __name__ == "__main__":
    main()
