/* ********************************************************** */
/*                                                            */
/* ✨  GRIMOIRE DES SORTS : trielist.c                ✨      */
/*                                                            */
/* Créé pour : Le Marchand                                    */
/* Rédigé par : Le Mage ldauber                               */
/* Date de rédaction : 29/12/2025 09:56                       */
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

void trie(int *liste, unsigned int taille)
{
	unsigned int i = 0;
	unsigned int j = 0;
	int tmp = 0;
	while (i < taille - 1)
	{
		j = i;
		while (j < taille)
		{
			if (liste[i] > liste[j])
			{
				tmp = liste[i];
				liste[i] = liste[j];
				liste[j] = tmp;
			}
			j++;
		}
		i++;
	}
}

int main()
{
	int liste[] = {5, 8, 1, 7, 3, 124, -6, 0, 5, 42};
	unsigned int taille = 10;
	unsigned i = 0;

	printf("liste[%d] = {", taille);
	while(i < taille)
	{
		if (i == taille - 1)
		{
			printf("%d", liste[i]);
			break;
		}
		printf("%d, ", liste[i]);
		i++;
	}
	printf("}\n");

	trie(liste, taille);

	printf("nouvelle liste[%d] = {", taille);
	i = 0;
	while (i < taille)
	{
		if (i == taille - 1)
        {
            printf("%d", liste[i]);
            break;
        }
		printf("%d, ", liste[i]);
		i++;
	}
	printf("}\n");

	return (0);
}
