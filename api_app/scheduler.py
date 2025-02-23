# api_app/scheduler.py
import pandas as pd
from apscheduler.schedulers.background import BackgroundScheduler
from .models import Person

def import_excel_data():
    # Change the file path to your actual Excel file location
    file_path = r'C:\Users\Asus TUF\Desktop\Desktop\django_project\data_supply\persons.xlsx'
    try:
        df = pd.read_excel(file_path)
        # Optional: clear existing data before import (be cautious with production data)
        Person.objects.all().delete()
        for index, row in df.iterrows():
            Person.objects.create(
                name=row['Name'],    # Replace with your actual column name
                email=row['Email']   # Replace with your actual column name
            )
        print("Excel data imported successfully.")
    except Exception as e:
        print("Error importing Excel data:", e)

def start_scheduler():
    scheduler = BackgroundScheduler()
    # Schedule the job to run every minute
    scheduler.add_job(import_excel_data, 'interval', minutes=1)
    scheduler.start()
