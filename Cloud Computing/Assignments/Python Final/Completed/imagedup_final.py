
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
  print("Enter the image name: ")
  user_input = input()
  try:
    orig_image_path = os.path.join(image_folder, user_input)        #The original image will be converted to a matrix list of RGB values per pixel. 
    orig_image = Image.open(orig_image_path)
    orig_image_array = np.asarray(orig_image)
    #print(orig_image_array)
    
    match = sha1(orig_image_array).hexdigest()                       #Convet this matrix to sha1 hash to be used to match
    #print(match)
                  
  
    


    chunk = len(image_files) // size
    image_files = [image_files[c:c + chunk] for c in range(0, len(image_files), chunk)]
  
    for x in range(size):
      comm.send(image_files[x],dest=x, tag=12)
      comm.send(match,dest=x, tag=11)
      comm.send(orig_image_path,dest=x, tag=13)
      comm.isend(1, dest=x, tag=14)
      #print("Sent to  rank %d" % (x))

  except IOError:
    print("User did not input a valid file name")
    for r in range(size):
      comm.isend(0, dest=r, tag=14) 

comm.Barrier() 
if comm.recv(source=0, tag = 14) == 0:
  print("Process %d stopped" % (rank))
  quit()
   
imagelist = comm.recv(source=0, tag = 12)
match = comm.recv(source=0, tag = 11)
orig_image_path = comm.recv(source=0, tag = 13)

#run a for loop for every file in the list imagelist #This does the same as above in rank 0 but for every image in the image folder
for i in imagelist:                                                                  
  cur_image_path = os.path.join(image_folder, i)                                     
  cur_image = Image.open(cur_image_path)
  image_array = np.asarray(cur_image)
  cur_image_hash = sha1(image_array).hexdigest()
  
  if cur_image_hash == match and cur_image_path != orig_image_path:                  #IF a match occurs and it's not the same image as the original 
    #print("A dup image was found on rank %d at %s" %(rank,cur_image_path));          #Add to a list to be printed later
    image_path_dup_list.append(cur_image_path)
    

comm.Barrier() 
image_path_dup_list = comm.gather(image_path_dup_list, root = 0)


if rank == 0:
                                                                                        #Print the list
  print("Duplicate Images are found at")
  for i in range(len(image_path_dup_list)) : 
    for j in range(len(image_path_dup_list[i])) : 
      if image_path_dup_list[i][j] != "":
        print(image_path_dup_list[i][j])

    
    