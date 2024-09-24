import time
import random

def read_resource_level():
    resource_level = random.uniform(0, 100)
    return resource_level

def log_resource_data(resource_level):
    with open('resource_level_data.csv', 'a') as file:
        file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')},{resource_level:.2f}\n")

def main():
    while True:
        resource_level = read_resource_level()
        log_resource_data(resource_level)
        time.sleep(60)

if __name__ == "__main__":
    main()
