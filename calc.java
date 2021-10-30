
import java.util.Scanner; 
class calc { 
     
    int a,b; 
    int add() 
    { 
        return a+b; 
    } 
 
    int sub() 
    { 
        return a-b; 
    } 
 
    int mul() 
    { 
        return a*b; 
    } 
 
    int divide() 
    {         if(b!=0)             return a/b;         else  
            return -1;  
    } 
 
    int rem() 
    {         if(b!=0)             return a%b; 
        else                 return -1;     } 
 
    public static void main(String args[]) { 
 
        calc c=new calc(); 
        Scanner sc =  new Scanner(System.in);         System.out.println("Enter two numbers: ");         c.a=sc.nextInt(); 
        c.b=sc.nextInt(); 
        int op; 
        while(true) 
        { 
            System.out.print("\n1.Add\n2.Subtract\n3.Multiply\n4.Divide\n5.Remainder\n6.Change the numbers\n7.Exit\nChoose any option: "); 
            op=sc.nextInt(); 
            switch(op) 
            { 
                case 1: System.out.println("A + B = "+c.add());                         break; 
                case 2: System.out.println("A - B = "+c.sub());                         break; 
                case 3: System.out.println("A * B = "+c.mul());                         break; 
                case 4: if(c.divide()!=-1) 
                            System.out.println("A / B = "+c.divide());                         else  
                            System.out.println("A / B not possible");                         break; 
                case 5: if(c.rem()!=-1) 
                            System.out.println("A % B = "+c.rem());                         else  
                            System.out.println("A % B not possible");                         break; 
                case 6: System.out.println("Enter the two numbers again: ");                         c.a=sc.nextInt(); 
                        c.b=sc.nextInt();                         break; 
                case 7: System.exit(0); 
                default: System.out.println("Enter correct option");                
            } 
        } 
    } 
} 
 
 
