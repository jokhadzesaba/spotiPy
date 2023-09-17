

from song import *
class Album:
    def __init__(self, title, releaseYear):
        self.__title = title
        self.__releaseYear = releaseYear
        self.__songs = []

    def __str__(self):
        return f'Title:{self.__title}, Release year:{self.__releaseYear}, songs:{"|".join([str(x) for x in self.__songs])}'

    def getTitle(self):
        return self.__title

    def getReleaseYear(self):
        return self.__releaseYear

    def getSongs(self):
        return self.__songs

    def checkIfSameSong(self,song):
            for i in self.__songs:
                if song.getTitle() == i.getTitle() and song.getReleaseYear() == i.getReleaseYear() and song.getDuration() == i.getDuration():
                    return True
            return False

    def addSongs(self,*songs):
        newSongsAdded = 0
        for i in songs:
            if self.checkIfSameSong(i) == False:
                self.__songs.append(i)
                newSongsAdded += 1
        return newSongsAdded


    def sortBy(self, byKey, reverse):
        if reverse == True:
            return self.__songs.sort(key=byKey, reverse=False)
        else:
            return self.__songs.sort(key=byKey, reverse=True)


    def sortByName(self, reverse):
        return self.sortBy(lambda song: song.getTitle(), reverse=reverse)
    def sortByPopularity(self, reverse):
        return self.sortBy(lambda song: song.Likes(), reverse=reverse)
    def sortByduration(self, reverse):
        return self.sortBy(lambda song: song.getDuration(), reverse=reverse)
    def sortByReleaseYear(self, reverse):
        return self.sortBy(lambda song: song.getReleaseYear(), reverse=reverse)

    




    
        
