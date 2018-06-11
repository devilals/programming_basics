#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <ctype.h>

bool isAnagram (char * str1, char * str2)
{
    int len1, i;
    int checkChar [256] = {0};
    if (str1 == NULL || str2 == NULL)
        return false;
    len1 = strlen(str1);
    if (len1<2 || len1 != strlen(str2))
        return false;
        
    for(i=0; i<len1; i++)
    {
        checkChar[toascii(str1[i])]++;
        checkChar[toascii(str2[i])]--;
    }
 
    for(i=0; i<256; i++)
    {
        if(checkChar[i])
            return false;
    }
    return true;
}
int main(void)
{
	printf("Program to find if two strings are anagram\n");
	char * str1 = "geeksforgeeks";
	char * str2 = "geeksgeeforks";
	bool result = isAnagram(str1, str2);
	if (result == true)
	    printf("strings are anagram\n");
	else
	    printf("strings are NOT anagram\n");
	    
	return 0;
}





