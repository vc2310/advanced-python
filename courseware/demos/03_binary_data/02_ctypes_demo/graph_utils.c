#include <stdio.h>
#include <stdlib.h>

typedef struct
{
    int x;
    int y;
} Point;

// x x x x y y y y
// 0 1 2 3 4 5 6 7 (byte position)

void calc_midpoint(Point *start, Point *end, Point *mid)
{
    mid->x = (end->x + start->x) / 2;
    mid->y = (end->y + start->y) / 2;
}
