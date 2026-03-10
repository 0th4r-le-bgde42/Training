/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ex_search_and_replace.c                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ldauber <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/17 15:06:58 by ldauber           #+#    #+#             */
/*   Updated: 2025/12/17 15:31:03 by ldauber          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

int ft_strlen(char *s)
{
	int i = 0;
	while (s[++i]);
	return (i);
}

int main(int ac, char **av)
{
	int i = 0;
	if (ac == 4)
	{
		char search = av[2][0];
		char replace = av[3][0];
		char *str = av[1];
		if (ft_strlen(av[2]) > 1 || ft_strlen(av[3]) > 1)
			write(1, "\n", 1);
		else
		{
			while (str[i])
			{
				if (str[i] == search)
					str[i] = replace;
				write(1, &str[i], 1);
				i++;
			}
		}
	}
	else
		write(1, "\n", 1);
	return (0);
}
