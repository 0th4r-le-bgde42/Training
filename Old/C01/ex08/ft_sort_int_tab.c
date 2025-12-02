/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_sort_int_tab.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ldauber <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/22 13:55:43 by ldauber           #+#    #+#             */
/*   Updated: 2025/07/31 09:52:15 by ldauber          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

void	ft_sort_int_tab(int *tab, int size)
{
	int	i;
	int	j;
	int	temp;

	i = 0;
	j = i + 1;
	temp = 0;
	while (i < size)
	{
		if (tab[i] > tab[j])
		{
			temp = tab[j];
			tab[j] = tab[i];
			tab[i] = temp;
			i = 0;
			j = i + 1;
		}
		else
		{
			i++;
			j++;
		}
	}
}
/*
#include <stdio.h>

int main()
{
    int tab[10] = {0, 8, 2, 6, 4, 5, 3, 7, 1, 9};
    int size = 10;
    int i = 0;
    ft_sort_int_tab(tab, size);
    while (i < size)
    {
        printf("%d", tab[i]);
        i++;
    }
    return (0);

}
*/
