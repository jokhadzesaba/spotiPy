from artist import *
class SpotiPy:
    def __init__(self):
        self.__artists = []
    def getArtists(self):
        return self.__artists
    def sameArtist(self, artist):
        for i in self.__artists:
            if i.getFirstName() == artist.getFirstName() and i.getSecondName() == artist.getSecondName() and i.getBitrhYear() == artist.getBitrhYear():
                return False    
        return True
    def addArtitsts(self, *artists):
        counter = 0
        for i in artists:
            if self.sameArtist(i):
                self.__artists.append(i)
                counter += 1
        return counter
    def getTopTrendingArtist(self):
        songOfArtists = []
        for i in self.__artists:
            songOfArtists.append(i.mostLikedSong())
        song = songOfArtists[0]
        for i in range(len(songOfArtists)):
            if songOfArtists[i].getLikes() > song.getLikes():
                song = songOfArtists[i]
        for i in self.__artists:
            for j in i.getAllSong():
                if j.getTitle() == song.getTitle() and j.getDuration() == song.getDuration() and j.getReleaseYear() == song.getReleaseYear() and j.getLikes() == song.getLikes():
                    tupleOfartist = (i.getFirstName(), i.getSecondName())
        return tupleOfartist

    def getTopTrendingAlbum(self):
        listOfAlbums = []
        songs = []
        likes = []
        topTrendingAlbum = ''

        for i in self.__artists:
            for j in i.getAlbums():
                listOfAlbums.append(j)

        for i in listOfAlbums:
            songs.append(i.getSongs())
        for i in songs:
            sum = 0
            for j in i:
                sum += j.getLikes()
            likes.append(sum)
        topAlbumlikes = max(likes)

        for i in listOfAlbums:
            checksum = 0
            for j in i.getSongs():
                checksum += j.getLikes()
            if checksum == topAlbumlikes:
                topTrendingAlbum = i
        return topTrendingAlbum
        

    def getTopTrendingSong(self):
        songOfArtists = []
        mostPopularSong = ''
        for i in self.__artists:
            songOfArtists.append(i.mostLikedSong())
        song = songOfArtists[0].getLikes()

        for i in songOfArtists:
            if i.getLikes() > song:
                mostPopularSong = i
        return mostPopularSong    




