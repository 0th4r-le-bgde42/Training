/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strpbrk.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ldauber <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/03 13:45:13 by ldauber           #+#    #+#             */
/*   Updated: 2025/12/03 13:56:31 by ldauber          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>

int	ft_is_charset(const char c, const char *s2)
{
	int	i = 0;
	while (s2[i])
	{
		if (s2[i] == c)
			return (1);
		i++;
	}
	return (0);
}

char	*ft_strpbrk(const char *s1, const char *s2)
{
	while (*s1)
	{
		if (ft_is_charset(*s1, s2) == 1)
			return ((char *)s1);
		s1++;
	}
	return(0);
}

int main(int ac, char **av)
{
	if (ac == 3)
		printf("%s\n", ft_strpbrk(av[1], av[2]));
	return (0);
}
