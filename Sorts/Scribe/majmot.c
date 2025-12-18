/* ********************************************************** */
/*                                                            */
/* ✨  GRIMOIRE DES SORTS : majmot.c                  ✨      */
/*                                                            */
/* Créé pour : Le Scribe                                      */
/* Rédigé par : Le Mage ldauber                               */
/* Date de rédaction : 18/12/2025 15:08                       */
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

int une_lettre(char *s)
{
	int i = 0;
	if ((s[i] >= 65 && s[i] <= 90) || (s[i] >= 97 && s[i] <= 122))
		return (1);
	return (0);
}
void majmot(char *s)
{
	int i = 0;
	while (s[i])
	{
		if (une_lettre(&s[0]))
			s[0] -= 32;
		if ((s[i]) == 32 && une_lettre(&s[i + 1]))
			s[i + 1] -= 32;
		write(1, &s[i], 1);
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
			majmot(av[i]);
			i++;
		}
	}
	write(1, "\n", 1);
	return (0);
}
