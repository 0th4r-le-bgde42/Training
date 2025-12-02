/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_range.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ldauber <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/21 08:18:53 by ldauber           #+#    #+#             */
/*   Updated: 2025/07/22 15:31:39 by ldauber          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>

int	*ft_range(int min, int max)
{
	int	*tab;
	int	i;

	tab = 0;
	i = 0;
	if (min >= max)
		return (0);
	tab = malloc(sizeof(int) * (max - min));
	if (tab == 0)
		return (0);
	while (i < (max - min))
	{
		tab[i] = min + i;
		i++;
	}
	return (tab);
}
/*
#include <stdio.h>

int	main(void)
{
	int	i;
	int	min;
	int	max;
	int	*tab;

	tab = 0;
	min = 6;
	max = 14;
	tab = ft_range(min, max);
	i = 0;
	while (i < (max - min))
	{
		printf("%d\n", tab[i]);
		i++;
	}
	free(tab);
	tab = 0;
	return (0);
}
*/
