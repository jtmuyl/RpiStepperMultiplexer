#include <stdio.h>
#include <stdlib.h>
#include <wiringPi.h>
int main(int argc, char *argv[])
{
  char *a = argv[1];
  int ms_delay = atoi(a);
  wiringPiSetupGpio() ;
  pinMode(6, OUTPUT) ;

  while (0<1)
  {
    //printf("start");
    digitalWrite(6, HIGH) ; delayMicroseconds(ms_delay) ;
    //printf("HIGH");
    digitalWrite(6,  LOW) ; delayMicroseconds(ms_delay) ;
    //printf("LOW");
  }
  return 0 ;
}