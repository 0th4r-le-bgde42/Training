/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strcapitalize.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ldauber <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/13 11:17:41 by ldauber           #+#    #+#             */
/*   Updated: 2025/07/13 17:19:04 by ldauber          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

//#include <stdio.h>

char	*ft_strcapitalize(char *str)
{
	int		i;
	char	sp;

	i = 0;
	sp = ' ';
	while (str[i] != '\0')
	{
		if (str[i] >= 'A' && str[i] <= 'Z')
		{
			str[i] += 32;
		}
		if (!(sp >= 'A' && sp <= 'Z') && !(sp >= 'a' && sp <= 'z'))
		{
			if (!(sp >= '0' && sp <= '9'))
			{
				if (str[i] >= 'a' && str[i] <= 'z')
				{
					str[i] -= 32;
				}
			}
		}
		sp = str[i];
		i++;
	}
	return (str);
}
/*
int main()
{
	char tab[50] = {"hI, hOw aRe yOu? 42wORds foRty-tWo; fIFtY+and+onE"};
	printf("%s", ft_strcapitalize(tab));
}
*/
