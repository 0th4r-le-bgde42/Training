/* ********************************************************** */
/*                                                            */
/* ✨  GRIMOIRE DES SORTS : tabmult.c                 ✨      */
/*                                                            */
/* Créé pour : Le Professeur                                  */
/* Rédigé par : Le Mage ldauber                               */
/* Date de rédaction : 19/12/2025 10:50                       */
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

void ecritnombre(long n)
{
	if (n > 9)
		ecritnombre(n / 10);
	write(1, &"0123456789"[n % 10], 1);
}

void ecritmult()
{
	write(1, " x ", 3);
}

void ecritres()
{
	write(1, " = ", 3);
}
void tabmult(long n)
{
	int i = 0;
	while (++i <= 10)
	{
		if (i < 10)
			write(1, " ", 1);
		ecritnombre(i);
		ecritmult();
		ecritnombre(n);
		ecritres();
		ecritnombre(i * n);
		write(1, "\n", 1);
	}
}

int expeliatoi(char *s)
{
	int res = 0;
	int i = 0;
	while (s[i] >= 48 && s[i] <= 57)
	{
		res *= 10;
		res += s[i] - 48;
		i++;
	}
	return (res);
}

int main(int ac, char **av)
{
	if (ac == 2)
		tabmult(expeliatoi(av[1]));
	return (0);
}
