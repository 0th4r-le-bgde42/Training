/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_iterative_power.c                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ldauber <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/16 10:51:00 by ldauber           #+#    #+#             */
/*   Updated: 2025/07/16 20:28:13 by ldauber          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_iterative_power(int nb, int power)
{
	int	i;
	int	result;

	i = 0;
	result = 1;
	if (power < 0)
		return (0);
	if (power == 0)
		return (1);
	while (i < power)
	{
		result = result * nb;
		i++;
	}
	return (result);
}
/*
#include <stdio.h>

int main()
{
	int	nbr = 3;
	int nbr2 = 6;
	int nbr3 = 10;
	int nbr4 = -6;
	int nbr5 = 0;
	int result = ft_iterative_power(nbr, 2);
	int result2 = ft_iterative_power(nbr2, 3);
	int result3 = ft_iterative_power(nbr3, 8);
	int result4 = ft_iterative_power(nbr4, -12);
	int result5 = ft_iterative_power(nbr5, 0);

	printf("%d = %d\n", nbr, result);
	printf("%d = %d\n", nbr2, result2);
	printf("%d = %d\n", nbr3, result3);
	printf("%d = %d\n", nbr4, result4);
	printf("%d = %d\n", nbr5, result5);
	return 0;
}
*/
