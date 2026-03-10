/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sort_in_tab.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ldauber <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/17 09:48:58 by ldauber           #+#    #+#             */
/*   Updated: 2025/12/17 10:05:37 by ldauber          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#define SIZE 10

void sort_int_tab(int *tab, unsigned int size)
{
	int tmp;
	unsigned int i = 0;
	unsigned int j;

	while (i < size - 1)
	{
		j = i;
		while (j < size)
		{
			if (tab[i] > tab[j])
			{
				tmp = tab[i];
				tab[i] = tab[j];
				tab[j] = tmp;
			}
			j++;
		}
		i++;
	}
}

int main()
{
	int tab[SIZE] = {1, 2, 3, 4, 6, 5, 42, -6, 12, 4};
	sort_int_tab(tab, SIZE);
	for (int i = 0; i < SIZE; i++)
		printf("%d, ", tab[i]);
	return (0);
}
