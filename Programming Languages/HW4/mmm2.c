// gcc -Wall mmm2.c -o /tmp/mmm2
// /tmp/mmm2 34 82 -4 -22 13 -83 0 3
// prints: Smallest positive=3 Largest negative=-4

#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

static int smallPos;      // Smallest positive number is 1
static int largeNeg;      // Largest negative number is -1

static void mmm2(int argc, char *argv[]) {
  int i;
  
  smallPos = INT_MAX;
  largeNeg = INT_MIN;
  for (i = 1; i < argc; i++) {
    int n = atoi(argv[i]);
TBD
  }
}

int main(int argc, char *argv[]) {
TBD call to mmm2()
  printf("Smallest positive=%d Largest negative=%d\n", smallPos, largeNeg);
  return 0;
}
