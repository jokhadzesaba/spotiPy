class Song:
    def __init__(self, title, releaseYear, duration= 60, likes = 0):
        self.__title = title
        self.__releaseYear = releaseYear
        self.__duration = duration
        self.__likes = likes

    def getTitle(self):
        return self.__title

    def getReleaseYear(self):
        return self.__releaseYear

    def getDuration(self):
        return self.__duration

    def getLikes(self):
        return self.__likes

    def like(self):
        self.__likes += 1
        return self.__likes

    def unlike(self):
        self.__likes -= 1
        return self.__likes

    def setDuration(self, newDuration):
        if newDuration < 0 or newDuration == self.__duration or newDuration > 720: 
            return False
        else:
            self.__duration = newDuration
            return True, newDuration
    def __str__(self):
        return f'Title:{self.__title}, Duration:{self.__duration/60} minutes , Release Year:{self.__releaseYear}, Likes:{self.__likes}' 
        
        









    
