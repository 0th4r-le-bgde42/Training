/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   p_s.c                                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ldauber <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/30 10:01:42 by ldauber           #+#    #+#             */
/*   Updated: 2025/12/30 10:19:40 by ldauber          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

void sa(int *i, int *j)
{
	int tmp;
	tmp = *i;
	*i = *j;
	*j = tmp;
}

void sb(int *i, int *j)
{
	int tmp;
	tmp = *i;
	*i = *j;
	*j = tmp;
}

void ss(int *ia, int *ja, int *ib, int *jb)
{
	sa(ia, ja);
	sb(ib, jb);
}

#include <stdio.h>

int main()
{
	int i[2] = {10, 5};
	int j[2] = {15, 0};
	printf("classic i = %d, %d\nclassic j = %d, %d\n\n", i[0], i[1], j[0], j[1]);
	sa(&i[0], &i[1]);
	printf("sa = %d, %d\n\n", i[0], i[1]);
    sb(&j[0], &j[1]);
	printf("sb = %d, %d\n\n", j[0], j[1]);
	ss(&i[0], &i[1], &j[0], &j[1]);
	printf("ss a = %d, %d\nss b = %d, %d\n", i[0], i[1], j[0], j[1]);
	return (0);
}
