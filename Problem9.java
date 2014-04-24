import java.lang.Math;

public class Problem9 {

	public static void main(String args[]) {

		for(int a = 1; a < 1000; a++) {
			for(int b = a+1; b < 1000 - a; b++) {
				double c = Math.sqrt(a*a + b*b);
				if(a + b + c == 1000 && c > b) {
					System.out.println(a*b*(int) c);
				}
			}
		}

	} 

}
