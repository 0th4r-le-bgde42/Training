/* ********************************************************** */
/*                                                            */
/* ✨  GRIMOIRE DES SORTS : decoupage.c               ✨      */
/*                                                            */
/* Créé pour : Le Marchand                                    */
/* Rédigé par : Le Mage ldauber                               */
/* Date de rédaction : 29/12/2025 13:46                       */
/*                                                            */
/*                ||/                         /{\             */
/*                |  @___oo                   \}/             */
/*       /\  /\   / (__,,,,|                   |     ___      */
/*      ) /^\) ^/ _)                          (=\.  /-. \     */
/*      )   /^\/   _)                          |\/\_|"| |     */
/*      )   _ /  / _)                          |_\ |;-|  ;    */
/*  /\  )/\/ ||  | )_)                         | / \| |_/ \   */
/* <  >      |(,,) )__)                        | )/\/      \  */
/*  ||      /    \)___)\                       | ( '|  \   |  */
/*  | ____(      )___) )___                    |    \_ /   \  */
/*  \______(_______;;; __;;;                   |    /  \_.--\ */
/* ********************************************************** */

#include <stdio.h>
#include <stdlib.h>

int comptemot(char const *s)
{
	int i = 0;
	int compte = 0;
	int danslemot = 0;
	while (s[i])
	{
		if (s[i] != 32 && danslemot == 0)
		{
			danslemot = 1;
			compte++;
		}
		else if (s[i] == 32)
			danslemot = 0;
		i++;
	}
	return (compte);
}

char *dupstr(char const *s, int start, int end)
{
	char *dup;
	int i;
	dup = malloc(sizeof(char) * (end - start + 1));
	if (!dup)
		return (0);
	i = 0;
	while (start < end)
	{
		dup[i] = s[start];
		i++;
		start++;
	}
	dup[i] = '\0';
	return (dup);
}

char **remplissage(char const *s, char c, char **tab, int compte)
{
	int i = 0;
	int j = 0;
	int start;

	while (s[i] && j < compte)
	{
		while (s[i] == c)
			i++;
		start = i;
		while (s[i] && s[i] != c)
			i++;
		if (i >= start)
		{
			tab[j] = dupstr(s, start, i);
			if (!tab[j])
				return (NULL);
			j++;
		}
		tab[j] = "~~Fin de la liste de course~~";
		i++;
	}
	return (tab);
}

char **decoupage(char const *s, char c)
{
	char **tab;
	int compte;
	compte = comptemot(s);
	tab = malloc((compte + 1) * (sizeof(char *)));
	if (!tab)
		return (0);
	return (remplissage(s, c, tab, compte));
}

int main(int ac, char **av)
{
	if (ac == 3)
	{
		char *s = av[1];
		char c = av[2][0];
		char **res = decoupage(s, c);
		int i = 0;
		while (i <= comptemot(s))
		{
			printf("%s\n", res[i]);
			i++;
		}
	}
	return (0);
}
