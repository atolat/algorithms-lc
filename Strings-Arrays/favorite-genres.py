# Given a map Map<String, List<String>> userSongs with user names as keys and a list of all the songs that the user has listened to as values.

# Also given a map Map<String, List<String>> songGenres, with song genre as keys and a list of all the songs within that genre as values. The song can only belong to only one genre.

# The task is to return a map Map<String, List<String>>, where the key is a user name and the value is a list of the user's favorite genre(s). Favorite genre is the most listened to genre. A user can have more than one favorite genre if he/she has listened to the same number of songs per each of the genres.

# Example 1:

# Input:
# userSongs = {  
#    "David": ["song1", "song2", "song3", "song4", "song8"],
#    "Emma":  ["song5", "song6", "song7"]
# },
# songGenres = {  
#    "Rock":    ["song1", "song3"],
#    "Dubstep": ["song7"],
#    "Techno":  ["song2", "song4"],
#    "Pop":     ["song5", "song6"],
#    "Jazz":    ["song8", "song9"]
# }

# Output: {  
#    "David": ["Rock", "Techno"],
#    "Emma":  ["Pop"]
# }

# Explanation:
# David has 2 Rock, 2 Techno and 1 Jazz song. So he has 2 favorite genres.
# Emma has 2 Pop and 1 Dubstep song. Pop is Emma's favorite genre.
# Example 2:

# Input:
# userSongs = {  
#    "David": ["song1", "song2"],
#    "Emma":  ["song3", "song4"]
# },
# songGenres = {}

# Output: {  
#    "David": [],
#    "Emma":  []
# }

# TIME COMPLEXITY: O(User * (Song * Genres))
# SPACE COMPLEXITY: O(n * m + m * s), where n is the number of users, and m is the amount of genres, and s is the number of songs.

from collections import defaultdict
def favoriteGenres(userSongs, songGenres):
    results = defaultdict(int)
    for user in userSongs:
        songs = userSongs[user]
        genreCount = defaultdict(int)
        for song in songs:
            for genre in songGenres:
                if song in songGenres[genre]:
                    genreCount[genre] += 1
        
        results[user] = [key for key, val in genreCount.items() if val == max(genreCount.values())]    
                    
    return dict(results)

userSongs = userSongs = {  
   "David": ["song1", "song2", "song3", "song4", "song8"],
   "Emma":  ["song5", "song6", "song7"]
}

songGenres = songGenres = {  
   "Rock":    ["song1", "song3"],
   "Dubstep": ["song7"],
   "Techno":  ["song2", "song4"],
   "Pop":     ["song5", "song6"],
   "Jazz":    ["song8", "song9"]
}

print(favoriteGenres(userSongs, songGenres))