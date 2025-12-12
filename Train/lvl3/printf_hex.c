/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   printf_hex.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ldauber <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/12 10:50:23 by ldauber           #+#    #+#             */
/*   Updated: 2025/12/12 10:57:04 by ldauber          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void ft_putnbr(long nb)
{
	if (nb > 15)
		ft_putnbr(nb / 16);
	write(1, &"0123456789abcdef"[nb % 16], 1);
}

int ft_atoi(char *str)
{
	int res = 0;
	int i = 0;
	while (str[i])
	{
		res *= 10;
		res += str[i] - 48;
		i++;
	}
	return (res);
}

int main(int ac, char **av)
{
	if (ac == 2)
	{
		ft_putnbr(ft_atoi(av[1]));
	}
	write(1, "\n", 1);
	return (0);
}
