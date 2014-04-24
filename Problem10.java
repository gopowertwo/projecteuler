public class Problem10 {

	public static void main(String args[]) {

		int border = 2000000;

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

		long sum = 0L; // Overflow if int
		for(int i = 2; i <= border; i++) {
			if(prime[i]) sum += i;
		}

		System.out.println(sum);

	} 

}
