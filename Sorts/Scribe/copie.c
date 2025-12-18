/* ********************************************************** */
/*                                                            */
/* ✨  GRIMOIRE DES SORTS : copie.c                   ✨      */
/*                                                            */
/* Créé pour : Le Scribe                                      */
/* Rédigé par : Le Mage ldauber                               */
/* Date de rédaction : 18/12/2025 12:31                       */
/*                                                            */
/* ********************************************************** */

#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>

int compte_lettre(char *s)
{
	int i = 0;
	while (s[++i]);
	return (i);
}

char *copie1(char *s1, char *s2)
{
	int i = 0;
	while (s2[i] && compte_lettre(s1) != compte_lettre(s2))
	{
		s1[i] = s2[i];
		write(1, &s1[i], 1);
		i++;
	}
	return (s1);
}

char *copie2(char *s1, char *s2)
{
	int i = 0;
	s1 =  malloc(compte_lettre(s2 + 1) * sizeof(char));
	if (!s1)
		return (NULL);
	while (s2[i] && i < len)
	{
		s1[i] = s2[i];
		i++;
	}
	s1[i] = '\0';
	return (s1);
}

int main(int ac, char **av)
{
	if (ac == 3)
	{
		char *s1 = av[1];
		char *s2 = av[2];
		char *copie = copie2(s1, s2);
		int i = 0;
		while (copie[i])
		{
			write(1, &copie[i], 1);
			i++;
		}
	}
	else
	{
		char phrase1[39] = "";
		char phrase2[39] = "Meme plus besoin de toucher a ma plume";
		copie1(phrase1, phrase2);
	}
	return (0);
}
