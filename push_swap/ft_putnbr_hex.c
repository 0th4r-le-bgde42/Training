/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putnbr_hex.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ldauber <ldauber@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/11 11:29:04 by ldauber           #+#    #+#             */
/*   Updated: 2025/11/11 13:31:38 by ldauber          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libftprintf.h"

static void	ft_putchar_p(char c)
{
	write(1, &c, 1);
}

int	ft_putnbr_hex(unsigned int n, char *base)
{
	int	len;

	len = 0;
	if (n >= 16)
		len += ft_putnbr_hex((n / 16), base);
	ft_putchar_p(base[n % 16]);
	len++;
	return (len);
}
