/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_itoa.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ldauber <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/15 09:53:44 by ldauber           #+#    #+#             */
/*   Updated: 2025/12/15 11:20:32 by ldauber          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include <stdio.h>

int get_len(long nb)
{
	int len = 0;
	if (nb <= 0)
		len++;
	while (nb > 0)
	{
		len++;
		nb = nb / 10;
	}
	return (len);
}

char *ft_itoa(int nb)
{
	char *result;
	int sign;
	int len;
	long n = nb;
	
	sign = (n < 0);
	if (sign)
		n = -n;
	len = get_len(n);
	result = malloc((len + sign + 1) * sizeof(char));
	if (!result)
		return (0);
	result[len + sign] = '\0';
	while (len > 0)
	{
		result[len + sign - 1] = (n % 10) + 48;
		n /= 10;
		len--;
	}
	if (sign)
		result[0] = '-';
	return (result);
}

int ft_atoi(char *str)
{
	int res = 0;
	int sign = 1;
	int i = 0;

	while (str[i] >= 9 && str[i] <= 12 && str[i] == 32)
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
		res += str[i] - 48;
		i++;
	}
	return (res * sign);
}

int main(int ac, char **av)
{
	if (ac == 2)
	{
		int tres = ft_atoi(av[1]);
		char *res = ft_itoa(tres);
		printf("%s", res);
		free(res);
	}
	return (0);
}
