#include <stdio.h>
#include <stdlib.h>
#include <wiringPi.h>




int main(int argc, char *argv[])
    {
    //char *a = argv[1];
    //int ms_delay = atoi(a);
    wiringPiSetupGpio() ;

    int pin1 = 6;
    int pin2 = 19;


    pinMode(pin1, OUTPUT) ;
    pinMode(pin2, OUTPUT) ;
    delay(200);
    digitalWrite(pin1,HIGH);
    digitalWrite(pin2,HIGH);

    int step_sequence[4][2] =
        {
            {0, 0},
            {0, 1},
            {1, 0},
            {1, 1},
        };

    int pins[2] = {pin1, pin2};

    int step_count = 10000000;
    int i;
    for (i=0;i<step_count;i++)
        {
            int step_nr = i % 4;
            int pin = 0;
            for (pin=0; pin <2; pin++)
                {
                    if (step_sequence[step_nr][pin] == 0)
                        {
                            digitalWrite(pins[pin], LOW);
                        }
                    else
                        {
                            digitalWrite(pins[pin], HIGH);
                        }

                }



        /*delayMicroseconds(10000);*/
        delay(500);
        }








    digitalWrite(pin1,LOW);
    digitalWrite(pin2,LOW);
    delay(200);
    pinMode(pin1,INPUT);
    pinMode(pin2,INPUT);
    delay(200);


    return 0 ;
    }

