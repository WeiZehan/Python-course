def make_album(singer_name, album_name,song_number=''):
    album = {
        'singer_name': singer_name,
        'album_name': album_name,
    }
    if song_number:
        album['song_number'] = song_number
    return album


while True:
    singer = input("Please input singer name : ")
    album = input("Please input album name : ")
    number = input("Please input song number : ")
    if singer == 'q' or album == 'q' or number == 'q':
        break
    else:
        album = make_album(singer,album,number)
        print(album)