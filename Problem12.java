public class Problem12 {

	public static void main(String args[]) {

		long sum = 0L;
		int p = 1;
		
		while(true) {
			int counter = 1;
			sum += p;
			p++;
			long n = sum;
			long current = 0L;
			int tmp = 0;

			for (long j = 2; j*j <= n; j++) {
	            while (n % j == 0) {

	            	if(current == 0) {
	            		current = j;
	            		tmp = 0;
	            	}

	            	if(current == j) {
	            		tmp++;
	            	} else {
	            		counter *= (tmp + 1);
	            		current = j;
	            		tmp = 1;
	            	}

	                n = n / j;
	            }

	        }

	        counter *= (tmp + 1);
	        if (n > 1)	counter *= 2;

	        if(counter > 500) {
	         	System.out.println(sum);
	           	break;
	        }
	    }

	} 

}
