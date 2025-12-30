/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ldauber <ldauber@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/10 15:09:41 by ldauber           #+#    #+#             */
/*   Updated: 2025/11/27 12:40:51 by ldauber          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libftprintf.h"

static int	ft_write_to_percent(const char **str)
{
	int	len;

	len = 0;
	while (**str && **str != '%')
	{
		len += ft_putchar((unsigned int)**str);
		(*str)++;
	}
	return (len);
}

static int	ft_types(va_list args, char c)
{
	int	len;

	len = 0;
	if (c == 'i' || c == 'd')
		len += ft_putnbr(va_arg(args, int));
	if (c == 's')
		len += ft_putstr(va_arg(args, char *));
	if (c == 'c')
		len += ft_putchar(va_arg(args, unsigned int));
	if (c == 'u')
		len += ft_putnbr_u(va_arg(args, unsigned int));
	if (c == '%')
		len += ft_putchar('%');
	if (c == 'p')
		len += ft_putptr(va_arg(args, void *));
	if (c == 'x')
		len += ft_putnbr_hex(va_arg(args, unsigned int), "0123456789abcdef");
	if (c == 'X')
		len += ft_putnbr_hex(va_arg(args, unsigned int), "0123456789ABCDEF");
	return (len);
}

int	ft_printf(const char *str, ...)
{
	va_list	args;
	int		len;

	va_start(args, str);
	len = 0;
	while (*str)
	{
		len += ft_write_to_percent(&str);
		if (*str == '%')
		{
			str++;
			len += ft_types(args, *str);
			str++;
		}
	}
	va_end(args);
	return (len);
}

#include <stdio.h>
#include <limits.h>

int main(void)
{
/*     int ret1, ret2;

    ft_printf("Test chaînes:\n");
    ret1 = printf("printf:    Hello %s!\n", "world");
    ret2 = ft_printf("ft_printf: Hello %s!\n", "world");
    printf("Return: printf=%d, ft_printf=%d\n\n", ret1, ret2);

    ft_printf("Test caractères:\n");
    ret1 = printf("printf:    Char: %c\n", 'A');
    ret2 = ft_printf("ft_printf: Char: %c\n", 'A');
    printf("Return: printf=%d, ft_printf=%d\n\n", ret1, ret2);

    ft_printf("Test entiers:\n");
    ret1 = printf("printf:    Int: %d, %i\n", 42, -42);
    ret2 = ft_printf("ft_printf: Int: %d, %i\n", 42, -42);
    printf("Return: printf=%d, ft_printf=%d\n\n", ret1, ret2);

    ft_printf("Test unsigned:\n");
    ret1 = printf("printf:    Unsigned: %u\n", UINT_MAX);
    ret2 = ft_printf("ft_printf: Unsigned: %u\n", UINT_MAX);
    printf("Return: printf=%d, ft_printf=%d\n\n", ret1, ret2);

    ft_printf("Test hexadécimal:\n");
    ret1 = printf("printf:    Hex: %x, %X\n", 255, 255);
    ret2 = ft_printf("ft_printf: Hex: %x, %X\n", 255, 255);
    printf("Return: printf=%d, ft_printf=%d\n\n", ret1, ret2);

    ft_printf("Test pointeur:\n");
    void *ptr = &ret1;
    ret1 = printf("printf:    Pointer: %p\n", ptr);
    ret2 = ft_printf("ft_printf: Pointer: %p\n", ptr);
    printf("Return: printf=%d, ft_printf=%d\n\n", ret1, ret2);
	
	ft_printf("Test pourcentage:\n");
    ret1 = printf("printf:    Percent: %%\n");
    ret2 = ft_printf("ft_printf: Percent: %%\n");
    printf("Return: printf=%d, ft_printf=%d\n\n", ret1, ret2);

    ft_printf("Test NULL string:\n");
	ret1 = printf("printf:    NULL string: %s\n", (char *)NULL);
    ret2 = ft_printf("ft_printf: NULL string: %s\n", (char *)NULL);
    printf("Return: printf=%d, ft_printf=%d\n\n", ret1, ret2);

	ft_printf("Test NULL pointeur:\n");
	ret1 = printf("printf:    NULL string: %p\n", (char *)NULL);
    ret2 = ft_printf("ft_printf: NULL string: %p\n", (char *)NULL);
    printf("Return: printf=%d, ft_printf=%d\n\n", ret1, ret2);
	
    ft_printf("Test limites:\n");
    ret1 = printf("printf:    INT_MIN: %d, INT_MAX: %d\n", INT_MIN, INT_MAX);
    ret2 = ft_printf("ft_printf: INT_MIN: %d, INT_MAX: %d\n", INT_MIN, INT_MAX);
    printf("Return: printf=%d, ft_printf=%d\n\n", ret1, ret2); */

	/*ft_printf("Test mix:\n");
	int d = 10;
	char *s = "Huber Alphonse";
	unsigned int u = -127;
	printf("%d\n\n", printf("printf:     Bonjour a tous,\n
	 je compte jusqu'a %d\n
	 mon nom est %s et mes initiales sont %c.%c\n
	 J'aime le chiffre %u, et le symbole. %%\n
	 Mon papa est un pointeur dont l'adresse est %p
	 et ses codes sont %x et %X\n", d, s, 'H', 'A', u, s, 88, 112));
	ft_printf("%d\n\n", ft_printf("ft_printf:  Bonjour a tous,\n
	 je compte jusqu'a %d\nmon nom est %s et mes initiales sont %c.%c.\n
	 J'aime le chiffre %u, et le symbole. %%\n
	 Mon papa est un pointeur dont l'adresse est %p 
	 et ses codes sont %x et %X\n", d, s, 'H', 'A', u, s, 88, 112));*/
	return (0);
}
