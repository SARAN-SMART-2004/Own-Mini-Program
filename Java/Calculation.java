/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package calculation;
import java.util.*;
import java.lang.*;
/**
 *
 * @author CSE STUDENTS
 */
public class Calculation {

  
    public static void main(String[] args) {
       
        Scanner sc= new Scanner(System.in);    
        System.out.print("Enter the body temperature (in fahrenheit)  :");  
        float a= sc.nextFloat();  
        System.out.print("Enter the surface temperature of the room   :");  
        float b= sc.nextFloat();   
        System.out.print("How many hours after you see the body       :");  
        float c = sc.nextFloat();   
        System.out.print("Enter the body temperature after {} hours  ?");
        float d= sc.nextFloat(); 
         var CCC = (float)(a-b);//  C
        var CCCC=(float)((98.6-b)/CCC);//   UPP
        var CCCCC=(float)((d-b)/CCC);//       E
         var l1=(float)(c*(Math.log(CCCCC)));//L1
        var l2=(float)(Math.log(CCCC));//LL
        var l3=(float)(l2/l1);//            LLL
        var l4=(int)(-1*(l3));
         /**System.out.println("Total= " +CCC); 
        System.out.println("Total= " +CCCC); 
        System.out.println("Totl=" +CCCCC);
        System.out.println("Total= " +l1);
        System.out.println("Total= " +l2);
        System.out.println("Hours= " +l3);
  
     * @param args the command line arguments
    * */
         System.out.println("Hours= " +l4);
    
    }
}
