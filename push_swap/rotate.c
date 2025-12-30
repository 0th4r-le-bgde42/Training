/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   rotate.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ldauber <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/30 14:09:31 by ldauber           #+#    #+#             */
/*   Updated: 2025/12/30 15:19:33 by ldauber          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void rotate(t_stack **stack)
{
	t_stack *tmp;
	t_stack *first;

	if (!stack || !*stack || !(*stack)->next)
		return ;
	tmp = *stack;
	first = *stack;
	(*stack)->next->prev = NULL;
	*stack = (*stack)->next;
	while (tmp->next != NULL)
		tmp = tmp->next;
	tmp->next = first;
	first->prev = tmp;
	first->next = NULL;
}

void ra(t_stack **stack_a)
{
	rotate(stack_a);
	write(1, "ra\n", 3);
}

void rb(t_stack **stack_b)
{
	rotate(stack_b);
	write(1, "rb\n", 3);
}

void rr(t_stack **stack_a, t_stack **stack_b)
{
	rotate(stack_a);
	rotate(stack_b);
	write(1, "rr\n", 3);
}

/*#include <stdio.h>

t_stack *new_node(int val)
{
	t_stack *node = malloc(sizeof(t_stack));
	node->value = val;
	node->next = NULL;
	node->prev = NULL;
	return (node);
}

void printf_stack(t_stack *a)
{
	printf("Etat de la pile\n");
	printf("A: ");
	while(a) {printf("%d ", a->value); a = a->next;}
}

int main()
{
	t_stack *stack_a = NULL;

	stack_a = new_node(15);
	stack_a->next = new_node(2);
    stack_a->next->prev = stack_a;
    stack_a->next->next = new_node(6);
    stack_a->next->next->prev = stack_a->next;

	printf_stack(stack_a);

	ra(&stack_a);
	printf("\nNouvel ");
	printf_stack(stack_a);
	return (0);
}*/
