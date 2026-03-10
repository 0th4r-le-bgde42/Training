/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   fprime.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ldauber <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/12 13:06:21 by ldauber           #+#    #+#             */
/*   Updated: 2025/12/12 13:24:47 by ldauber          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <stdlib.h>

int main(int ac, char **av)
{
	int i = 2;
	int num = atoi(av[1]);
	if (ac == 2)
	{
		if (num == 1)
			printf("1");
		while (i <= num)
		{
			if (num % i == 0)
			{
				printf("%d", i);
				if (num != i)
					printf("*");
				num = num / i;
			}
			else
				i++;
		}
	}
	printf("\n");
	return (0);
}
