/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_all.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ldauber <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/12 13:47:00 by ldauber           #+#    #+#             */
/*   Updated: 2025/12/12 14:13:04 by ldauber          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void ft_putnbr(long n)
{
	if (n < 0)
	{
		write(1, "-", 1);
		n = -n;
	}
	if (n > 9)
		ft_putnbr(n / 10);
	write(1, &"0123456789"[n % 10], 1);
}

void ft_putstr(char *str)
{
	int i = -1;
	while (str[++i])
		write(1, &str[i], 1);
}
int ft_atoi(char *s)
{
	int i = 0;
	int res = 0;
	int sign = 1;
	while (s[i] >= 9 && s[i] <= 13 && s[i] == 32)
		i++;
	if (s[i] == 43 || s[i] == 45)
	{
		if (s[i] == 45)
			sign = -1;
		i++;
	}
	while (s[i])
	{
		res *= 10;
		res += s[i] - 48;
		i++;
	}
	return (res * sign);
}

int main(int ac, char **av)
{
	int i = 1;
	int j = 0;
	if (ac > 1)
	{
		while (i < ac)
		{
			if (av[i][j] >= 48 && av[i][j] <= 57)
			{
				ft_putnbr(ft_atoi(av[i]));
				write(1, "\n", 1);
			}
			else
			{
				ft_putstr(av[i]);
				write(1, "\n", 1);
			}
			i++;
		}
	}
	else
		write(1, "\n", 1);
	return (0);
}
