/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_atoi.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ldauber <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/15 16:07:27 by ldauber           #+#    #+#             */
/*   Updated: 2025/07/31 14:56:42 by ldauber          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_atoi(char *str)
{
	int	result;
	int	sign;

	result = 0;
	sign = 1;
	while (*str == ' ' || *str == '\t' || *str == '\n' || *str == '\v'
		|| *str == '\f' || *str == '\r')
		str++;
	while (*str == '-' || *str == '+')
	{
		if (*str == '-')
			sign++;
		str++;
	}
	while (*str >= '0' && *str <= '9')
	{
		result = result * 10 + (*str - '0');
		str++;
	}
	if (sign % 2 == 0)
		return (result * -1);
	else
		return (result);
}

#include <stdio.h>
#include <stdlib.h> 

int main()
{
	char test1[] = "234";
	char test2[] = "  +6543";
	char test3[] = "-1234";
	char test4[] = "   9B123";
	char test5[] = "   ---+--+4321ab567";

	int a = ft_atoi(test1);
	int b = ft_atoi(test2);
	int c = ft_atoi(test3);
	int d = ft_atoi(test4);
	int e = ft_atoi(test5);
	int f = atoi(test1);
	int g = atoi(test2);
	int h = atoi(test3);
	int i = atoi(test4);
	int j = atoi(test5);
	printf("%d\n %d\n %d\n %d\n %d\n", a, b, c, d, e);
	printf("%d\n %d\n %d\n %d\n %d\n", f, g, h, i ,j);
	return 0;
}

