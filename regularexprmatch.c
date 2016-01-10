#include <stdio.h>
#include <stdbool.h>

bool isMatch(char* s, char* p);

bool isMatchRep(char c, char *s, char* p) {
	do {
		if (isMatch(s, p))
			return true;
	} while (*s != '\0' && (*s++ == c || c == '.'));
	return false;
}

bool isMatch(char* s, char* p) {
	if (*p == '\0')
		return *s == '\0';
	if (p[1] == '*')
		return isMatchRep(p[0], s, p+2);
	if (*s != '\0' && (p[0] == s[0] || p[0] == '.'))
		return isMatch(s+1, p+1);
    return false;
}

int main (int argc, char const *argv[])
{
	printf("%d\n", isMatch("a", "ab*"));
	return 0;
}