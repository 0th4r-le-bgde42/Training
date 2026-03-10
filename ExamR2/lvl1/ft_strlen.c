/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlen.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ldauber <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/02 15:17:22 by ldauber           #+#    #+#             */
/*   Updated: 2025/12/03 14:03:46 by ldauber          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>
#include <stdio.h>
#include <string.h>

int	ft_strlen(char *str)
{
	int i = 0; 
	while (str[++i]); 
	return (i);
}

int main(int ac, char **av)
{
	if (ac == 2)
	{
		printf("len = %d\n", ft_strlen(av[1]));
		printf("vlen = %lu", strlen(av[1]));
	}
	return (0);
}
