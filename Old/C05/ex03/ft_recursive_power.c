/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_recursive_power.c                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ldauber <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/16 12:44:40 by ldauber           #+#    #+#             */
/*   Updated: 2025/07/16 20:28:46 by ldauber          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_recursive_power(int nb, int power)
{
	if (power > 0)
		return (nb * ft_recursive_power(nb, power -1));
	if (power < 0)
		return (0);
	else
		return (1);
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
	int result = ft_recursive_power(nbr, 2);
	int result2 = ft_recursive_power(nbr2, 3);
	int result3 = ft_recursive_power(nbr3, 8);
	int result4 = ft_recursive_power(nbr4, -12);
	int result5 = ft_recursive_power(nbr5, 0);

	printf("%d = %d\n", nbr, result);
	printf("%d = %d\n", nbr2, result2);
	printf("%d = %d\n", nbr3, result3);
	printf("%d = %d\n", nbr4, result4);
	printf("%d = %d\n", nbr5, result5);
	return 0;
}
*/
