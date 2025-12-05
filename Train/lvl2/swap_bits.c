/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   swap_bits.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ldauber <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/05 13:26:16 by ldauber           #+#    #+#             */
/*   Updated: 2025/12/05 13:33:48 by ldauber          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void print_bits(unsigned char octet)
{
	int i = 8;
	unsigned char bit = 0;
	while (i--)
	{
		bit = (octet >> i & 1) + 48;
		write(1, &bit, 1);
	}
}

unsigned char swap_bits(unsigned char octet)
{
	return ((octet >> 4 | octet << 4));
}

int main()
{
	unsigned char octet = 3;
	print_bits(octet);
	write(1, "\n", 1);
	unsigned char res = swap_bits(octet);
	print_bits(res);
	return (0);
}
