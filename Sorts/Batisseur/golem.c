/* ********************************************************** */
/*                                                            */
/* ✨  GRIMOIRE DES SORTS : golem.c                   ✨      */
/*                                                            */
/* Créé pour : Le Batisseur                                   */
/* Rédigé par : Le Mage ldauber                               */
/* Date de rédaction : 29/12/2025 11:24                       */
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
#include <stdlib.h>

typedef struct s_golem
{
	char *nom;
	int force;
	int etat;
} t_golem;

typedef struct s_equipe
{   
    t_golem *golem;
    struct s_equipe *next;
} t_equipe;


void caragolem(t_golem golem)
{
	printf("Nom du golem = %s\nForce du golem = %d\nEtat du golem = %d\n\n", golem.nom, golem.force, golem.etat);
}

void carateam(t_equipe *nod)
{
	int i = 1;
	while (nod != NULL)
	{
		printf("Golem_%d\n", i);
		caragolem(*nod->golem);
		nod = nod->next;
		i++;
	}
}

void nomgolem(t_equipe *nod)
{
	printf("Dreamteam = ");
	while (nod != NULL)
	{
		if (nod->next == NULL)
		{
			printf("%s", nod->golem->nom);
			break;
		}
		printf("%s, ", nod->golem->nom);
		nod = nod->next;
	}
}

t_golem *creergolem(char *nom, int force, int etat)
{
	t_golem *golem = malloc(sizeof(t_golem));
	golem->nom = nom;
    golem->force = force;
    golem->etat = etat;
	return (golem);
}

void autoteam(t_equipe *nod, t_golem *golem)
{
	t_equipe *nod2 = malloc(sizeof(t_equipe));
	nod2->golem = golem;
	nod2->next = NULL;
	while (nod->next != NULL)
	{
		nod = nod->next;
	}
		nod->next = nod2;
}

int main()
{
	/*t_golem Golem_1;
	inigolem(&Golem_1, "Pedro", 100000, 1);
	caragolem(Golem_1);

	t_golem Golem_2;
	inigolem(&Golem_2, "Jacques", 1, 5);
	caragolem(Golem_2);

	t_golem Golem_3;
	inigolem(&Golem_3, "Ben", 42, 0);
	caragolem(Golem_3);*/

	t_equipe nod1;
	nod1.golem = creergolem("Pedro", 1000000, 1);
	nod1.next = NULL;

	autoteam(&nod1, creergolem("Jacques", 1, 5));
	autoteam(&nod1, creergolem("Ben", 42, 0));
	autoteam(&nod1, creergolem("Barbara", 99999999, 5));

	carateam(&nod1);
	nomgolem(&nod1);
	return (0);
}
