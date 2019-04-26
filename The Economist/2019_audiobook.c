/*
 *    The Economist Audio Edition Download Links
 *
 *    http://audiocdn.economist.com/sites/default/files/AudioArchive/2019/20190105/Issue_9124_20190105_The_Economist_Full_edition.zip

*/

#include <stdio.h>
#include <time.h>
#define YEAR 2019
#define LOOP    52
int main()
{
    int months[12] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    int year_day = 5;
    int series = 9124;
    int weeks = 0, j = 0;
    int this_month = months[j];
    int last_month = 0;
    int month_day = year_day;
    int year = YEAR;
    for(; weeks <= LOOP; weeks++)
    {
        if(year_day > this_month)
        {
            j++;
            if(j == 12)
            {
                year++;
                j = 0;
            }
            last_month = this_month;
            this_month += months[j];

        }
        month_day = year_day - last_month;

//        printf("经济学人发行日： %04d年%02d月%02d日\n", year, j+1, month_day);
        printf("http://audiocdn.economist.com/sites/default/files/AudioArchive/%04d/%04d%02d%02d/Issue_%04d_%04d%02d%02d_The_Economist_Full_edition.zip\n", year, year, j+1, month_day, series, year, j+1, month_day);
        year_day += 7;
        series += 1;
    }
    return 0;
}
