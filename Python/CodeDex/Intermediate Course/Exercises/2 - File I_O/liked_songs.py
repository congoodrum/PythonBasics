# Write code below 💖

liked_songs = {
  'Bad Habits' : 'Ed Sheeran',
  'I\'m Just Ken':'Ryan Gosing',
  'Mastermind ':'Taylor Swift',
  'Uptown Funk':'Mark Ronson ft. Bruno Mars',
  'Ghost ':'Justin Bieber'
}

def write_liked_songs_to_file(liked_songs: dict, file_name):
  with open(file_name, 'w') as f:
    for song, artist in liked_songs.items():
      f.writelines(f"{song} by {artist}\n")


write_liked_songs_to_file(liked_songs, 'liked_songs.txt')