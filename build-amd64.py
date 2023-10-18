import os
import gzip
import lzma
import requests
import shutil

# Function to change xz into gz
def convert_tar_xz_to_tar_gz(xz_file_path, gz_file_path):
    # Open the .tar.xz file for reading
    with lzma.open(xz_file_path, 'rb') as xz_file:
        # Create a gzip compressed .tar.gz file for writing
        with gzip.open(gz_file_path, 'wb') as gz_file:
            # Copy the contents from the .tar.xz file to the .tar.gz file
            shutil.copyfileobj(xz_file, gz_file)

# Create the folder and enter
os.makedirs('eweoswsl', exist_ok=True)
os.chdir('eweoswsl')



# Download wsldl.exe
print('Downloading wsldl...')
exe_url = 'https://github.com/yuk7/wsldl/releases/download/23072600/wsldl.exe'
exe_filename = 'wsldl.exe'

if not os.path.exists(exe_filename):
  response = requests.get(exe_url)
  response.raise_for_status()  # check the connection

  with open(exe_filename, 'wb') as file:
      file.write(response.content)
else:
    print('wsldl.exe exsists.')


# Download the eweOS' rootfs
print('Downloading rootfs...')
xz_url = 'https://os-repo.ewe.moe/eweos-images/x86_64/eweos-x86_64-tarball-Build60.2.xz'
xz_filename = 'eweos-x86_64-tarball-Build60.2.xz'
if not os.path.exists(xz_filename):
  response = requests.get(xz_url)
  response.raise_for_status()  # check the connection

  with open(xz_filename, 'wb') as file:
      file.write(response.content)
else:
    print('rootfs exsists.')

# Change the rootfs xz into gz file
xz_file_path = 'eweos-x86_64-tarball-Build60.2.xz' 
gz_file_path = 'rootfs.tar.gz'

if not os.path.exists(gz_file_path):
  convert_tar_xz_to_tar_gz(xz_file_path, gz_file_path)
else:
    print('rootfs exsists.')

print('Done!')
