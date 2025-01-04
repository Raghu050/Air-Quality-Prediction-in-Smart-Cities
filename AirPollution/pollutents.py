
from django.core.management.base import BaseCommand
from AirPollution.models import AirPollutionData
import random

class Command(BaseCommand):
    help = 'Populate AirPollutionData for Karnataka cities from 2017 to 2023'

    def handle(self, *args, **kwargs):
        karnataka_cities = [
            'Bagalkot', 'Bangalore Rural', 'Bangalore Urban', 'Belgaum', 'Bellary',
            'Bidar', 'Vijayapura', 'Chamarajanagar', 'Chikkaballapur', 'Chikkamagaluru',
            'Chitradurga', 'Dakshina Kannada', 'Davanagere', 'Dharwad', 'Gadag',
            'Gulbarga', 'Hassan', 'Haveri', 'Kodagu', 'Kolar', 'Koppal', 'Mandya',
            'Mysore', 'Raichur', 'Ramanagara', 'Shimoga', 'Tumakuru', 'Udupi',
            'Uttara Kannada', 'Yadgir'
        ]


        years = range(2017, 2024)

        for city in karnataka_cities:
            for year in years:
                pollution_level = random.randint(100, 300)  # Random pollution level between 100 and 300
                AirPollutionData.objects.create(
                    district=city,
                    year=year,
                    pollution_level=pollution_level
                )

        self.stdout.write(self.style.SUCCESS('Pollution data added successfully.'))
