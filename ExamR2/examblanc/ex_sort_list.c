/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ex_sort_list.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ldauber <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/17 12:39:15 by ldauber           #+#    #+#             */
/*   Updated: 2025/12/17 13:26:42 by ldauber          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>

typedef struct    s_list
{
    struct s_list *next;
    int	data;
}                 t_list;

int ascending(int a, int b)
{
	return (a <= b);
}

t_list *sort_list(t_list* lst, int (*cmp)(int, int))
{
	int tmp;
	t_list *head;

	head = lst;
	while(lst != 0 && lst->next != 0)
	{
		if ((*cmp)(lst->data, lst->next->data) == 0)
		{
			tmp = lst->data;
			lst->data = lst->next->data;
			lst->next->data = tmp;
			lst = head;
		}
		else
			lst = lst->next;
	}
	return (head);
}

int main()
{
	t_list a;
	int var_a = 42;
	a.data = var_a;
	a.next = 0;

	t_list b;
	int var_b = 0;
	b.data = var_b;
	b.next = 0;

	t_list c;
	int var_c = -42;
	c.data = var_c;
	c.next = 0;

	a.next = &b;
	b.next = &c;

	sort_list(&a, ascending);
	
	for (t_list *tmp = &a; tmp > 0; tmp = tmp->next)
		printf("%d\n", tmp->data);
	return (0);
}
