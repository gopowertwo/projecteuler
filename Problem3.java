import java.lang.Math;

public class Problem3 {

	public static void main(String args[]) {
		
		long n = 600851475143L;
		long largest = 0;

		for(int i = 2; i <= n / i; i++) {
			while(n % i == 0) {
				if( i > largest) largest = i;
				n /= i;
			}
		}

		if(n > 1 && n > largest) {
			largest = n;
		} 

		System.out.println(largest);

	} 

}
