import java.util.Scanner;

class sort {
    public static void main(String args[] {
        Scanner sc = new Scanner(System.in);

        String name = 'A';
        String nameList[100];
        int i=0;, count=0;
        FileWriter fw = new FileWriter("professors.txt", tue);

        while(name!=null) {
            name = sc.next();
            int count=0;
            for(int j=0; j<100; j++) {
                if(name==nameList[j] {
                    count++;
                }
            }
            if(count==0) {
               fw.write(name + "\n");
            }
        }
    }
}

