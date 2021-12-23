#include <wiringPi.h>
#define LED 4

int main (void)
{
  //wiringPiSetup () ;
  wiringPiSetupGpio() ;
  pinMode (LED, OUTPUT) ;
  for (int i=0; i<5; i++)
  {
    digitalWrite (LED, HIGH) ; delay(1000);
    digitalWrite (LED,  LOW) ; delay(1000);
  }
  return 0 ;
}