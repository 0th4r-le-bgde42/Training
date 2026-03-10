/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   rstr_capitalizer.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ldauber <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/12 10:59:58 by ldauber           #+#    #+#             */
/*   Updated: 2025/12/12 11:24:48 by ldauber          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void uncapitalizer(char *str)
{
	int i = 0;
	while (str[i])
	{
		if (str[i] >= 65 && str[i] <= 90)
			str[i] += 32;
		if (str[i] >= 97 && str[i] <= 122 && (str[i + 1] == 32 || str[i + 1] == 0))
			str[i] -= 32;
		write(1, &str[i], 1);
		i++;
	}
}

int main(int ac, char **av)
{
	int i = 1;
	if (ac > 1)
	{
		while (i < ac)
		{
			uncapitalizer(av[i]);
			write(1, "\n", 1);
			i++;
		}
	}
	else
		write(1, "\n", 1);
	return (0);
}
