/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ldauber <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/30 11:44:45 by ldauber           #+#    #+#             */
/*   Updated: 2025/12/30 15:23:48 by ldauber          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef PUSH_SWAP_H
# define PUSH_SWAP_H

#include "libftprintf.h"

#include <unistd.h>
#include <stdlib.h>

typedef struct s_stack
{
	int value;
	int index;
	struct s_stack *next;
	struct s_stack *prev;
} t_stack;

void swap(t_stack **stack);
void sa(t_stack **stack_a);
void sb(t_stack **stack_b);
void ss(t_stack **stack_a, t_stack **stack_b);
void push(t_stack **src, t_stack **dst);
void pa(t_stack **a, t_stack **b);
void pb(t_stack **b, t_stack **a);
void rotate(t_stack **stack);
void ra(t_stack **stack_a);
void rb(t_stack **stack_b);
void rr(t_stack **stack_a, t_stack **stack_b);

#endif
