public class Problem4 {

	public static void main(String args[]) {

		int result = 0;

		for(int i = 999; i > 100; i--) {
			for(int j = 999; j > 100; j--) {

				int x = (int) (i*j) / 1000;
				int y = 0;
				int t = (i*j) % 1000;
				while(t != 0) {
					y *= 10;	
					y += t%10;
					t /= 10;
				}

				if(x == y && i*j > result) {
					result = i*j;		
				}
			}
		}
	
		System.out.println(result);

	}

}
