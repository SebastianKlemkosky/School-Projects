// gcc -Wall mmm5.c -o /tmp/mmm5
// /tmp/mmm5 34 82 -4 -22 13 -83 0 3
// prints: Smallest positive=3 Largest negative=-4

#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

typedef struct MMM {
  int smallPos;      // Smallest positive number is 1
  int largeNeg;      // Largest negative number is -1
} mmm_t;

static mmm_t *mmm5(int argc, char *argv[]) {
  mmm_t *mmm = (mmm_t *) malloc(sizeof(mmm_t));
  int i;
  mmm->smallPos = INT_MAX;
  mmm->largeNeg = INT_MIN;
  for (i = 1; i < argc; i++) {
    int n = atoi(argv[i]);
TBD
}
  return mmm;
}

int main(int argc, char *argv[]) {
TBD call to mmm5()
  printf("Smallest positive=%d Largest negative=%d\n", mmm->smallPos, mmm->largeNeg);
  return 0;
}
