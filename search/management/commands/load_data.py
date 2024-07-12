import csv
import json
from django.core.management.base import BaseCommand
from search.models import RestaurantData

class Command(BaseCommand):
    help = 'Load data from CSV file into the database'

    def handle(self, *args, **kwargs):
        file_path = './search/management/commands/data1.csv'  # Update with the actual path to your CSV file

        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                headers = reader.fieldnames
                self.stdout.write(self.style.SUCCESS(f'CSV Headers: {headers}'))

                for row in reader:
                    self.stdout.write(self.style.SUCCESS(f'Processing row: {row}'))
                    try:
                        RestaurantData.objects.create(
                            id=row['id'].strip(),
                            name=row['name'].strip(),
                            location=row['location'].strip(),
                            items=json.loads(row['items']),
                            geolocation=row['lat_long'].strip(),
                            fullDetails=json.loads(row['full_details'])
                        )
                    except KeyError as e:
                        self.stdout.write(self.style.ERROR(f'Missing field in row: {e}'))
                    except json.JSONDecodeError as e:
                        self.stdout.write(self.style.ERROR(f'JSON decode error: {e}'))
                    except Exception as e:
                        self.stdout.write(self.style.ERROR(f'Error processing row: {e}'))

            self.stdout.write(self.style.SUCCESS('Data loaded successfully'))
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f'File not found: {file_path}'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error reading file: {e}'))
