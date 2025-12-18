/* ********************************************************** */
/*                                                            */
/* ✨  GRIMOIRE DES SORTS : cherche_et_remplace.c     ✨      */
/*                                                            */
/* Créé pour : Le Scribe                                      */
/* Rédigé par : Le Mage ldauber                               */
/* Date de rédaction : 18/12/2025 14:00                       */
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
#include <stdio.h>

int compte_lettre(char *s)
{
	int i = 0;
	while (s[++i]);
	return (i);
}

void cherche_et_remplace(char *s, char c, char r)
{
	int i = 0;
	while (s[i])
	{
		if (s[i] == c)
			s[i] = r;
		write(1, &s[i], 1);
		i++;
	}
}

int main(int ac, char **av)
{
	if (ac == 4)
	{
		char *s = av[1];
		char c = *av[2];
		char r = *av[3];
		if (compte_lettre(av[2]) > 1 || compte_lettre(av[3]) > 1)
		{
			printf("Je ne peux remplacer plusieurs lettres, choisissez-en une et relancez le sorts");
			return (0);
		}
		cherche_et_remplace(s, c, r);
	}
	else
		printf("Je ne peux rien remplacer car je n'ai pas d'arguments, donnez m'en et relancez le sorts");
	return (0);
}
