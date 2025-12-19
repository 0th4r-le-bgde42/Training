/* ********************************************************** */
/*                                                            */
/* ✨  GRIMOIRE DES SORTS : intermonnaie.c            ✨      */
/*                                                            */
/* Créé pour : Le Marchand                                    */
/* Rédigé par : Le Mage ldauber                               */
/* Date de rédaction : 19/12/2025 11:19                       */
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

void intermonnaie(int *i, int *j)
{
	int tmp = 0;
	tmp = *i;
	*i = *j;
	*j = tmp;
}

int expeliatoi(char *s)
{
	int res = 0;
	int i = 0;
	int sign = 1;
	if (s[i] == '-' && s[i] == '+')
	{
		if (s[i] == '-')
		{
			sign = -1;
			i++;
		}
	}
	while (s[i] >= 48 && s[i] <= 57)
	{
		res *= 10;
		res += s[i] - 48;
		i++;
	}
	return (res * sign);
}

int main(int ac, char **av)
{
	if (ac == 3)
	{
		int a = expeliatoi(av[1]);
		int b = expeliatoi(av[2]);
		printf("personne_a = %d\npersonne_b = %d\n", a, b);
		printf("~~intervertion~~\n");
		intermonnaie(&a, &b);
		printf("personne_a = %d\npersonne_b = %d\n", a, b);
	}
	else
		printf("\n");
	return (0);
}
