/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ex_ulstr.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ldauber <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/17 10:30:50 by ldauber           #+#    #+#             */
/*   Updated: 2025/12/17 10:46:15 by ldauber          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>
#include <stdio.h>

void swap_case(char *s)
{
	int i = 0;
	while (s[i])
	{
		if (s[i] >= 65 && s[i] <= 90)
			s[i] += 32;
		else if (s[i] >= 97 && s[i] <= 122)
			s[i] -= 32;
		i++;
	}
}

int main(int ac, char **av)
{
	int i = 0;
	if (ac == 2)
	{
		swap_case(av[1]);
		while (av[1][i])
		{
			write(1, &av[1][i], 1);
			i++;
		}
	}
	write(1, "\n", 1);
	return (0);
}
