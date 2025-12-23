#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>

int comptelettre(char *s)
{
	int i = 0;
	while (s[i])
		i++;
	return (i);
}
int trouvemot(char *s1, char *s2)
{
	int i = 0;
	int j = 0;
	int t = 0;
	int res = 0;
	char *tmp = malloc(comptelettre(s1 + 1) *sizeof(char));
	if (!tmp)
		return (0);
	while (s2[i])
	{
		while (s1[j])
		{
			if (s2[i] == s1[j])
			{
				tmp[t] = s2[i];
				t++;
				j++;
			}
			else
				break ;
		}
		i++;
	}
	tmp[t] = '\0';
	if (comptelettre(s1) == comptelettre(tmp))
		res = 1;
	else
		res = 0;
	free(tmp);
	return (res);
}

int main(int ac, char **av)
{
	if (ac == 3)
	{
		char *s1 = av[1];
		char *s2 = av[2];
		if (!trouvemot(s1, s2))
			write(1, "non", 3);
		else
			write(1, "oui", 3);
	}
	write(1, "\n", 1);
	return (0);
}
