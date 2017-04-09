import java.util.Scanner;


public class Main {
	public static void main(String[] args) {
		//code to read input is 
		//FROM HERE
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();
		int[][] checkboard = new int[n][m];
		for(int i = 0; i < n; i++){
			int[] row = new int[m];
			for(int j=0; j < m; j++){
				checkboard[i][j] = sc.nextInt();
			}
		}
		//TO HERE
		
		//after this is uncompleted code for navigating the checkerboard.
		int sum = 0;
		if(checkboard[0][0] != 0 && checkboard[0][1] != 0){
			boolean feven = (checkboard[0][0] & 1) == 1;
			boolean seven = (checkboard[0][1] & 1) == 1;
			int num;
			for(int i = 0; i < n; i++){
				for(int j=0; j < m; j++){
					num = checkboard[i][j];
					if(num == 0){
						int up;
						if(i == 0){up = 0;}else{up = checkboard[i-1][j];}
						if(j == 0){left = 0;}else{left = checkboard[i][j-1];}
						Math.max(up, left);
						
					}
				}
			}
		
		}
	}
}
