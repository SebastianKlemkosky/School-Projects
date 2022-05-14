// gcc -Wall mmm1.c -o /tmp/mmm1
// /tmp/mmm1 34 82 -4 -22 13 -83 0 3
// prints: Smallest positive=3 Largest negative=-4

#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

// Find the smallest positive number
static int small(int argc, char *argv[]) {
  int smallest = INT_MAX;
  int i;
  for (i = 1; i < argc; i++) {
    int n = atoi(argv[i]);
TBD
  }
  return smallest;
}

// Find the largest negative number
static int large(int argc, char *argv[]) {
  int largest = INT_MIN;
  int i;
  for (i = 1; i < argc; i++) {
    int n = atoi(argv[i]);
TBD
  }
  return largest;
}

int main(int argc, char *argv[]) {
TBD calls to small() and large()
  printf("Smallest positive=%d Largest negative=%d\n", smallPos, largeNeg);
  return 0;
}
