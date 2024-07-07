from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.apps import apps
app_name = 'app'

@receiver(post_migrate)
def handle_post_migrate(sender,**kwargs):
    print('migrate')
    if sender.name == app_name:
        add_initial_data()

def add_initial_data():
    ErrorCharges = apps.get_model(app_name, 'ErrorCharges')
    if not ErrorCharges.objects.exists():
        initial_data = [
            ErrorCharges(error='Name', description="the system or user interface cannot locate or retrieve the patient's name from the database or input fields. It could be due to a missing entry or an error in data entry."),
            ErrorCharges(error='Date of Birth', description="the system or user interface cannot find or retrieve the patient's date of birth from the available records. It typically means the date of birth information is either missing or not properly entered."),
            ErrorCharges(error='Medical Record', description="The MRN serves as a unique identifier for the patient within the healthcare system, so this error suggests that the MRN is either missing or there is an issue with accessing the database or records."),
        ]
        ErrorCharges.objects.bulk_create(initial_data)
