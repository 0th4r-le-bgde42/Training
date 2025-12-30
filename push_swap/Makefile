# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ldauber <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/30 11:56:43 by ldauber           #+#    #+#              #
#    Updated: 2025/12/30 15:19:50 by ldauber          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

NAME = push_swap.a
CC = cc
CFLAGS = -Wall -Wextra -Werror -I .

AR = ar -rcs
RM = rm -f

SRC = \
	ft_printf.c ft_putchar.c ft_putnbr.c ft_putstr.c ft_putnbr_u.c \
	ft_putptr.c ft_putnbr_hex.c \
	swap.c push.c rotate.c

OBJ = $(SRC:.c=.o)

all: $(NAME)

$(NAME): $(OBJ)
    $(AR) $(NAME) $(OBJ)

%.o: %.c
    $(CC) $(CFLAGS) -I . -c $< -o $@

clean:
	$(RM) $(OBJ)

fclean: clean
    $(RM) $(NAME)

re: fclean all

.PHONY: all clean fclean re
