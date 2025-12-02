/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_recursive_factorial.c                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ldauber <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/16 09:21:53 by ldauber           #+#    #+#             */
/*   Updated: 2025/07/16 20:26:53 by ldauber          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_recursive_factorial(int nb)
{
	if (nb < 0)
		return (0);
	else if (nb == 0)
		return (1);
	else
		return (nb * ft_recursive_factorial(nb - 1));
}
/*
#include <stdio.h>

int main()
{
    int nbr = 3;
    int nbr2 = 6;
    int nbr3 = 10;
	int nbr4 = -16;
    int fact = ft_recursive_factorial(nbr);
    int fact2 = ft_recursive_factorial(nbr2);
    int fact3 = ft_recursive_factorial(nbr3);
	int fact4 = ft_recursive_factorial(nbr4);

    printf("%d! = %d\n", nbr, fact);
    printf("%d! = %d\n", nbr2, fact2);
    printf("%d! = %d\n", nbr3, fact3);
	printf("%d! = %d\n", nbr4, fact4);
    return 0;
}
*/
