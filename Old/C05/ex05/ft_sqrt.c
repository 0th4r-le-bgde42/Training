/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_sqrt.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ldauber <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/17 09:52:11 by ldauber           #+#    #+#             */
/*   Updated: 2025/07/31 08:12:15 by ldauber          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_sqrt(int nb)
{
	int	i;
	int	result;

	i = 0;
	result = 0;
	if (nb < 0)
		return (0);
	while (result < nb && i <= 46340)
	{
		result = i * i;
		if (result == nb)
			return (i);
		i++;
	}
	return (0);
}
/*
#include <stdio.h>

int main()
{
	int nb;

	nb = 49;
	printf("racine carre de %d = %d", nb, ft_sqrt(nb));
	return (0);
}
*/
