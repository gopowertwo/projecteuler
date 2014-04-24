public class Problem6 { 

	public static void main(String args[]) {

		int n = 100;
		int sq_sum = n*n*(n+1)*(n+1)/4; // Use formula for sum of 1..n
		int sum_sq = (2*n+1)*(n+1)*n/6; // Use formula for 1^2 + 2^2 + ... + n*2

		System.out.println(sq_sum - sum_sq);

	} 

}
