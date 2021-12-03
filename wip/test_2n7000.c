#include <stdio.h>
#include <stdlib.h>
#include <wiringPi.h>




int main(int argc, char *argv[])
    {
    //char *a = argv[1];
    //int ms_delay = atoi(a);
    wiringPiSetupGpio() ;




    pinMode(6, OUTPUT) ;
    pinMode(19, OUTPUT) ;
    delay(200);
    digitalWrite(6,HIGH);
    digitalWrite(19,HIGH);


    int big_loop = 0;
    for (big_loop = 0; big_loop < 100000; big_loop++)
        {
            digitalWrite(6,HIGH);
            delayMicroseconds(700);
            //delay(200);
            digitalWrite(6,LOW);
            delayMicroseconds(700);
            //delay(200);
        }

    digitalWrite(6,LOW);
    digitalWrite(19,LOW);
    delay(200);
    pinMode(6,INPUT);
    pinMode(19,INPUT);
    delay(200);


    return 0 ;
    }

