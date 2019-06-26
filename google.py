from google_images_download import google_images_download

insectFolder = "~/ai-insects/dataset-collection/insects-dataset/"
#creating list of arguments
arguments = {"keywords":"mosquitoes","limit":50,"print_urls":True,output_directory:insectFolder}
arguments.type = "photo"
arguments.print_size = true

response = google_images_download.googleimagesdownload()
absolute_image_paths = response.download(arguments)