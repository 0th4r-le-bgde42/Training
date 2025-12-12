/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_atoi.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ldauber <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/11 10:18:04 by ldauber           #+#    #+#             */
/*   Updated: 2025/12/11 10:36:14 by ldauber          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>

int ft_isspace(char c)
{
	if ((c >= 9 && c <= 13) || c == 32)
		return (1);
	return (0);
}

int ft_atoi(const char *str)
{
	int i = 0;
	int res = 0;
	int sign = 1;
	while (ft_isspace(str[i]))
		i++;
	if (str[i] == '-' || str[i] == '+')
	{
		if (str[i] == '-')
			sign = -1;
		i++;
	}
	while (str[i])
	{
		res *= 10;
		res += (str[i] - 48); 
		i++;
	}
	return (res * sign);
}

int main (int ac, char **av)
{
	int i = 0;
	if (ac > 1)
	{
		while (av[++i])
			printf("%d\n", ft_atoi(av[i]));
	}
	return (0);
}
