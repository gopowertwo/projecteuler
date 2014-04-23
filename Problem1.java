import java.lang.Math;

public class Problem1 {

	public static void main(String args[]) {
		
		int sum = 0;
		for(int i = 0; i < 1000; i++) {
			if(i % 3 == 0 || i % 5 == 0)
				sum += i;
		}	

		System.out.println(sum);

		int n = 999;
		int x = (int) Math.floor(n / 3);
		int y = (int) Math.floor(n / 5);
		int z = (int) Math.floor(n / 15);
		sum = 3*x*(x+1)/2 + 5*y*(y+1)/2 - 15*z*(z+1)/2;

		System.out.println(sum);

	} 

}
