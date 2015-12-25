#include <stdio.h>

char *my_strstr(const char *s1, const char *s2)
{
    if (!s1 || !s2)
        return NULL;
    while (*s1 != '\0')
    {
        char *p1 = s1;
        char *p2 = s2;
        while (*(p1++) == *(p2++));
        if (*p2 == '\0')
            return s1;
        s1++;
    }
    return NULL;
}

int main(int argc, const char *argv[])
{
    printf("%s\n", my_strstr("abcd", "cd"));
    return 0;
}
