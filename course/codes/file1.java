
/* 
public class file1{
    
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
         if(age<=2){
          humanage=age*11;
         }else{
          humanage= 22+((age-2)*5);
         }
         return humanage;
      } 
    
      public static void main(String[] args) {
        // Creating an object of the class
        file1 dog = new file1();
        
        // Assigning values
        dog.name = "Buddy";
        dog.breed = "Golden Retriever";
        dog.age = 3;

        // Calling method to print details
        dog.writeoutput();
      }
  }

  */

 /* 
  class Main
{
 public static void main (String args[])
 {
int sample[] = new int[10];
int i;
for (i = 0; i <10; i = i + 1){
 sample[i] = i;
 
 System.out.println ("This is sample[" + i + "]: " + sample[i]);}
 }
}
  
  */

public class file1{
   public static void main(String args[]){
    int arr[]=new int[4];
    arr[0]=1;
    arr[1]=2;
    arr[2]=3;
    arr[3]=4;
    System.out.println(arr[0]);

   }
}








