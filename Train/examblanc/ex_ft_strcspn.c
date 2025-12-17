/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ex_ft_strcspn.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ldauber <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/17 13:43:16 by ldauber           #+#    #+#             */
/*   Updated: 2025/12/17 14:06:07 by ldauber          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stddef.h>

int	is_reject(char c, const char *reject)
{
	int i = 0;
	while (reject[i])
	{
		if (c == reject[i])
			return (1);
		i++;
	}
	return (0);
}

size_t ft_strcspn(const char *s, const char *reject)
{
	size_t count = 0;
	int i = 0;
	while (s[i])
	{
		if (!is_reject(s[i], reject))
			count++;
		i++;
	}
	return (count);
}

#include <stdio.h>

int main(int ac, char **av)
{
	if (ac == 3)
		printf("%zu\n", ft_strcspn(av[1], av[2]));
	else
		printf("c faux");
	return (0);
}
