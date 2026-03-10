/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   last_word.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ldauber <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/04 10:06:37 by ldauber           #+#    #+#             */
/*   Updated: 2025/12/04 11:31:02 by ldauber          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

int ft_strlen(char *str)
{
	int i = 0;
	while (str[++i]);
	return (i);
}

int main (int ac, char **av)
{
	int i = ft_strlen(av[1]);
	if (ac == 2)
	{
		while (av[1][--i] == 9 || av[1][--i] == 32);
		while (i >= 0)
		{
			i--;
			if (av[1][i] == 9 || av[1][i] == 32)
			{
				while (av[1][++i])
				{
					if (av[1][i] == 9 || av[1][i] == 32)
						break;
					write(1, &av[1][i], 1);

				}
				break;
			}
		}
	}
	write(1, "\n", 1);
}
