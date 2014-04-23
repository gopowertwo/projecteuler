import java.lang.Math;

public class Problem2 {

	public static void main(String args[]) {
		
		int sum = 0;
		double phi = (1 + Math.sqrt(5))/2;
		double phi2 = (1 - Math.sqrt(5))/2;
		int fib = 0;
		int counter = 1;
		while(fib < 4*Math.pow(10, 6)) {
			fib = (int) ((Math.pow(phi, counter) - Math.pow(phi2,counter)) / Math.sqrt(5));
			if(fib % 2 == 0) 
				sum += fib;
			counter++;
		}

		System.out.println(sum);

	} 

}
