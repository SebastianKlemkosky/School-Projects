// gcc -Wall mmm6.c -o /tmp/mmm6
// /tmp/mmm6 34 82 -4 -22 13 -83 0 3
// prints: Smallest positive=3 Largest negative=-4

#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

static void mmm6(int argc, char *argv[], int *smallPos, int *largeNeg) {
  int i;
  *smallPos = INT_MAX;
  *largeNeg = INT_MIN;
  for (i = 1; i < argc; i++) {
    int n = atoi(argv[i]);
TBD
  }
}

int main(int argc, char *argv[]) {
  int smallPos;
  int largeNeg;
TBD call to mmm6()
  printf("Smallest positive=%d Largest negative=%d\n", smallPos, largeNeg);
  return 0;
}