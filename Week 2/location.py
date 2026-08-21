#Tuples
import sys

def main():
    coordinates = (42.376, -71.115)
    print(f"Latitude: {coordinates[0]}")
    print(f"Longitude: {coordinates[1]}")
    #Unpacking the Tuple
    latitude, longitude = coordinates
    print(f"Latitude: {latitude}")
    print(f"Longitude: {longitude}")  
    # coordinates[0] = -42.23 # tuples are immutable TypeError: 'tuple' object does not support item assignment
    coordinates_list = [42.376, -71.115]
    print(f"{sys.getsizeof(coordinates)} bytes")
    print(f"{sys.getsizeof(coordinates_list)} bytes")

main()