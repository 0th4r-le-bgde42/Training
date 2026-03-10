/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   pgcd.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ldauber <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/10 11:12:20 by ldauber           #+#    #+#             */
/*   Updated: 2025/12/10 11:23:46 by ldauber          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <stdlib.h>

int pgcd(unsigned int a, unsigned int b)
{
	if (b == 0)
		return (a);
	return (pgcd(b, a % b));
}

int main(int ac, char **av)
{
	if (ac == 3)
		printf("%d\n", pgcd(atoi(av[1]), atoi(av[2])));
	else
		printf("\n");
	return (0);
}
