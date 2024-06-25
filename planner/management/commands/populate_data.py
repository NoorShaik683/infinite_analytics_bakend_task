# planner/management/commands/populate_data.py
from django.core.management.base import BaseCommand
from planner.models import Location, PicnicSpot

locations = [
    {
        'name': 'Goa',
        'latitude': '15.2993',
        'longitude': '74.1240'
    },
    {
        'name': 'Ooty',
        'latitude': '11.4102',
        'longitude': '76.6950'
    },
    {
        'name': 'Manali',
        'latitude': '32.2396',
        'longitude': '77.1887'
    },
    {
        'name': 'Shimla',
        'latitude': '31.1048',
        'longitude': '77.1734'
    },
    {
        'name': 'Mysore',
        'latitude': '12.2958',
        'longitude': '76.6394'
    }
]

picnic_spots = {
    'Goa': [
        {
            'name': 'Palolem Beach',
            'description': "One of the area's most picturesque beaches.",
            'distance': '2'
        },
        {
            'name': 'Baga Beach',
            'description': 'We indulged in thrilling water sports during the day, from parasailing to jet-skiing.',
            'distance': '5'
        },
        {
            'name': 'Agonda Beach',
            'description': 'And om sai beach huts are best in agonda beach',
            'distance': '20'
        },
        {
            'name': 'Canacona',
            'description': 'Best Waterfalls',
            'distance': '12'
        },
        {
            'name': 'Calangute',
            'description': 'Good Fort to chill',
            'distance': '32'
        }
    ],
    'Ooty': [
        {
            'name': 'Rose Garden',
            'description': "One of the area's most picturesque flowers.",
            'distance': '2'
        },
        {
            'name': 'Botanical Garden',
            'description': 'We indulged in thrilling water sports during the day.',
            'distance': '5'
        },
        {
            'name': 'St Stephen Church',
            'description': 'Historical Church',
            'distance': '20'
        },
        {
            'name': 'Boat House',
            'description': 'Best Boring Experience',
            'distance': '12'
        },
    ],
    'Manali': [
        {
            'name': 'Solang Valley',
            'description': "Known for its stunning views and adventure sports.",
            'distance': '14'
        },
        {
            'name': 'Hadimba Temple',
            'description': 'An ancient cave temple surrounded by cedar forest.',
            'distance': '2'
        },
        {
            'name': 'Rohtang Pass',
            'description': 'A high mountain pass with breathtaking scenery.',
            'distance': '51'
        }
    ],
    'Shimla': [
        {
            'name': 'Mall Road',
            'description': "Shimla's main street, lined with shops, cafes, and attractions.",
            'distance': '1'
        },
        {
            'name': 'Jakhoo Temple',
            'description': 'A temple dedicated to Hanuman, located on Jakhoo Hill.',
            'distance': '2.5'
        },
        {
            'name': 'The Ridge',
            'description': 'A large open space in the heart of Shimla, offering panoramic views.',
            'distance': '1'
        }
    ],
    'Mysore': [
        {
            'name': 'Mysore Palace',
            'description': 'A historical palace and royal residence.',
            'distance': '0'
        },
        {
            'name': 'Brindavan Gardens',
            'description': 'Famous for its symmetric design and musical fountain.',
            'distance': '21'
        },
        {
            'name': 'Chamundi Hill',
            'description': 'Offers a panoramic view of the city and houses a temple.',
            'distance': '13'
        }
    ]
}

class Command(BaseCommand):
    help = 'Populates the database with dummy data'

    def handle(self, *args, **options):
        print('Populating locations...')
        for loc in locations:
            location, created = Location.objects.get_or_create(
                name=loc['name'],
                latitude=loc['latitude'],
                longitude=loc['longitude']
            )
            print(f'Created location: {location.name}')

        print('Populating picnic spots...')
        for loc_name, spots in picnic_spots.items():
            location = Location.objects.get(name=loc_name)
            for spot in spots:
                picnic_spot, created = PicnicSpot.objects.get_or_create(
                    name=spot['name'],
                    location=location,
                    description=spot['description'],
                    distance=spot['distance']
                )
                print(f'Created picnic spot: {picnic_spot.name} in {location.name}')
        
        print('Database population completed.')
