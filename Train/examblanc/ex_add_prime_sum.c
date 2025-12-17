/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ex_add_prime_sum.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ldauber <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/17 14:07:44 by ldauber           #+#    #+#             */
/*   Updated: 2025/12/17 14:41:32 by ldauber          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */


#include <unistd.h>

int is_prime(int n)
{
	int i = 2;
	if (n < i)
		return (0);
	while (i <= n / 2)
	{
		if (n % i == 0)
			return (0);
		i++;
	}
	return (1);
}

void ft_putnbr(long n)
{
	if (n > 9)
		ft_putnbr(n / 10);
	write(1, &"0123456789"[n % 10], 1);
}

int ft_atoi(char *s)
{
	int i = 0;
	int res = 0;
	while (s[i])
	{
		res *= 10;
		res += s[i] - 48;
		i++;
	}
	return (res);
}

#include <stdio.h>

int main(int ac, char **av)
{
	if (ac == 2)
	{
		int n = ft_atoi(av[1]);
		int i = 0;
		int sum = 0;
		while (i <= n)
		{
			if (is_prime(i))
				sum += i;
			i++;
		}
		ft_putnbr(sum);
		write(1, "\n", 1);
	}
	else
		write(1, "0\n", 1);
	return (0);
}
