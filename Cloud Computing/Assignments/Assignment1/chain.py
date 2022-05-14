from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# recieve a int from the user and add it from process 0 to process i - 1
# ask for another number and do the same
# keep asking until the user inputs a negative 
# each process should print something  
##At some point do error handling in case the value is not a integer




  
while True:
  #In the case that the number of processes specified is 1
  if size == 1:
    try:
      value = int(input())
    except ValueError:
      print("Error: User did not input an integer")
      value = -1
       
    if(value < 0):
      quit()
    print("Process %d got %d\n" % (rank, value))

  else:

    if rank == 0:
      try:
        value = int(input())
      except ValueError:
        print("Error: User did not input an integer")
        value = -1  #In the case the User doesn't input an integer we are going to treat it as a negative value to exit the program
           
      comm.send(value, dest = rank + 1)
    else:
      value = comm.recv(source = rank -1)
      if rank < size - 1:
        comm.send(value, dest = rank + 1)
  
    if value >= 0:
      print ("Process %d got %d\n" % (rank, value))
    
    if(value < 0):
      quit()




#if rank == 0:
 # data = input()
  #comm.send(data, dest=1)
  #print("Message sent, data is : ", data)
#elif rank == 1:
  #data = comm.recv(source=0)
  #print("Message recieved, data is: ", data)






#print("hello world! I am process %d of %d" % (rank, size))