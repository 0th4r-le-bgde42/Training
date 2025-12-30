/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   swap.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ldauber <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/30 10:01:42 by ldauber           #+#    #+#             */
/*   Updated: 2025/12/30 14:16:00 by ldauber          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void swap(t_stack **stack)
{
	t_stack *first;
	t_stack *second;

	if (!*stack || !(*stack)->next || !stack)
		return;
	first = *stack;
	second = first->next;
	first->next = second->next;
	if (second->next)
		second->next->prev = first;
	second->next = first;
	second->prev = NULL;
	first->prev = second;
	*stack = second;
}

void sa(t_stack **stack_a)
{
	swap(stack_a);
	write(1, "sa\n", 3);
}

void sb(t_stack **stack_b)
{
	swap(stack_b);
	write(1, "sb\n", 3);
}

void ss(t_stack **stack_a, t_stack **stack_b)
{
	swap(stack_a);
	swap(stack_b);
	write(1, "ss\n", 3);
}

/*#include <stdio.h>

// Fonction utilitaire pour créer un nouveau noeud proprement
t_stack	*stack_new(int val)
{
	t_stack	*new;

	new = malloc(sizeof(t_stack));
	if (!new)
		return (NULL);
	new->value = val;
	new->index = 0;
	new->next = NULL;
	new->prev = NULL;
	return (new);
}

// Fonction pour afficher une pile et vérifier l'intégrité des pointeurs
void	display_stack(char *name, t_stack *stack)
{
	t_stack	*tmp;

	printf("--- Pile %s ---\n", name);
	if (!stack)
	{
		printf("(vide)\n");
		return ;
	}
	tmp = stack;
	while (tmp)
	{
		printf("Val: %d", tmp->value);
		// Vérification du lien précédent
		if (tmp->prev)
			printf(" | Prev: %d", tmp->prev->value);
		else
			printf(" | Prev: NULL");
		// Vérification du lien suivant
		if (tmp->next)
			printf(" | Next: %d\n", tmp->next->value);
		else
			printf(" | Next: NULL\n");
		tmp = tmp->next;
	}
}

int	main(void)
{
	t_stack	*a;
	t_stack	*b;
	t_stack	*tmp;

	// 1. Initialisation de la pile A : 15 -> 2 -> 6
	a = stack_new(15);
	a->next = stack_new(2);
	a->next->prev = a;
	a->next->next = stack_new(6);
	a->next->next->prev = a->next;

	// 2. Initialisation de la pile B : 100 -> 50
	b = stack_new(100);
	b->next = stack_new(50);
	b->next->prev = b;

	printf("### ÉTAT INITIAL ###\n");
	display_stack("A", a);
	display_stack("B", b);

	// 3. Test de sa
	printf("\nExécution de sa...\n");
	sa(&a);
	display_stack("A", a);

	// 4. Test de ss
	printf("\nExécution de ss...\n");
	ss(&a, &b);
	display_stack("A", a);
	display_stack("B", b);

	// Nettoyage de la mémoire (simple pour le test)
	while (a)
	{
		tmp = a->next;
		free(a);
		a = tmp;
	}
	while (b)
	{
		tmp = b->next;
		free(b);
		b = tmp;
	}

	return (0);
}*/
