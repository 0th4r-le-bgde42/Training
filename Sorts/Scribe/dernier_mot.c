/* ********************************************************** */
/*                                                            */
/* ✨  GRIMOIRE DES SORTS : dernier_mot.c             ✨      */
/*                                                            */
/* Créé pour : Le Scribe                                      */
/* Rédigé par : Le Mage ldauber                               */
/* Date de rédaction : 18/12/2025 11:16                       */
/*                                                            */
/* ********************************************************** */

#include <unistd.h>

int compte_lettre(char *s)
{
	int i = 0;
	while (s[++i]);
	return (i);
}

void dernier_mot(char *s)
{
	int i = compte_lettre(s);
	while (i >= 0)
	{
		while (s[i] == 9 || s[i] == 32)
			i--;
		while ((s[i] >= 65 && s[i] <= 90) || (s[i] >= 97 && s[i] <= 122))
			i--;
		if (s[i] == 9 || s[i] ==32)
		{
			while ((s[i] >= 22 && s[i] <= 125))
			{
				write(1, &s[i], 1);
				if (s[i + 1] == 0 || s[i + 1] == 9 || s[i + 1] == 32)
				{
					write(1, "\n", 1);
					return ;
				}
				i++;
			}
		}
		i--;
	}
}

#include <stdio.h>

int main(int ac, char **av)
{
	int i = 1;
	if (ac > 1)
	{
		while (i < ac)
		{
			dernier_mot(av[i]);
			i++;
		}
	}
	else
		printf("Scribe, il n'y a pas de phrase.\n");
	return (0);
}
