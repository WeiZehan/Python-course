def make_album(singer_name, album_name,song_number=''):
    album = {
        'singer_name' : singer_name,
        'album_name' : album_name,
    }
    if song_number:
        album['song_number'] = song_number
    return album


information = make_album('wangjue','zuixuanminzufeng')
information_2 = make_album('wanggouyu','xiaoeyu','100')
print(information)
print(information_2)