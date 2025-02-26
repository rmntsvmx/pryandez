import pygame
import requests
import sys


MAP_API_SERVER = "https://static-maps.yandex.ru/v1?ll=37.677751,55.757718&spn=0.016457,0.00619&apikey=f3a0fe3a-b07e-4840-a1da-06f18b2ddf13"
WIDTH, HEIGHT = 600, 450


lon, lat = 37.6173, 55.7558
zoom = 10


def get_map_image(lon, lat, zoom):
    params = {
        "ll": f"{lon},{lat}",
        "z": zoom,
        "l": "map",
        "size": "600,450"
    }
    response = requests.get(MAP_API_SERVER, params=params)
    if not response:
        print("Ошибка запроса к API Яндекс.Карт")
        sys.exit(1)
    return response.content


def main():
    global lon, lat, zoom
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Карта")

    map_image = get_map_image(lon, lat, zoom)
    with open("map.png", "wb") as file:
        file.write(map_image)
    map_surface = pygame.image.load("map.png")

    running = True
    while running:
        screen.blit(map_surface, (0, 0))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False




    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
