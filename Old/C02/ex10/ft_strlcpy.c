/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcpy.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ldauber <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/13 17:34:26 by ldauber           #+#    #+#             */
/*   Updated: 2025/07/13 17:58:57 by ldauber          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

//#include <stdio.h>

int	ft_strlen(char *str)
{
	int		i;

	i = 0;
	while (str[i] != '\0')
	{
		i++;
	}
	return (i);
}

unsigned int	ft_strlcpy(char *dest, char *src, unsigned int size)
{
	unsigned int	src_l;
	unsigned int	i;

	i = 0;
	src_l = ft_strlen(src);
	if (size > 0)
	{
		while (src[i] != '\0')
		{
			if (i > size - 2)
			{
				dest[i] = '\0';
				break ;
			}
			else
			{
				dest[i] = src[i];
			}
			i++;
		}
	}
	return (src_l);
}
/*
int main()
{
	char tab1[] = {"Jpp vivement que ce soit fini"};
	char tab2[35];

	printf("%u", ft_strlcpy(tab2, tab1, 35));
	return 0;
}
*/
