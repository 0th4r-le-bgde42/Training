/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   reverse_bits.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ldauber <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/05 12:58:57 by ldauber           #+#    #+#             */
/*   Updated: 2025/12/05 13:53:35 by ldauber          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void	print_bits(unsigned char octet)
{
	int i = 8;
	unsigned char bit = 0;
	while(i--)
	{
		bit = (octet >> i & 1) + 48;
		write(1, &bit, 1);
	}
}
unsigned char	reverse_bits(unsigned char octet)
{
	int i = 8;
	unsigned char res = 0;

	while (i--)
	{
		res = (res << 1) | (octet & 1);
		octet = octet >> 1;
	}
	return (res);
}

int main()
{
	unsigned char octet = 3;
	unsigned char res = reverse_bits(octet);
	print_bits(res);
	return (0);
}
