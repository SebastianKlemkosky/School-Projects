import os
from hashlib import sha1
from mpi4py import MPI
import numpy as np
from PIL import Image
from array import *

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()


#This finds a folder called images and creates a list of the image file names if they end with a png
image_folder = os.path.join(os.getcwd(), 'images')
image_files = [_ for _ in os.listdir(image_folder) if _.endswith('png')]
image_path_dup_list = []

if rank == 0:
  #rank 0 will open and find the original image 
  orig_image_path = os.path.join(image_folder, '0.9.png')  #dot.png is the current test image we are using
  orig_image = Image.open(orig_image_path)
  orig_image_array = np.asarray(orig_image)

  match = sha1(orig_image_array).hexdigest()
  #print(match)

  chunk = len(image_files) // size
  image_files = [image_files[c:c + chunk] for c in range(0, len(image_files), chunk)]
  
  for x in range(size):
    comm.send(image_files[x],dest=x, tag=12)
    comm.send(match,dest=x, tag=11)
    comm.send(orig_image_path,dest=x, tag=13)
    #print("Sent to  rank %d" % (x))

imagelist = comm.recv(source=0, tag = 12)
match = comm.recv(source=0, tag = 11)
orig_image_path = comm.recv(source=0, tag = 13)

#run a for loop for every file in the list imagelist
for i in imagelist:
  cur_image_path = os.path.join(image_folder, i)
  cur_image = Image.open(cur_image_path)
  image_array = np.asarray(cur_image)
  cur_image_hash = sha1(image_array).hexdigest()
  
  if cur_image_hash == match and cur_image_path != orig_image_path:
    #print("A dup image was found on rank %d at %s" %(rank,cur_image_path));
    image_path_dup_list.append(cur_image_path)
    

comm.Barrier() 
image_path_dup_list = comm.gather(image_path_dup_list, root = 0)

 
if rank == 0:

  print("Duplicate Images are found at")
  
  for i in range(len(image_path_dup_list)) : 
    for j in range(len(image_path_dup_list[i])) : 
      if image_path_dup_list[i][j] != "":
        print(image_path_dup_list[i][j])
     
    
  

  
    
