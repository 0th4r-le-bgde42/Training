/* ********************************************************** */
/*                                                            */
/* ✨  GRIMOIRE DES SORTS : supprespace.c             ✨      */
/*                                                            */
/* Créé pour : Le Scribe                                      */
/* Rédigé par : Le Mage ldauber                               */
/* Date de rédaction : 18/12/2025 14:29                       */
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
	if ((c >= 65 && c <= 90) || (c >= 97 && c <= 122))
		return (1);
	return(0);
}

void supprespace(char *s)
{
	int i = 0;
	while (s[i])
	{
		write(1, &s[i], 1);
		while (s[i] == 32 && s[i + 1] == 32)
		{
			if (s[i] == 32 && une_lettre(s[i + 1]))
				break ;
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
			supprespace(av[i]);
			i++;
		}
	}
	write(1, "\n", 1);
	return (0);
}
