/* ********************************************************** */
/*                                                            */
/* ✨  GRIMOIRE DES SORTS : calcul.c                  ✨      */
/*                                                            */
/* Créé pour : Le Marchand                                    */
/* Rédigé par : Le Mage ldauber                               */
/* Date de rédaction : 19/12/2025 11:57                       */
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

int add(int i, int j)
{
	int res = i + j;
	return (res);
}

int sous(int i, int j)
{
	int res = i - j;
	return (res);
}

int mult(int i, int j)
{
	int res = i * j;
	return (res);
}

int div(int i, int j)
{
	int res = i / j;
	return (res);
}

int mod(int i, int j)
{
	int res = i % j;
	return (res);
}

int expeliatoi(char *s)
{
	int res = 0;
	int sign = 1;
	int i = 0;
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
	if ( n > 9)
		ecritnombre(n / 10);
	write(1, &"0123456789"[n % 10], 1);
}
int main(int ac, char **av)
{
	if (ac == 4)
	{
		int i = expeliatoi(av[1]);
		int j = expeliatoi(av[3]);
		char c = av[2][0];
		if (c == '+')
			ecritnombre(add(i, j));
		if (c == '-')
			ecritnombre(sous(i, j));
		if (c == '*')
			ecritnombre(mult(i, j));
		if (c == '/')
			ecritnombre(div(i, j));
		if (c == '%')
			ecritnombre(mod(i, j));
	}
	write(1, "\n", 1);
	return (0);
}
