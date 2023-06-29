#include <stdio.h>
#include <string.h>

#define FLAG_LENGTH 38
#define KEY_LENGTH 6

unsigned char keys[KEY_LENGTH] = {49, 53, 49, 50, 51, 53};
unsigned char flag[FLAG_LENGTH] = {85, 80, 83, 71, 84, 106, 85, 80, 83, 71, 84, 106, 95, 106, 85, 87, 81, 64, 86, 106, 87, 93, 65, 106, 69, 93, 84, 109, 88, 80, 72, 106, 80, 7, 0, 81, 87, 84};

int main(int argc, char **argv)
{
    if (argc < 2)
    {
        fprintf(stderr, "Usage: %s <pin>\n", *argv);
        return -1;
    }

    if (!strncmp(argv[1], keys, KEY_LENGTH))
    {
        for (int i = 0; i < FLAG_LENGTH; i++)
            flag[i] ^= keys[i % KEY_LENGTH];

        printf("ForestyCTF{%s}\n", flag);
        return 0;
    }

    puts("Nope!");
    return -1;
}