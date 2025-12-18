/* ********************************************************** */
/*                                                            */
/* ✨  GRIMOIRE DES SORTS : premier_mot.c             ✨      */
/*                                                            */
/* Créé pour : Le Scribe                                      */
/* Rédigé par : Le Mage ldauber                               */
/* Date de rédaction : 18/12/2025 10:51                       */
/*                                                            */
/* ********************************************************** */

#include <stdio.h>

void premier_mot(char *s)
{
	int i = 0;
	while (s[i])
	{
		while (s[i] == 32 || s[i] == 9)
			i++;
		while ((s[i] >= 65 && s[i] <= 90) || (s[i] >= 97 && s[i] <= 122))
		{
			printf("%c", s[i]);
			if (s[i + 1] == 32 || s[i + 1] == 9)
				return  ;
			i++;
		}
		i++;
	}
}

int main(int ac, char **av)
{
	int i = 1;
	if (ac > 1)
	{
		while (i < ac)
		{
			premier_mot(av[i]);
			i++;
		}
	}
	else
		printf("Scribe, il n'y a pas de phrase\n");
	return (0);
}

