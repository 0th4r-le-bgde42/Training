/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   add_prime_sum.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ldauber <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/09 10:47:19 by ldauber           #+#    #+#             */
/*   Updated: 2025/12/09 11:26:44 by ldauber          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void	ft_putnbr(long nb)
{
	if (nb < 0)
	{
		write(1, "-", 1);
		nb = -nb;
	}
	if (nb > 9)
		ft_putnbr(nb / 10);
	write(1, &"0123456789"[nb % 10], 1);
}

int	is_prime(int nb)
{
	int i = 2;
	if  (nb < 2)
		return (0);
	while (i <= nb / 2)
	{
		if (nb % i == 0)
			return (0);
		i++;
	}
	return (1);
}

int	ft_atoi(char *str)
{
	int i = 0;
	int sign = 1;
	int result = 0;
	while ((str[i] >= 9 && str[i] <= 13) || str[i] == 32)
		i++;
	if (str[i] == '-' || str[i] == '+')
		if(str[i++] == '-')
			sign = -1;
	while (str[i] && str[i] >= 48 && str[i] <= 57)
	{
		result *= 10;
		result += str[i] - 48;
		i++;
	}
	return (result * sign);
}

int	main(int ac, char **av)
{
	if (ac != 2 || ft_atoi(av[1]) <= 0)
		return (write(1, "0\n", 1), 0);
	int nb = ft_atoi(av[1]);
	int sum = 0;
	while (nb > 1)
	{
		if (is_prime(nb))
			sum += nb;
		nb--;
	}
	ft_putnbr(sum);
	return (0);
}
