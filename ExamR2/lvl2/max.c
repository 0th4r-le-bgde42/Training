/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   max.c                                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ldauber <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/05 10:21:00 by ldauber           #+#    #+#             */
/*   Updated: 2025/12/05 10:42:56 by ldauber          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#define LEN 4

int	max(int* tab, unsigned int len)
{
	unsigned int i = 0;
	int stock = 0;
	if (!tab)
		return (0);
	while (i < len)
	{
		if (tab[i] >= stock)
			stock = tab[i];
		i++;
	}
	return (stock);
}

int main()
{
	int tab[LEN] = {1, 2, 3, 4};
	printf("%d\n", max(tab, LEN));
	return (0);
}
