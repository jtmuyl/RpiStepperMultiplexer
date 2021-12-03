#include <stdio.h>
#include <stdlib.h>
#include <wiringPi.h>




int main(int argc, char *argv[])
    {
    //char *a = argv[1];
    //int ms_delay = atoi(a);
    wiringPiSetupGpio() ;

    int pin1 = 18;
    int pin2 = 23;
    int pin3 = 24;
    int pin4 = 25;
    pinMode(pin1, OUTPUT) ;
    pinMode(pin2, OUTPUT) ;
    pinMode(pin3, OUTPUT) ;
    pinMode(pin4, OUTPUT) ;

    pinMode(6, OUTPUT);
    delay(200);
    digitalWrite(6,HIGH);
    delay(200);

    int pins[4] = {pin1, pin2, pin3, pin4};

    int step_count = 40960;

    int step_sequence[8][4] =
        {
            {1, 0, 0, 1},
            {1, 0, 0, 0},
            {1, 1, 0, 0},
            {0, 1, 0, 0},
            {0, 1, 1, 0},
            {0, 0, 1, 0},
            {0, 0, 1, 1},
            {0, 0, 0, 1}
        };


    int big_loop = 0;
    for (big_loop = 0; big_loop < 10; big_loop++)
        {
            printf("%d", big_loop);
            int i = 0;
            for (i=0;i<step_count;i++)
                {
                int step_nr = i % 8;
                int pin = 0;
                for (pin=0; pin <4; pin++)
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
                delayMicroseconds(750);


                }
            delay(200);
        }
    delay(200);
    pinMode(6,INPUT);
    delay(200);

    int pin = 0;
    for (pin=0; pin <4; pin++)
        {
            pinMode(pins[pin], INPUT);
        }


    return 0 ;
    }

