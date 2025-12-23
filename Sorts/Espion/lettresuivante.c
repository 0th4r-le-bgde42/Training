#include <unistd.h>

void ecritcarac(char s)
{
	write(1, &s, 1);
}

void lettresuivante(char *s)
{
	int i = 0;
	while (s[i])
	{
		if ((s[i] >= 65 && s[i] <= 90) || (s[i] >= 97 && s[i] <= 122))
		{
			if (s[i] == 90)
				s[i] = 65;
			else if (s[i] == 122)
				s[i] = 97;
			else
				s[i] = s[i] + 1;
		}
		ecritcarac(s[i]);
		i++;
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
			lettresuivante(av[i]);
			i++;
		}
	}
	return (0);
}
