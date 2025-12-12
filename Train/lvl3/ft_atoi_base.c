/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_atoi_base.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ldauber <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/11 10:40:05 by ldauber           #+#    #+#             */
/*   Updated: 2025/12/12 10:04:57 by ldauber          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>

int ft_isspace(char c)
{
	if ((c >= 9 && c <= 13) || c == 32)
		return (1);
	return (0);
}
	
int ft_atoi_base(const char *str, int str_base)
{
	int i = 0;
	int sign = 1;
	int res = 0;
	while (ft_isspace(str[i]))
		i++;
	if (str[i] == '-' || str[i] == '+')
	{
		if (str[i] == '-')
			sign = -1;
		i++;
	}
	while (str[i])
	{
		res *= str_base;
		if (str[i] >= 48 && str[i] <= 57)
			res += (str[i] - 48);
		else if (str[i] >= 97 && str[i] <= 102)
			res += str[i] - 97 + 10;
		else if (str[i] >= 65 && str[i] <= 70)
			res += str[i] - 65 + 10;
		else
			break;
		i++;
	}
	return (res * sign);
}

int main()
{
	const char *str = "10";
	int str_base = 4;
	printf("%d\n", ft_atoi_base(str, str_base));
	return (0);
}
