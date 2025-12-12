/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_list_size.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ldauber <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/12 10:21:40 by ldauber           #+#    #+#             */
/*   Updated: 2025/12/12 10:38:17 by ldauber          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

typedef struct s_list
{
	struct s_list	*next;
	void			*data;
}					t_list;

int ft_list_size(t_list *begin_list)
{
	int i = 0;
	if (!begin_list)
		return (0);
	while (begin_list)
	{
		begin_list = begin_list->next;
		i++;
	}
	return (i);
}

#include <stdio.h>

int main(void)
{
    // Déclaration statique de trois nœuds
    t_list node3 = {NULL, "C"}; // Dernier élément, next est NULL
    t_list node2 = {&node3, "B"}; // Pointeur vers node3
    t_list node1 = {&node2, "A"}; // Tête de la liste, pointeur vers node2

    t_list *list_head = &node1; // Pointeur vers le début de la liste
    int size;

    printf("########## Test de ft_list_size ##########\n");
    
    // Test 1 : Liste complète (node1 -> node2 -> node3)
    size = ft_list_size(list_head);
    printf("#  Taille de la liste (A -> B -> C) : %d  #\n", size);

    // Test 2 : Liste d'un seul élément (en partant de node3)
    size = ft_list_size(&node3);
    printf("#    Taille de la liste (C seul) : %d     #\n", size);

    // Test 3 : Liste vide (NULL)
    size = ft_list_size(NULL);
    printf("#   Taille de la liste vide (NULL) : %d   #\n", size);

	printf("################# END ####################\n");

    return (0);
}
