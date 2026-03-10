/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   str_capitaliser.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ldauber <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/12 11:27:17 by ldauber           #+#    #+#             */
/*   Updated: 2025/12/12 11:33:40 by ldauber          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void str_capitalizer(char *str)
{
    int i = 0;
    while (str[i])
    {
        if (str[i] >= 65 && str[i] <= 90)
            str[i] += 32;
        if (str[i] >= 97 && str[i] <= 122 && str[i - 1] == 32)
            str[i] -= 32;
		if (str[0] >= 97 && str[0] <= 122)
			str[0] -= 32;
        write(1, &str[i], 1);
        i++;
    }
}

int main(int ac, char **av)
{
    int i = 1;
    if (ac > 1)
    {
        while (i < ac)
        {
            str_capitalizer(av[i]);
            write(1, "\n", 1);
            i++;
        }
    }
    else
        write(1, "\n", 1);
    return (0);
}

