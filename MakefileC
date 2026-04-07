# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    MAKEFILE                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ldauber <ldauber@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/10/29 14:38:11 by ldauber           #+#    #+#              #
#    Updated: 2025/11/03 09:18:58 by ldauber          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

NAME = libft.a
CC = cc
CFLAGS = -Wall -Wextra -Werror

SRC = ft_isalpha.c ft_isdigit.c ft_isalnum.c  ft_isascii ft_isdigit.c
    ft_isprint ft_strlen.c ft_memset.c ft_bzero.c ft_memcpy.c ft_memmove.c
    ft_strlcpy.c ft_strlcat.c ft_toupper.c ft_tolower.c ft_strchr.c
    ft_strrchr.c ft_strncmp.c ft_memchr.c ft_memcmp.c ft_strnstr.c ft_atoi.c
    ft_calloc.c ft_strdup.c ft_substr.c ft_strjoin.c ft_strim.c ft_split.c
    ft_itoa.c ft_strmapi.c ft_striteri.c ft_putchar_fd.c ft_putnbr_fd.c
DIR_SRC = $(patsubst %.c, srcs/%.c, $(SRC))
OBJ = $(patsubst %.c, %.o, $(DIR_SRC))
HEADER = includes

all: $(NAME)

$(NAME): $(OBJ)
    ar -rcs $(NAME) $(OBJ)

%.o: %.c
    $(CC) $(CFLAGS) -o $@ -c $? -I $(HEADER)

clean:
    rm -rf $(OBJ)

fclean: clean
    rm -rf $(NAME)

re: fclean all

.PHONY: all clean fclean re