// gcc -Wall mmm4.c -o /tmp/mmm4
// /tmp/mmm4 34 82 -4 -22 13 -83 0 3
// prints: Smallest positive=3 Largest negative=-4

#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

typedef struct MMM {
  int smallPos;      // Smallest positive number is 1
  int largeNeg;      // Largest negative number is -1
} mmm_t;

static void mmm4(int argc, char *argv[], mmm_t *mmm) {
  int i;
  
  mmm->smallPos = INT_MAX;
  mmm->largeNeg = INT_MIN;
  for (i = 1; i < argc; i++) {
    int n = atoi(argv[i]);
    if(mmm->smallPos > n && n > 0) mmm->smallPos = n;
     
    if(mmm->largeNeg < n && n < 0) mmm->largeNeg = n;
      
  }
}

int main(int argc, char *argv[]) {
  mmm_t mmm;
  mmm4(argc, argv, &mmm);
  printf("Smallest positive=%d Largest negative=%d\n", mmm.smallPos, mmm.largeNeg);
  return 0;
}
