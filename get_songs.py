
#!/usr/bin/env python3
# This program coded by  Burak Can Bülbül  only to improve myself.
import os
from bs4 import BeautifulSoup
import requests
import  random


class Songs():
#
 def get_files(self,path):

    st_dir=os.getcwd()
    files=[]

    os.chdir(path)

    for f in os.listdir(os.curdir):
        if not os.path.isdir(path):
            files.append(f)
        else:
            files.extend(self.get_files(f))

    os.chdir(st_dir)

    return files


 def filter_songs(self):
     path='/home/burakcan/Desktop/Müzikler'
     files_list=self.get_files(path)
     song_list=[]
     for isSong in files_list:
         if isSong.endswith(".mp3"):
            #print(isSong)
            song_list.append(isSong)

    # for i in range(song_list.__len__()):
     #   print(song_list.__getitem__(i))
     return song_list

 def get_path(self):
     path='/home/burakcan/Desktop/Müzikler'
     return path
 def count_songs(self):

     return len(self.filter_songs())


 def get_songs_abs_path(self):

     abs_paths=[]
     path="/home/burakcan/Desktop/Müzikler"
     os.chdir(path)
     get_songs=self.filter_songs()
     for songs in get_songs:
         if songs is not None:
            abs_paths.append(os.path.abspath(songs))
     #for i in range(abs_paths.__len__()):
      #   print(abs_paths.__getitem__(i))
     return abs_paths


 def get_song_index_abs_path(self,index):

     abs_path=self.get_songs_abs_path()

     return abs_path[index]


 def search_song(self,name):
     song_list=self.filter_songs()
     searching_list=[]
     for i in range(song_list.__len__()):

         if name.lower() in song_list.__getitem__(i).lower() or\
                         name.upper() in song_list.__getitem__(i).upper():
            searching_list.append(song_list.__getitem__(i))


   #  for i in range(searching_list.__len__()):
    #  print(searching_list.__getitem__(i))

     return searching_list

 def listing_all_music_singers(self):
     song_list=self.filter_songs()
     singer_list=[]
     filter_list=[]
     for name in song_list:
         a=name.split('-')
         singer_list.append(a[0])

     for searching in singer_list:

         for j in range(singer_list.__len__()):

             if singer_list.__getitem__(j) is searching and not filter_list.__contains__(searching) :

                 filter_list.append(singer_list.__getitem__(j))

     return filter_list

 def delete_song(self,song_name):
    search_list=str(self.search_song(song_name))
    song_list=self.filter_songs()
    index=0
    for search in song_list:
        if search_list.__contains__(search):
            break
        else:
            index+=1

    abs_path=self.get_song_index_abs_path(index)
    del_file=song_list[index]
    print(abs_path)
    print("Deleting this Music, in your list : ",song_list[index])
    del song_list[index]
    print("Deleted")
    print(os.listdir(os.curdir))
    os.chdir('yeni müz')
    os.remove(del_file)


 def get_status(self,path):

 # status for your path

  return print(os.stat(path))


 def get_information_for_singer(self,singer_name):

     #Information about searching singer from Wikipedia.
   link="https://tr.wikipedia.org/wiki/"+singer_name
   r=requests.get(link)
   print(r.url)
   information=""
   soup=BeautifulSoup(r.content,'html.parser')
   soup.prettify()
   for inf in soup.find_all('div',id='mw-content-text'):
        for p in inf.find_all('p'):
             print(p.get_text())


  def get_random_song(self):
      song_list=self.filter_songs()
      random_choice=random.choice(song_list)
      print(random_choice)
      return random_choice


  def get_random_shuffling(self):
      song_list=self.filter_songs()
      shuffling_list=random.shuffle(song_list)
      return shuffling_list

  def get_random_sample(self,sample):

      song_list=self.filter_songs()
      sample_list=random.sample(song_list,sample)
      return sample_list



s=Songs()
s.get_random_song()
#print(s.get_song_index_abs_path(3))

#list =s.filter_songs()

#s.listing_all_music_singers()


#s.delete_song('dale papi')

#s.get_information_for_singer('Loreen')






