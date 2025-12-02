/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_numbers.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ldauber <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/09 12:24:56 by ldauber           #+#    #+#             */
/*   Updated: 2025/07/09 15:36:31 by ldauber          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void	ft_print_numbers(void)
{
	int		numbers;

	numbers = 48;
	while (numbers <= 57)
	{
		write(1, &numbers, 1);
		numbers += 1;
	}
}

/*
int main()
{
	ft_print_numbers();
	return 0;
}
*/
