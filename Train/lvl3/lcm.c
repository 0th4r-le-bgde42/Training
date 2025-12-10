/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   lcm.c                                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ldauber <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/10 11:04:16 by ldauber           #+#    #+#             */
/*   Updated: 2025/12/10 11:11:04 by ldauber          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>

int hcf(unsigned int a, unsigned int b)
{
	if (b == 0)
		return (a);
	return (hcf(b, a % b));
}

int lcm(unsigned int a, unsigned int b)
{
	return (((a * b) / hcf(a, b)));
}

int main()
{
	unsigned int a = 259;
	unsigned int b = 1500000;
	printf("%d\n", lcm(a, b));
	return (0);
}
