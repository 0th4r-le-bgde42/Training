/* ********************************************************** */
/*                                                            */
/* ✨  GRIMOIRE DES SORTS : compte_lettre.c           ✨      */
/*                                                            */
/* Créé pour : Le Scribe                                      */
/* Rédigé par : Le Mage ldauber                               */
/* Date de rédaction : 18/12/2025 10:36                       */
/*                                                            */
/* ********************************************************** */

#include <stdio.h>

int compte_lettre(char *s)
{
	int i = 0;
	while (s[++i]);
	return (i);
}

#include <stdio.h>

int main(int ac, char **av)
{
	int i = 1;
	if (ac >= 2)
	{
		while (i < ac)
		{
			printf("%d\n", compte_lettre(av[i]));
			i++;
		}
	}
	else
		printf("Scribe, il n'y a pas de mots\n");
	return (0);
}
