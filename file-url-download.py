import requests
import pyperclip
import os

#enter url of file you want to download
file_url = ""
dest_folder = "download_test"

def download_url(file_url,dest_folder):
	# if file_url not given take from clipboard
	if file_url == "":
		file_url = pyperclip.paste()

	# make folder if it does not exist 
	if not os.path.exists(dest_folder):
		os.makedirs(dest_folder)

	response = requests.get(file_url)

	if response.ok:

		file_name = file_url.split('/')[-1].replace(" ", "_")

		file_path = os.path.join(dest_folder,file_name)
		
		print("saving file as:", os.path.abspath(file_path))
		print("\nFolder location copied to clipboard")
		pyperclip.copy(os.path.abspath(dest_folder))

		with open(file_path,"wb") as f:
			for chunk in response.iter_content(chunk_size = 16*1024):
				f.write(chunk)
		f.close()
	else:
		print("Download failed status code {}\n{}".format(response.status_code,response.text))

download_url(file_url,dest_folder)