/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strdup.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ldauber <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/03 13:24:12 by ldauber           #+#    #+#             */
/*   Updated: 2025/12/03 13:42:08 by ldauber          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include <stdio.h>

int ft_strlen(char *src)
{
	int i = 0;
	while (src[++i]);
	return (i);
}

char	*ft_strdup(char *src)
{
	char	*dup;
	int		i = -1;
	if (!src)
		return (0);
	dup = malloc((ft_strlen(src) + 1) * sizeof (char));
	if (!dup)
		return (0);
	while (src[++i])
		dup[i] = src[i];
	dup[i] = '\0';
	return (dup);
}

int main(int ac, char **av)
{
	if (ac == 2)
		printf("%s\n", ft_strdup(av[1]));
	return (0);
}
