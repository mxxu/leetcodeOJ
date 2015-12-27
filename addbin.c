
#include <stdio.h>
#include <string.h>

// ADD FUNC HERE
char* addBinary(char* a, char* b) {
    int m = strlen(a);
    int n = strlen(b);

    int bigger = m;
    if (m < n) {
        bigger = n;
    }

    char* s = new char[bigger+2];
    strcpy(s, m);
    s[m+1] = '\0';
    return s;
}

int main(int argc, const char *argv[])
{
    printf("%s\n", addBinary('11', '1'));
    return 0;
}
