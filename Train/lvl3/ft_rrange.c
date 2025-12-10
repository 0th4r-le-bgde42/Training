/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_rrange.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ldauber <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/10 10:33:10 by ldauber           #+#    #+#             */
/*   Updated: 2025/12/10 10:39:51 by ldauber          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>

int	*ft_range(int start, int end)
{
	int i = 0;
	int len = 0;
	if ((end - start) < 0) 
		len = ((end - start) * -1) + 1;
	else
		len = (end - start) + 1;

	int *range = malloc(len * sizeof(int));
	while (i < len)
	{
		if (end < start)
			range[i] = end++;
		else
			range [i] = end--;
		i++;
	}
	return (range);
}

#include <stdio.h>

int main()
{
	int i = 0;
	int start = 0;
	int end = -3;
	int *tab = ft_range(start, end);

	while (i < 4)
	{
		printf("%d\n", tab[i]);
		i++;
	}
	free(tab);
	tab = 0;
	return (0);
}
