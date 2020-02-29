def album(car,com):
    album = []
    for i in com:
        if(i in car):
            album.append(i)
    return len(car) - len(album)
