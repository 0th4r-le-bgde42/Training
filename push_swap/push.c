/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ldauber <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/30 13:07:58 by ldauber           #+#    #+#             */
/*   Updated: 2025/12/30 15:28:03 by ldauber          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void push(t_stack **src, t_stack **dst)
{
	t_stack *tmp;

	if (!src || !*src)
		return ;
	if (!dst || !*dst)
	{
		*dst = *src;
		(*src)->next->prev = NULL;
		*src = (*src)->next;
		(*dst)->next = NULL;
	}
	else
	{
		tmp = *src;
		if ((*src)->next)
			(*src)->next->prev = NULL;
		*src = (*src)->next;
		(*dst)->prev = tmp;
		tmp->next = *dst;
		*dst = tmp;
	}
}

void pb(t_stack **a, t_stack **b)
{
	push(a, b);
	write(1, "pb\n", 3);
}

void pa(t_stack **b, t_stack **a)
{
	push(b, a);
	write(1, "pa\n", 3);
}

/*#include <stdio.h>

// Utilitaire de création
t_stack *new_node(int val)
{
    t_stack *node = malloc(sizeof(t_stack));
    node->value = val;
    node->next = NULL;
    node->prev = NULL;
    return node;
}

void print_stacks(t_stack *a, t_stack *b)
{
    printf("\n--- État des Piles ---\n");
    printf("A: ");
    while(a) { printf("%d ", a->value); a = a->next; }
    printf("\nB: ");
    while(b) { printf("%d ", b->value); b = b->next; }
    printf("\n----------------------\n");
}

int main(void)
{
    t_stack *stack_a = NULL;
    t_stack *stack_b = NULL;

    // Création A: 15 -> 2 -> 6
    stack_a = new_node(15);
    stack_a->next = new_node(2);
    stack_a->next->prev = stack_a;
    stack_a->next->next = new_node(6);
    stack_a->next->next->prev = stack_a->next;
	stack_b = new_node(42);

    print_stacks(stack_a, stack_b);

    printf("\nAction: pb (A vers B)\n");
    pb(&stack_a, &stack_b);
    print_stacks(stack_a, stack_b);

    printf("\nAction: pb (A vers B)\n");
    pb(&stack_a, &stack_b);
    print_stacks(stack_a, stack_b);

    printf("\nAction: pa (B vers A)\n");
    pa(&stack_b, &stack_a);
    print_stacks(stack_a, stack_b);

    // Nettoyage (optionnel pour un test rapide)
    return 0;
}*/
