/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strs_to_tab.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ldauber <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/23 14:39:39 by ldauber           #+#    #+#             */
/*   Updated: 2025/07/24 09:35:38 by ldauber          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_stock_str.h"
#include <stdlib.h>

int	ft_strlen(char *str)
{
	int	i;

	i = 0;
	while (str[i] != '\0')
		i++;
	return (i);
}

char	*ft_strcpy(char *str, int size)
{
	int		i;
	char	*ret;

	i = 0;
	ret = 0;
	ret = malloc(sizeof(char) * (size +1));
	while (str[i] != '\0')
	{
		ret[i] = str[i];
		i++;
	}
	ret[i] = '\0';
	return (ret);
}

struct	s_stock_str	*ft_strs_to_tab(int ac, char **av)
{
	t_stock_str	*ret;
	int			i;

	i = 0;
	ret = ((t_stock_str *)malloc(sizeof(t_stock_str) * (ac + 1)));
	if (ret == 0)
		return (0);
	while (i < ac)
	{
		ret[i].size = ft_strlen(av[i]);
		ret[i].str = av[i];
		ret[i].copy = ft_strcpy(av[i], ret[i].size);
		i++;
	}
	ret[i].size = 0;
	ret[i].str = 0;
	ret[i].copy = 0;
	return (ret);
}
/*
#include <stdio.h>

int main()
{
	char *ret[] = {"pousser", "mamie", "dans","les", "orties"};
	t_stock_str *g = ft_strs_to_tab(5, ret);
	int i = 0;
	int j = (ft_strlen(ret[0]) + ft_strlen(ret[1]) + ft_strlen(ret[2]) 
		+ ft_strlen(ret[3]) + ft_strlen(ret[4]));
	while (g[i].str)
	{
		printf("str:%s\n", g[i].str);
		printf("copy:%s\n", g[i].copy);
		printf("size:%d\n\n", g[i].size);
		i++;
	}
	printf("%s %s %s %s %s %d fois\n", g[0].str, g[1].copy, g[2].str, 
		g[3].copy, g[4].str, j);
	free(g);
	return (0);
}
*/
