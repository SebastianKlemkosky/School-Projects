from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

sendbuf = None

if size != 4:
  print("Number of processes must be 4")
  quit()

#chunk = 24/size #change this to 40k after tests
chunk = 40000//size

if rank == 0:
  sendbuf = np.loadtxt('data', dtype=int)
  sendbuf = sendbuf.astype(int) 
  np.array_split(sendbuf, size)
  


recvbuf = np.empty(chunk, dtype=int)
recvbuf = recvbuf.astype(int) 
comm.Scatter(sendbuf, recvbuf, root=0)


comm.Barrier()
#Start Search
for i in range(len(recvbuf)):
  if comm.Iprobe(source = 0, tag=11) or comm.Iprobe(source = 1, tag=11) or comm.Iprobe(source = 2, tag=11) or comm.Iprobe(source = 3, tag=11):
    print("Process %d stopped searching at index %d" % (rank, i))
    quit()
  if recvbuf[i] == 11:
      print("Process %d found %s on index %d" % (rank, recvbuf[i], i))
      for r in range(size):
        comm.isend(0, dest=r, tag=11)
      quit()
if i == len(recvbuf) -1:
  print("Process %d reached index %d of search and couldn't find 11" % (rank,i))
  
#This program works on the fox machines and outputs correctly
#need to try this one on the CC servers