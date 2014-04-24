public class Problem7 {

	public static void main(String args[]) {

		int border = 1000000;

		// Sieve of Eratosthenes
		boolean[] prime = new boolean[border+1];
		for(int i = 2; i <= border; i++) {
			prime[i] = true;
		}

		for(int i = 2; i*i < border; i++) {
			if(prime[i]) {
				int j = i;
				while(i*j <= border) {
					prime[i*j] = false;
					j++;
				}
			}		
		}

		int counter = 0;
		for(int i = 1; i <= border; i++) {
			if(prime[i]) counter++;

			if(counter == 10001) {
				System.out.println(i);
				break;
			}
			
		}

	}
}
