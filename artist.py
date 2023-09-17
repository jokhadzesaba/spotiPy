
from album import *

class Artist:
    def __init__(self, firstName, lastName, birthYear, album, singles):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__birthYear = birthYear
        self.__album = album
        self.__singles = singles

    def getFirstName(self):
        return self.__firstName
    def getSecondName(self):
        return self.__lastName
    def getBitrhYear(self):
        return self.__birthYear
    def getAlbums(self):
        return self.__album
    def getSingle(self):
        return self.__singles
    def getAllSong(self):
        lstOfSongs = []
        for i in self.__singles:
            lstOfSongs.append(i)
        for i in self.__album:
            for j in i.getSongs():
                lstOfSongs.append(j)
        return lstOfSongs
    

    def mostLikedSong(self):
        lstOfSongs = []
        for i in self.__singles:
            lstOfSongs.append(i)
        for i in self.__album:
            for j in i.getSongs():
                lstOfSongs.append(j)
        mostLiked = lstOfSongs[0]
        for i in lstOfSongs:
            if i.getLikes() > mostLiked.getLikes():
                mostLiked = i
        return mostLiked

    def LeastLikedSongs(self):
        lstOfSongs = []
        for i in self.__singles:
            lstOfSongs.append(i)
        for i in self.__album:
            for j in i.getSongs():
                lstOfSongs.append(j)
        leastLiked = lstOfSongs[0]
        for i in lstOfSongs:
            if i.getLikes() < leastLiked.getLikes():
                leastLiked = i
        return leastLiked

    def TotalLikes(self):
        lstOfSongs = []
        sumOfLikes = 0
        for i in self.__singles:
            lstOfSongs.append(i)
        for i in self.__album:
            for j in i.getSongs():
                lstOfSongs.append(j)
        for songs in lstOfSongs:
            sumOfLikes += songs.getLikes()
        return sumOfLikes

    def __str__(self):
        return f'Name:{self.getFirstName()}, Lastname:{self.getSecondName()}, year:{self.getBitrhYear()}, Total likes:{self.TotalLikes()}'
        
    def sumOflikesFromAlbum(self, songsfromalbum):
            sum = 0
            for i in songsfromalbum.getSongs:
                    sum + i.getLikes()
            return sum


    

        
    
