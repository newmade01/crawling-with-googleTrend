from google_images_download import google_images_download   #importing the library

response = google_images_download.googleimagesdownload()   #class instantiation

arguments = {"keywords":"손흥민","limit":50,"print_urls":True, "format": "jpg" }   #creating list of arguments

paths = response.download(arguments)   
print(paths)   #printing absolute paths of the downloaded images

#현재는 업데이트로 웹크롤링 막힘, # Right now, crawling the web on updates blocked.
