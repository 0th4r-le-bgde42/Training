/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_comb.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ldauber <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/10 09:46:47 by ldauber           #+#    #+#             */
/*   Updated: 2025/07/10 09:55:30 by ldauber          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void	ft_print(char k1, char k2, char k3)
{
	char	fin [2];

	fin [0] = ',';
	fin [1] = ' ';
	write (1, &k1, 1);
	write (1, &k2, 1);
	write (1, &k3, 1);
	if (k1 != '7' || k2 != '8' || k3 != '9')
	{
		write (1, &fin, 2);
	}
}

void	ft_print_comb(void)
{
	char	k1;
	char	k2;
	char	k3;

	k1 = '0';
	while (k1 <= '7')
	{
		k2 = k1 + 1;
		while (k2 < '8')
		{
			k3 = k2 + 1;
			while (k3 < '9')
			{
				ft_print(k1, k2, k3);
				k3 += 1;
			}
			ft_print(k1, k2, k3);
			k2 += 1;
		}
		ft_print(k1, k2, k3);
		k1 += 1;
	}
}

/*
int main(void)
{
    ft_print_comb();
    return (0);
}
*/
