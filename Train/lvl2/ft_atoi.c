/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_atoi.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ldauber <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/03 10:55:18 by ldauber           #+#    #+#             */
/*   Updated: 2025/12/09 11:06:51 by ldauber          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>

int ft_atoi(const char *str)
{
	int result = 0;
	int sign = 1;
	int i = -1;
	while((str[++i] >= 9 && str[i] <= 13) || str[i] == 32);
	if (str[++i] == '-' || str[i] == '+')
		if(str[i] == '-')
			sign *= -1;
	while (str[++i])
	{
		result *= 10;
		result += str[i] - '0';
	}
	return (result * sign);
}

int main(int ac, char **av)
{
	if (ac == 2)
	{
		printf("%d", ft_atoi(av[1]));
	}
	printf("\n");
	return (0);
}
