/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_range.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ldauber <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/09 12:41:46 by ldauber           #+#    #+#             */
/*   Updated: 2025/12/09 12:56:36 by ldauber          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>

int	*ft_range(int start, int end)
/*{
	int i = 0;
	int len = (end - start) < 0 ? ((end - start) * -1) + 1 : (end - start) + 1;
	int *range = (int *)malloc(len * sizeof(int));
	while (i < len)
	{
		if (start < end)
			range[i] = start++;
		else
			range [i] = start --;
		i++;
	}
	return (range);
}*/
{
	int *tab = 0;
	int i = 0;
	if (start >= end)
		return (0);
	tab = malloc(sizeof(int) * (end - start + 1));
	if (!tab)
		return (0);
	while (i < (end - start + 1))
	{
		tab[i] = start + i;
		i++;
	}
	return (tab);
}

#include <stdio.h>

int main()
{
	int i = 0;
	int start = 0;
	int end = -3;
	int *tab = ft_range(start, end);
	
	while (i < (end - start + 1))
	{
		printf("%d\n", tab[i]);
		i++;
	}
	return (free(tab), tab = 0, 0);
}
