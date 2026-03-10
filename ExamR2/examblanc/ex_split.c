/* ********************************************************** */
/*                                                            */
/* ✨  GRIMOIRE DES SORTS : ex_split.c                ✨      */
/*                                                            */
/* Créé pour : Le examblanc                                   */
/* Rédigé par : Le Mage ldauber                               */
/* Date de rédaction : 30/12/2025 09:34                       */
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

#include <stdlib.h>
#include <stdio.h>


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
	int i = 0;
	dup = malloc(sizeof(char) * (end - start + 1));
	if (!dup)
		return (0);
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
	int j = 0;
	int end = 0;
	int start;

	while (s[end] && j < compte)
	{
		while (s[end] == c)
			end++;
		start = end;
		while (s[end] && s[end] != c)
			end++;
		if (end >= start)
		{
			tab[j] = dupstr(s, start, end);
			if (!tab[j])
				return (NULL);
			j++;
		}
		tab[j] = NULL;
		end++;
	}
	return (tab);
}

char **decoupage(char const *s, char c)
{
	int compte = comptemot(s);
	char **tab = malloc((compte +1) * sizeof(char *));
	if (!tab)
		return (NULL);
	return (remplissage(s, c , tab, compte));
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
