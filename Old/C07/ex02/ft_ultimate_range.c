/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_ultimate_range.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ldauber <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/21 08:35:46 by ldauber           #+#    #+#             */
/*   Updated: 2025/07/22 15:36:42 by ldauber          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>

int	ft_ultimate_range(int **range, int min, int max)
{
	int		i;
	int		*arr;

	i = 0;
	if (min >= max)
	{
		*range = NULL;
		return (0);
	}
	arr = (int *) malloc(sizeof (int) * (max - min));
	if (arr == NULL)
	{
		*range = NULL;
		return (-1);
	}
	*range = arr;
	while (min < max)
	{
		arr[i] = min;
		min++;
		i++;
	}
	return (i);
}
/*
#include <stdio.h>
int main(void)
{
    int* arr;
    int i = 0;
	int n = 2;
	int min = -12;
	int max = 6;

    arr = (int*)malloc(sizeof(int) * n);
    printf("%d\n", ft_ultimate_range(&arr, min, max));
    while (i < n)
    {
        printf("%d ", arr[i]);
        i++;
    }
    return 0;
}
*/
