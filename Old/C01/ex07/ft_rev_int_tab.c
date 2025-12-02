/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_rev_int_tab.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ldauber <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/10 19:44:18 by ldauber           #+#    #+#             */
/*   Updated: 2025/07/12 15:59:44 by ldauber          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

void	ft_rev_int_tab(int *tab, int size)
{
	int		i;
	int		temp;
	int		stock;

	i = 0;
	temp = size - 1;
	while (i < (size / 2))
	{
		stock = tab[i];
		tab[i] = tab[temp];
		tab[temp] = stock;
		i++;
		temp --;
	}
}
