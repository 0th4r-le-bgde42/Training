/* ********************************************************** */
/*                                                            */
/* ✨  GRIMOIRE DES SORTS : comparemots.c             ✨      */
/*                                                            */
/* Créé pour : Le Professeur                                  */
/* Rédigé par : Le Mage ldauber                               */
/* Date de rédaction : 19/12/2025 10:35                       */
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

void comparemot(char *s1, char *s2)
{
	int i = 0;
	int j = 0;
	while (s1[i])
	{
		while (s2[i])
		{
			if (s1[i] != s2[j])
			{
				write(1, "different\n", 10);
				return ;
			}
			else
			{
				write(1, "juste", 5);
				return ;
			}
			j++;
		}
		i++;
	}
}

int main(int ac, char **av)
{
	if (ac == 3)
	{
		char *s1 = av[1];
		char *s2 = av[2];
		comparemot(s1, s2);
	}
	else
		write(1, "\n", 1);
	return (0);
}
