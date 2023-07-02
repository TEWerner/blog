import os
import json

def generate_locations_data(dir_path):
    locations_data = []

    for dir_name in os.listdir(dir_path):
        location_dir_path = os.path.join(dir_path, dir_name)
        print(location_dir_path, os.path.isdir(location_dir_path))
        if os.path.isdir(location_dir_path):
            pictures = [
                f for f in os.listdir(location_dir_path) 
                if os.path.isfile(os.path.join(location_dir_path, f))
            ]
            location_data = {
                "name": dir_name,
                "description": "",
                "date": "",
                "coordinates": {"lat": 0, "lng": 0},
                "pictures": [
                    {
                        "path": f'assets/pictures/{dir_name}/{pic}',
                        "description": ""
                    }
                    for pic in pictures
                ],
                "mainPicturePath": f'assets/pictures/{dir_name}/{pictures[0]}' if pictures else ""
            }
            locations_data.append(location_data)
    
    return locations_data

dir_path = 'C:/Users/timur/Documents/blog/src/assets/pictures'
locations_data = generate_locations_data(dir_path)
with open('C:/Users/timur/Documents/blog/src/assets/locations_data.json', 'w') as f:
    json.dump(locations_data, f, indent=4)
