#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>

int comptelettre(char *s)
{
	int i = 0;
	while (s[i])
		i++;
	return (i);
}

/*char *copie(char *copie, char *source)
{
	int i = 0;
	printf("source = %s\n", source);
	while (source[i])
	{
		copie[i] = source[i];
		i++;
	}
	return (copie);
}

void ecrit(char *s)
{
	int i = 0;
	while (s[i])
	{	
		write(1, &s[i], 1);
		i++;
	}
}*/

void inverse(char *s)
{
	int i = comptelettre(s);
	int j;
	int premier_mot = 0;
	//char *res = malloc(comptelettre(s + 1) * sizeof(char));
	while (i >= 0)
	{
		while (s[i] == ' ' || s[i] == '\t')
			i--;
		j = i;
		while (j >= 0 && s[j] != ' ' && s[j] != '\t')
			j--;
		if (premier_mot)
			write(1, " ", 1);
		//ecrit(copie(res, &s[j + 1]));
		//printf("j + 1) = %d\ni - j = %d\nres = %s\n", j, i - j, &s[j]);
		write(1, &s[j + 1], i - j);
		premier_mot = 1;
		i = j;
		i--;
	}
}

int main(int ac, char **av)
{
	int i = 1;
	if (ac > 1)
	{
		while (i < ac)
		{
			char *s = av[i];
			inverse(s);
			i++;
		}
	}
	write(1, "\n", 1);
	return (0);
}
