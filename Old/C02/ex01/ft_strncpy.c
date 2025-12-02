/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strncpy.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ldauber <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/12 18:59:44 by ldauber           #+#    #+#             */
/*   Updated: 2025/07/13 17:28:33 by ldauber          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

//#include <stdio.h>

char	*ft_strncpy(char *dest, char *src, unsigned int n)
{
	char			*tempd;
	unsigned int	i;

	i = 0;
	tempd = dest;
	while (i < n)
	{
		if (*src == '\0' && i < n)
		{
			*dest = '\0';
		}
		else
		{
			*dest = *src;
			src++;
		}
		dest++;
		i++;
	}
	return (tempd);
}
/*
int main()
{
	char tab1[]= {"42 c'est trop bien!"};
	char tab2[25];

	ft_strncpy(tab2, tab1, 26);
	printf("%s", tab2);

	return 0;
}
*/
