/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strcpy.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ldauber <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/02 14:57:45 by ldauber           #+#    #+#             */
/*   Updated: 2025/12/02 15:08:55 by ldauber          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

char	*ft_strcpy(char *s1, char *s2)
{
	int	i = 0;

	while(s1[i] && s2[i])
	{
		s1[i] = s2[i];
		i++;
	}
	s1[i] = '\0';
	return (s1);
}

int main(int ac, char **av)
{
	int	i = 0;
	if (ac == 3)
	{
		while (av[1][i] && av[2][i])
		{
			write(1, ft_strcpy(&av[1][i], &av[2][i]), 1);
			i++;
		}
	}
	write(1, "\n", 1);
	return (0);
}
