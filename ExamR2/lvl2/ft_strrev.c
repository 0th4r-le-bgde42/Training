/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strrev.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ldauber <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/03 13:57:01 by ldauber           #+#    #+#             */
/*   Updated: 2025/12/03 14:18:05 by ldauber          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>

int	ft_strlen(char *str)
{
	int i = 0;
	while (str[++i]);
	return (i);
}

char	*ft_strrev(char *str)
{
	int start = 0;
	int end = ft_strlen(str) - 1;
	char temp;

	if (!str)
		return (0);
	while (str[start] && start < (ft_strlen(str) / 2))
	{
		temp = str[end];
		str[end] = str[start];
		str[start] = temp;
		start++;
		end--;
	}
	return (str);
}

int main(int ac, char **av)
{
	if (ac == 2)
		printf("%s\n", ft_strrev(av[1]));
	return (0);
}
