/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strjoin.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ldauber <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/21 10:24:24 by ldauber           #+#    #+#             */
/*   Updated: 2025/07/31 10:57:57 by ldauber          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>

int	strlen_max(int size, char **strs, char *sep)
{
	int	i;
	int	j;
	int	c;
	int	l;

	i = 0;
	l = 0;
	c = 0;
	while (i < size)
	{
		j = 0;
		while (strs[i][j++])
			l++;
		i++;
	}
	while (sep[c])
		c++;
	return (l + (c * (size - 1)));
}

char	ft_strcat(int size, char *dest, char **strs, char *sep)
{
	int	i;
	int	j;
	int	a;

	a = 0;
	i = 0;
	while (i < size)
	{
		j = 0;
		while (strs[i][j])
			dest[a++] = strs[i][j++];
		j = 0;
		while (sep[j] && i < size -1)
			dest[a++] = sep[j++];
		i++;
	}
	dest[strlen_max(size, strs, sep)] = '\0';
	return (*dest);
}

char	*ft_strjoin(int size, char **strs, char *sep)
{
	char	*dest;

	if (size <= 0)
	{
		dest = malloc(sizeof(char));
		dest[0] = '\0';
		return (dest);
	}
	dest = malloc(sizeof(char) * (strlen_max(size, strs, sep) + 1));
	if (dest == NULL)
		return (NULL);
	ft_strcat(size, dest, strs, sep);
	return (dest);
}
/*
#include <stdio.h>
int main()
{
    int		size = 1;
    char	*sep = "--";
    char	*strs[] = {"Jpp", "de", "cet", "exo", "de", "mort"};
    char	*result = ft_strjoin(size, strs , sep);

    printf("%s", result);
	free(result);
    return (0);
}
*/
