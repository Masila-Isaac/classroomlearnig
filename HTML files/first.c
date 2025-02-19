# include <stdio.h>  //header file 
#define pi 3.142  // all this are preprocessor commands
int main()
{
	float radius, height, volume;
	printf("input the radius of the cylinder; ");
	scanf("%f", &radius);
	printf("input the height of the cylinder; ");
	scanf("%f", &height);
	volume = radius * radius * height * pi;
	printf("volume =%f", volume);

	return 0;
}
