/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putptr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ldauber <ldauber@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/11 10:49:15 by ldauber           #+#    #+#             */
/*   Updated: 2025/11/11 13:31:31 by ldauber          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libftprintf.h"

static void	ft_putchar_p(char c)
{
	write(1, &c, 1);
}

static int	ft_putnbr_p(unsigned long long n, char *base)
{
	int	len;

	len = 0;
	if (n >= 16)
		len += ft_putnbr_p((n / 16), base);
	ft_putchar_p(base[n % 16]);
	len++;
	return (len);
}

int	ft_putptr(void *p)
{
	int	len;

	len = 0;
	if (!p)
	{
		write(1, "(nil)", 5);
		return (5);
	}
	else
	{
		ft_putstr("0x");
		len += 2;
		len += ft_putnbr_p((unsigned long long)p, "0123456789abcdef");
	}
	return (len);
}
