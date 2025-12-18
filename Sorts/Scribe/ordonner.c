/* ********************************************************** */
/*                                                            */
/* ✨  GRIMOIRE DES SORTS : ordonner.c                ✨      */
/*                                                            */
/* Créé pour : Le Scribe                                      */
/* Rédigé par : Le Mage ldauber                               */
/* Date de rédaction : 18/12/2025 15:23                       */
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

#include <unistd.h>

int une_lettre(char c)
{
	if ((c >= 65 && c<= 90) || (c >= 97 && c <= 122))
		return (1);
	return (0);
}

void ordonner(char *s)
{
	int i = 0;
	int f = 0;
	int d = 0;
	while (s[i] == 32)
		i++;
	d = i;
	while ((s[i] >= 65 && s[i] <= 90) || (s[i] >= 97 && s[i] <= 122))
		i++;
	f = i;
	while (s[++i])
	{
		write(1, &s[i], 1);
		while (s[i] == 32 && s[i + 1] == 32)
		{
			if (s[i] == 32 && une_lettre(s[i + 1]))
				break;
			i++;
		}
	}
	if (s[i] == '\0')
	{
		i--;
		write(1, " ", 1);
		while (d < f)
		{
			write(1, &s[d], 1);
			d++;
		}
	}
}

int main(int ac, char **av)
{
	int i = 1;
	if (ac > 1)
	{
		while (i < ac)
		{
			ordonner(av[i]);
			i++;
		}
	}
	return (0);
}
