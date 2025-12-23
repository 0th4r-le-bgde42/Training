#include <unistd.h>

int comptelettre(char *s)
{
	int i = 0;
	while (s[i])
		i++;
	return (i);
}

void ecritmot(char *s)
{
	int i = comptelettre(s) - 1;
	while (i >= 0)
	{
		write(1, &s[i], 1);
		i--;
	}
	write(1, "\n", 1);
}

int main(int ac, char **av)
{
	int i = 1;
	if (ac > 1)
	{
		while (i < ac)
		{
			ecritmot(av[i]);
			i++;
		}
	}
	return (0);
}
