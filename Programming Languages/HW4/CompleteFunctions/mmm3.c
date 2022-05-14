// gcc -Wall mmm3.c -o /tmp/mmm3
// /tmp/mmm3 34 82 -4 -22 13 -83 0 3
// prints: Smallest positive=3 Largest negative=-4

#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

typedef struct {
  int smallPos;      // Smallest positive number is 1
  int largeNeg;      // Largest negative number is -1
} mmm_t;

static mmm_t *mmm3(int argc, char *argv[]) {
  static mmm_t mmm;
  int i;

  mmm.smallPos = INT_MAX;
  mmm.largeNeg = INT_MIN;
  for (i = 1; i < argc; i++) {
    int n = atoi(argv[i]);
    if(mmm.smallPos > n && n > 0) mmm.smallPos = n;
     
    if(mmm.largeNeg < n && n < 0) mmm.largeNeg = n;
      
  }
  return &mmm;
}

int main(int argc, char *argv[]) {
  mmm_t *mmm = mmm3(argc, argv);
  printf("Smallest positive=%d Largest negative=%d\n", mmm->smallPos, mmm->largeNeg);
  return 0;
}
