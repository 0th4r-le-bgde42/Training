/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strncmp.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ldauber <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/13 14:46:37 by ldauber           #+#    #+#             */
/*   Updated: 2025/07/16 13:40:42 by ldauber          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_strncmp(char *s1, char *s2, unsigned int n)
{
	unsigned int	i;

	i = 0;
	if (!n)
		return (0);
	while (i < n - 1 && s1[i] == s2[i] && s1[i])
		i++;
	return (s1[i] - s2[i]);
}

/*
#include <stdio.h>
#include <string.h>
int main()
{
    char *s1 = "ABC";
    char *s2 = "ABF";
    printf("%d\n", ft_strncmp(s1, s2, 3));
	printf("%d", strncmp(s1, s2, 3));
    return 0;
}
*/
