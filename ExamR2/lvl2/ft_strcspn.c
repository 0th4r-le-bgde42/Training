/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strcspn.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ldauber <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/03 13:01:43 by ldauber           #+#    #+#             */
/*   Updated: 2025/12/03 13:21:32 by ldauber          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stddef.h>
#include <stdio.h>
#include <string.h>

int	is_charset(const char c, const char *reject)
{
	int i = 0;
	while (reject[i])
	{
		if (reject[i] == c)
			return (1);
		i++;
	}
	return (0);
}

size_t	ft_strcspn(const char *s, const char *reject)
{
	int i = 0;
	while (s[i])
	{
		if (is_charset(s[i], reject) == 1)
			break;
		i++;
	}
	return (i);
}

int main(int ac, char **av)
{
	if (ac == 3)
	{
		printf("0 = %zu\n", ft_strcspn(av[1], av[2]));
		printf("1 = %zu\n", strcspn(av[1], av[2]));
	}
	return (0);
}
