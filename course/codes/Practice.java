/* 
public class Practice{
    public static void main(String[] args){
        //if-else statement
        int num=1;
        if (num>0){
          System.out.println("The number is positive")
        }else{
            System.out.println("The number is negative or zero")
        }
        //Switch statement
        int day=2;
        switch(day){
            case 1:
            System.out.println("Monday");
            break;
            case 2:
            System.out.print
        }


    }
}

*/

package grades;
public class Practice{
   public void showGrade(int a){
      if(a>=90){
        System.out.println("Grade:S")
      }else if(a>=80 && a<90){
        System.out.println("Grade:A")
      }else if(a>=70 && a<80){
         System.out.println("Grade:B")
      }else{
        System.out.println("Grade:C")
      }
   }
}