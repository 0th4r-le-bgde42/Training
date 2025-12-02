/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_iterative_factorial.c                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ldauber <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/16 09:07:05 by ldauber           #+#    #+#             */
/*   Updated: 2025/07/31 08:11:04 by ldauber          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_iterative_factorial(int nb)
{
	int	i;
	int	fact;

	i = 1;
	fact = 1;
	while (i <= nb)
	{
		fact = fact * i;
		i++;
	}
	if (nb < 0)
		return (0);
	return (fact);
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
	int fact = ft_iterative_factorial(nbr);
	int fact2 = ft_iterative_factorial(nbr2);
	int fact3 = ft_iterative_factorial(nbr3);
	int fact4 = ft_iterative_factorial(nbr4);
	int fact5 = ft_iterative_factorial(nbr5);

	printf("%d! = %d\n", nbr, fact);
	printf("%d! = %d\n", nbr2, fact2);
	printf("%d! = %d\n", nbr3, fact3);
	printf("%d! = %d\n", nbr4, fact4);
	printf("%d! = %d\n", nbr5, fact5);
	return 0;
}
*/
