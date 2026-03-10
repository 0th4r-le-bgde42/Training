/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strspn.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ldauber <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/03 14:45:07 by ldauber           #+#    #+#             */
/*   Updated: 2025/12/03 15:17:47 by ldauber          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stddef.h>
#include <stdio.h>
#include <string.h>

int is_charset(const char c, const char *accept)
{
	int i = -1;
	while (accept[++i])
		if (accept[i] == c)
			return (1);
	return (0);
}

size_t	ft_strspn(const char *s, const char *accept)
{
	int i = -1;
	while (s[++i] && is_charset(s[i], accept) == 1);
	return ((size_t)i);
}

int main(int ac, char **av)
{
	if (ac == 3)
	{
		printf("OG = %zu\n", ft_strspn(av[1], av[2]));
		printf("T = %zu\n", strspn(av[1], av[2]));
	}
	else
		printf("bouffon");
	return (0);
}
