#include <iostream>
#include <cmath>
#include <ctime>

int dist;
int speed;

int game_time_secs;
int real_time_secs;

char out_string[100];

int main()
{
    std::setlocale(0, "");

    while(true)
    {
        std::cout << "Enter distance: ";
        std::cin >> dist;
        std::cout << "Enter speed: ";
        std::cin >> speed;

        game_time_secs = ((round((dist / speed)))*60 + (round(((dist / speed) - round((dist / speed))) * 60)))*60;

        real_time_secs = game_time_secs / 10;

        time_t rawtime;
        struct tm * timeinfo;

        rawtime = real_time_secs;

        timeinfo = gmtime(&rawtime);

        std::strftime(out_string, 100, "%H:%M", timeinfo);

        std::cout << out_string << std::endl << std::endl;
    }

    return 0;
}