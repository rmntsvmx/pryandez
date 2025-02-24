import pygame
import requests
import sys


MAP_API_SERVER = "http://static-maps.yandex.ru/1.x/"
WIDTH, HEIGHT = 600, 450


lon, lat = 37.677751, 55.757718
zoom = 15


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
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_PAGEUP and zoom < 17:
                    zoom += 1
                elif event.key == pygame.K_PAGEDOWN and zoom > 2:
                    zoom -= 1


                map_image = get_map_image(lon, lat, zoom)
                with open("map.png", "wb") as file:
                    file.write(map_image)
                map_surface = pygame.image.load("map.png")

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
