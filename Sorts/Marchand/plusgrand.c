/* ********************************************************** */
/*                                                            */
/* ✨  GRIMOIRE DES SORTS : plusgrand.c               ✨      */
/*                                                            */
/* Créé pour : Le Marchand                                    */
/* Rédigé par : Le Mage ldauber                               */
/* Date de rédaction : 19/12/2025 13:58                       */
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

void ecritnombre(long n)
{
	if (n < 0)
	{
		write(1, "-", 1);
		n = -n;
	}
	if (n > 9)
		ecritnombre(n / 10);
	write(1, &"0123456789"[n % 10], 1);
}

int main(int ac, char **av)
{
	if (ac > 1)
	{
		int i = 0;
		int g = 0;
		while (i < ac)
		{
			if (expeliatoi(av[i]) > g)
				g = expeliatoi(av[i]);
			i++;
		}
		ecritnombre(g);
	}
	return (0);
}
