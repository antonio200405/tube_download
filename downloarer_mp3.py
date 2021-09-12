from pytube import YouTube

#ask for the link from user
link = input("Enter the link of YouTube video you want to download:  ")
yt = YouTube(link)

#Showing details
print("Title: ",yt.title)
print("Number of views: ",yt.views)
print("Length of video: ",yt.length)
print("Rating of video: ",yt.rating)
#Getting the highest resolution possible

#print(yt.streams.filter(only_video=True))
#ys = yt.streams.get_highest_resolution()

vids= yt.streams.all()
for i in range(len(vids)):
    print(i,'. ',vids[i])

vnum = int(input("Enter vid num: "))



#Starting download
print("Downloading...")
vids[vnum].download()
print("Download completed!!")

file_object = open('link.txt', 'ab')
file_object.write(bytes(link, encoding="raw_unicode_escape")+bytes(":", encoding="raw_unicode_escape")+ bytes(yt.title, encoding="raw_unicode_escape"))
file_object.close()