package zeus;
import java.util.Scanner;

public class test 
{
	
	public static int square(int num)
	{
		int squaredNum = num*num;
		return squaredNum;
	}



	public static void main(String[] args) 
	{
		System.out.println("Hello!");
		Scanner keyboard = new Scanner(System.in);
		//System.out.println("Enter a word:");
		//String word = keyboard.nextLine();
		//System.out.println("Your word is: "+ word);
		
		System.out.println("Enter a number:");
		int num = keyboard.nextInt();

		for(int i = 1; i <= num; i++) 
		{
			if(i%2 == 0)
			{
				System.out.println(i);
			}			
		}
		
		System.out.println("Your number squared: " + square(num));
		
	}

}
