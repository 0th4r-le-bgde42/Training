/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   print_bits.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ldauber <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/05 10:45:01 by ldauber           #+#    #+#             */
/*   Updated: 2025/12/05 12:02:21 by ldauber          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

void	print_bits(unsigned char octet)
{
	int i = 8; /*Déclare et initialise un compteur i à 8 utiliser pour parcourir l'octet qu'on attend avec l'unsigned char*/
	unsigned char bit = 0;

	while (i--)
	{
		bit = (octet >> i & 1) + 48;
		/*
		octet >> i : Décale l'octet vers la droite de i positions. 
					 Ceci place le bit que nous voulons examiner (de 7 à 0) à la position la plus à droite (position 0)
		& 1 : Effectue un ET binaire avec 1. Cela isole le bit 0, donnant soit 0, soit 1.
		+ 48 : Ajoute 48 = caractère '0' a la valeur décimale en ASCII, et le caractère '1' a la valeur 49. 
			   Ajouter 48 transforme le bit 0 en caractère '0', et le bit 1 en caractère '1'.
		*/
		write (1, &bit, 1);
	}
}

int main()
{
	unsigned char octet = 3;
	print_bits(octet);
}
