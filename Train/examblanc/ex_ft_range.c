/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ex_ft_range.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ldauber <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/17 11:02:47 by ldauber           #+#    #+#             */
/*   Updated: 2025/12/17 12:35:31 by ldauber          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include <stdio.h>

int ft_intlen(int start, int end)
{
	int i = 0;
	if (start < end)
	{
		while (start <= end)
		{
			i++;
			start++;
		}
	}
	else
		while (start >= end)
		{
			i++;
			start--;
		}
	return (i);
}

int *ft_range(int start, int end)
{
	int i = 0;
	printf("len = %d\n", ft_intlen(start, end));
	int *tab = malloc(ft_intlen(start, end) * sizeof(int));
	if (!tab)
		return (0);
	if (start < end)
	{
		while (start <= end)
		{
			tab[i] = start;
			start++;
			i++;
		}
	}
	else
		while (start >= end)
		{
			tab[i] = start;
			start--;
			i++;
		}
	return (tab);
}


int main()
{
	int i = 0;
	int start = 40;
	int end = 42;
	int *res = ft_range(start, end);
	while (i < ft_intlen(start, end))
	{
		printf("%d", res[i]);
		if (i + 1 == ft_intlen(start, end))
			break;
		else
			printf(", ");
		i++;
	}
	return (0);
}
