/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strdup.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ldauber <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/07/21 06:51:37 by ldauber           #+#    #+#             */
/*   Updated: 2025/07/21 08:06:28 by ldauber          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>

int	ft_strlen(char *src)
{
	int	i;

	i = 0;
	while (src[i])
		i++;
	return (i);
}

char	*ft_strdup(char *src)
{
	char	*new_str;
	char	*dup;

	dup = (char *)malloc (sizeof (char) * ft_strlen(src) + 1);
	if (dup == 0)
		return (0);
	new_str = dup;
	while (*src)
	{
		*new_str = *src;
		new_str++;
		src++;
	}
	*new_str = '\0';
	return (dup);
}

/*
#include <stdio.h>
#include <string.h>
int main()
{
    char OGs[10] = "21st CSM";
    char *DPs;
    char *Ts;
    int dp_len;

    DPs = ft_strdup(OGs);
    Ts = strdup(OGs);
    dp_len = ft_strlen(DPs);
    printf("Ma fonction prend :%s: en source et duplique :%s: 
		et mesure :%d: carac\n", OGs, DPs, dp_len);
    printf("La vraie fonction prend :%s: en source et duplique :%s: 
		et mesure :%d: carac\n", OGs, Ts, dp_len);
    return (0);

}
*/
