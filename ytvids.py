from pytube import YouTube 
import os
import math
def ytdownload():
    try:    
        yturl = input("Enter the youtube link URL: ")
        ytvid = YouTube(yturl)

        print(f"Title: {ytvid.title}")
        videos = ytvid.streams.filter(progressive=True, res="720p") #can be edited accordingly (progressive == True indicates audio ) 

        valid_options=[]
        

        for i,video in enumerate(videos):
            print(f"{int(i)} {str(video)}")
            valid_options.append(int(i))


        print(valid_options)
        num = int(input("Enter your choice: "))

        if num in valid_options:
            video = videos[num]
            print("Downloading the video. Please wait...")
            print()
            video.download()
            size = video.filesize
            size = size/(1024*1024)
            size = round(size, 2)

            print(f"Download Size: {size} MB")
            print("Download completed..")

    except Exception as e:
        print("Please enter a valid choice")
        print()
        ytdownload()

ytdownload()

