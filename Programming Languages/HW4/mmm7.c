// gcc -Wall mmm7.c -o /tmp/mmm7
// /tmp/mmm7 34 82 -4 -22 13 -83 0 3
// prints: Smallest positive=3 Largest negative=-4

#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

#define mmm7(argc, argv, smallPos, largeNeg) \
  smallPos = INT_MAX; \
  largeNeg = INT_MIN; \
  int i; \
  for (i = 1; i < argc; i++) { \
    int n = atoi(argv[i]); \
TBD
  }
  
int main(int argc, char *argv[]) {
  int smallPos;
  int largeNeg;
TBD call to mmm7()
  printf("Smallest positive=%d Largest negative=%d\n", smallPos, largeNeg);
  return 0;
}
