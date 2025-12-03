/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   do_op.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ldauber <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/03 10:39:48 by ldauber           #+#    #+#             */
/*   Updated: 2025/12/03 10:53:59 by ldauber          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

int main(int ac, char **av)
{
	if (ac == 4)
	{
		if (av[2][0] == '+')
			printf("%d\n", atoi(av[1]) + atoi(av[3]));
		if (av[2][0] == '-')
			printf("%d\n", atoi(av[1]) - atoi(av[3]));
		if (av[2][0] == '*')
			printf("%d\n", atoi(av[1]) * atoi(av[3]));
		if (av[2][0] == '/')
			printf("%d\n", atoi(av[1]) / atoi(av[3]));
		if (av[2][0] == '%')
			printf("%d\n", atoi(av[1]) % atoi(av[3]));
	}
	else
		write(1, "\n", 1);
	return (0);
}
