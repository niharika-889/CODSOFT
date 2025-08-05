

/* 
public class Hello{
  public String name;
  public String breed;
  public int age;
  public void writeoutput(){
    System.out.println("Name:"+name);
    System.out.println("Breed"+breed);
    System.out.println("Age in calendar years"+age);
    System.out.println("Age in human years:"+ getageinhumanyears());
    System.out.println();
  }
    public int getageinhumanyears(){
       int humanage=0;
       if(age<=20){
        humanage=age*11;
       }else{
        humanage= 22+((age-2)*5);
       }
       return humanage;
    } 
    
    
}

*/
/* 
import java.util.Scanner;
class Cat{

  String consumerName ;
  int consumerNumber ;
  int previousMonthReading ;
  int currentMonthReading ;
  
  Cat(String consumerName,int consumerNumber,int previousMonthReading,int currentMonthReading){
      this.consumerName=consumerName;
      this.consumerNumber=consumerNumber;
      this.previousMonthReading = previousMonthReading;
      this.currentMonthReading = currentMonthReading;
  }

   public double  calculateBillAmount(){
        int unitsConsumed= currentMonthReading - previousMonthReading;
        double billAmount=0;
        
        if (unitsConsumed<=100){
          billAmount=unitsConsumed*1;         
        }
        else if(unitsConsumed<=200){
          billAmount=(100*1)+((unitsConsumed-100)*2.50);
        }
        else if(unitsConsumed<=500){
          billAmount=(100*1)+(100*2.50)+((unitsConsumed-200)*4);
        }
        else{
          billAmount=(100*1)+(100*2.50)+(300*4)+((unitsConsumed-500)*6);

        }
         return billAmount ;
}


       public void displayBill(){
        System.out.println("consumer name  "+consumerName);
        System.out.println("consumer number  "+consumerNumber);
        System.out.println("previous month reading  "+previousMonthReading);
        System.out.println("current month reading  "+currentMonthReading);


       }
       



      public static void main(String[] args){
          Scanner sc=new Scanner (System.in);
          String consumerName=sc.nextLine();
          int consumerNumber=sc.nextInt();
          int previousReading=sc.nextInt();
          int currentReading=sc.nextInt();

          Cat bill=new Cat(consumerName,consumerNumber, previousReading, currentReading);
          System.out.println((int)bill.calculateBillAmount());

          sc.close();

          bill.displayBill();




      }
}
*/

/* 
import java.util.Scanner;
public class Hello{
    public static void main(String args[]){
      Scanner sc= new Scanner(System.in);
      System.out.print("Enter size of the array:");
      int n=sc.nextInt();
      int arr[]=new int[n];

      System.out.print("enter "+n+" numbers");

      for(int i=0; i<n;i++){
        arr[i]=sc.nextInt();
      }
      
      int[] encoded=new int[n];
      for (int i=0;i<n-1;i++){
        encoded[i]=arr[i]+arr[i+1];
        encoded[n-1]=arr[n-1];
      }

      System.out.print("Encoded array = [");
      for (int i=0;i<n;i++){
        System.out.print(encoded[i]);
        if (i<n-1){
          System.out.print(",");
        }
      }
        System.out.println("]");

      int middle=encoded[n/2];
      System.out.println("Middle element in encoded array is "+middle);

      int sum=0;
      for (int num:encoded){
        sum+=num;
      }
      System.out.println("Sum of all numbers in encoded array= "+sum);



    }
}
*/
/* 


 class Hello{
  double dimension;
  Hello(double dimension){
    this.dimension=dimension;
  }
}
  class Circle extends Hello{
    public  Circle(double radius){
       super(radius);
     }
     double calculateArea(){
       return Math.PI*dimension*dimension;
     }
     double calculateCircumference(){
      return 2*Math.PI*dimension;
    }
  }
  class Square extends Hello{
     public  Square(double side){
        super(side);
      }
      double calculateArea(){
        return dimension*dimension;
      }
      double calculateDiagonal(){
        return Math.sqrt(2)*dimension;
      }

  }   
   class Sphere extends Hello{
     public Sphere(double radius){
      super(radius);
    }
    double calculateVolume(){
      return (4.0/3.0)*Math.PI*Math.pow(dimension,3);
    }
    double calculateSurfaceArea(){
     return 4*Math.PI*dimension*dimension;

    }
  }

   public class ShapeTest{
    public static void main(String[] args){
        Circle circle=new Circle(5);
        System.out.println("Circle Area : "+circle.calculateArea());
        System.out.println("Circle Circumference :"+circle.calculateCircumference());

        Square square= new Square(4);
        System.out.println("Square area :"+square.calculateArea());
        System.out.println("Square diagonal :"+square.calculateDiagonal());

        Sphere sphere=new Sphere(3);
        System.out.println("Sphere volume :"+sphere.calculateVolume());
        System.out.println("Sphere surface area: "+sphere.calculateSurfaceArea());
    }
  }
*/

/* 
import java.util.Scanner;
class BankAccount{
   double balance;
   public BankAccount(double initialBalance){
    this.balance=initialBalance;
   }
   public void deposit(double amount){
      if (amount>0){
          balance +=amount;
        System.out.println("Deposited: "+amount);
      }
      else{
        System.out.println("Invalid deposit amount")
      }
   }
   public void withdrawal(double amount){
    if(amount>0 && amount<=balance){
      balance-=amount;
      System.out.println("Withdrawn: "+amount);
    }else{
      System.out.println("Withdrawal failed: Insufficient balance.");

    }
   }
     public void displayBalance(){
        System.out.println("Current balance: "+balance);
     }
    }

    class SavingsAccount extends BankAccount{
      private static final double minBalance=100.0;
      public SavingsAccount(double initialBalance){
        super(initialBalance);

      }
      public void withdraw(double amount)
    }
public class BankSystem{
  public static void main(String [] args){
    Scanner sc=new Scanner(System.in);
    System.out.print("Enter choice 1 for bank account and choice 2 for savings account");
    int choice=nextInt();
    System.out.print("enter intial balance for savings account :");
    double savingsBalance=sc.nextDouble(); 
    SavingsAccount savingsaccount=new SavingsAccount(savingsBalance);

  
  }
}
*/





    










