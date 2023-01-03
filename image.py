from PIL import Image
from PIL.ExifTags import TAGS

# open the image
image = Image.open("IMG_20230102_113129.jpg")
print("Meta Data Avalible ")

# extracting the exif metadata
exifdata = image.getexif()

# looping through all the tags present in exifdata
for tagid in exifdata:
	
	# getting the tag name instead of tag id
	tagname = TAGS.get(tagid, tagid)

	# passing the tagid to get its respective value
	value = exifdata.get(tagid)

	# printing the final result
	print(f"{tagname:25}: {value}")


#remove metadata
print("Start of removing  metadata  ")
data = list(image.getdata())
image_without_exif = Image.new(image.mode, image.size)
image_without_exif.putdata(data)
print("all Metadata are eresed ")


#save image

image_without_exif.save('image-without-exif.jpg')
print("Eresed data image save in file name image-without-exif.jpg ")


