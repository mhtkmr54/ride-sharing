/*
 * Input Format = Taxis selected from Dual-Side Search. Schedule of Taxis inputted as 2-d array. Column = Taxi No., Row = Query No. 
 Output = Taxi Schedule. Works well for 1 taxi 1 query system because it is intialisation stage. All taxi schedules are initially zero.
 
 3 classes - Query, QueryElement and InsertFeasable
 */
package insertfeasable;
import java.util.*;
import java.io.*;
import java.util.logging.Level;
import java.util.logging.Logger;

public class InsertFeasable {
static int final_query_list[]; //make it global
static int no_of_queries=1;
static int i=0;
static QueryElement input_query_lists[][];//make it global
static int time[][] = new int[100][100];

/**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        System.out.println("Enter the new_query : Enter t_curr, Q_o, Q_d");
        Scanner s1 = new Scanner(System.in);//int no_of_queries=0;

        Scanner in=null;
    try {
        in = new Scanner(new FileReader("time.txt"));
    } catch (FileNotFoundException ex) {
        Logger.getLogger(InsertFeasable.class.getName()).log(Level.SEVERE, null, ex);
    }
        for(int r =0;r<100;r++){
            for(int w=0;w<100;w++)
            {if(in.hasNextInt())time[r][w]=in.nextInt();
            }
        }    
        int a=0,b=0,c=0;
        a = s1.nextInt();
        b = s1.nextInt();
        c = s1.nextInt();
            
        
        int pos_i=0; int pos_j=0; int Q_wp_l=6; int Q_wd_l=6;
        
        System.out.println("Enter the no. of taxis");
                
        
        final_query_list  = new int[10];
        for(int d=0;d<10;d++)
        
        {
            final_query_list[i]=0;
        }
        
        
        
        int taxi_location[] = new int[3];
        for(int d=0;d<3;d++)
        {
            taxi_location[d]=0; //not hard coded, only for initialisation
        }
        
        Query[] query_array = null;
        int taxis = s1.nextInt(); //input
        
        input_query_lists= new QueryElement[no_of_queries+1][taxis+1];
        
        for(int d=0;d<no_of_queries;d++)
        {
            for(int y=0;y<taxis;y++)
        
            {
                input_query_lists[d][y]=new QueryElement();
        
            }
        }
        
        
        
        
        
        
        for(i=0;i<taxis; i++)
        {
        
            try{
            taxi_location[i]=s1.nextInt(); //input taxi location
            }
        
            catch(Exception e){System.out.println(""+e.getStackTrace());}
            //System.out.println("Enter the no. of queries");
            System.out.println("Enter no. of queries for the taxi");
            no_of_queries = s1.nextInt();
            for(int j=0;j<no_of_queries;j++)
            {System.out.println("For each query enter t_curr, Q_o and Q_d");
                a = s1.nextInt();
                b = s1.nextInt();
                c = s1.nextInt();
            
                input_query_lists[j][i]=new QueryElement(a,b,c);
           /*input_query_lists[j][i].t_curr=1;
           
           input_query_lists[j][i].Q_o.x=1;
           input_query_lists[j][i].Q_o.y=1;
           
           input_query_lists[j][i].Q_d.x=1;
           input_query_lists[j][i].Q_d.y=1;*/
           
           //Is it feasible to insert this Q into query list?
           //Run for every (pos_i,pos_j) until one with 
           for(pos_j=1;pos_j<no_of_queries+1;pos_j++)
           {
               for(pos_i=0;pos_i<pos_j;pos_i++){
           System.out.println("In");
                   boolean res = feasabilityCheck(input_query_lists[j][i].t_curr, taxi_location[i], 
           
                           input_query_lists[j][i].Q_o,  input_query_lists[j][i].Q_d ,pos_i, pos_j, Q_wp_l, Q_wd_l);
           
                   if(res){System.out.println("Yes"+"Taxi No. = "+i);break;}
                   else{System.out.println("Not Inserted");}
           
           }
           }
           //if res==true add query
           //else remove query
         }
        }
        //things as input:
        // V.l[x,y], Q.o[x,y], Q.wp.l, Q.wd.l,
        
        for(int g=0;g<final_query_list.length;g++)
        {
            System.out.println(""+final_query_list[g]);
        }
        
    }
    
    static float calcDistance(int A, int B){return time[A][B];} //calcDistance used to find time between two locations from time.txt
    
    
    //algorithm for checking if query Q can be inserted in query list
    public static boolean feasabilityCheck(int t_curr, int taxi_location, 
            int Q_o,int Q_d,int pos_i, int pos_j, int Q_wp_l, int Q_wd_l)
    { 
        float a_p=0,a_d=0;
        float Q_wp_l_h=0, Q_wd_l_h=0;
        //int slack_time_pickup=Q_wp_l-a_p;
        //int slack_time_drop=Q_wd_l-a_d;
                
        Query insertQuery = new Query(Q_o,Q_d,Q_wp_l,Q_wd_l);
        
        int flag=0;
        //i=position for inserting Q_o
        //j=position for inserting Q_d
         //make it global
        if(t_curr+calcDistance(taxi_location,Q_o)>Q_wp_l)
        {//System.out.println("\n"+9);
        return false;
        }
        for(int h =pos_i +1;h<no_of_queries;h++)
        {
            a_p = calcDistance(taxi_location,input_query_lists[h][i].Q_o);
            a_d = calcDistance(taxi_location,input_query_lists[h][i].Q_d);
            Q_wp_l_h = calcDistance(final_query_list[0],input_query_lists[h][i].Q_o)+6;
            Q_wd_l_h = calcDistance(final_query_list[0],input_query_lists[h][i].Q_d)+6;
            
            if(Q_wp_l_h-a_p<0||Q_wd_l_h-a_d<0){flag=2;
            //System.out.println("\n"+2);
            return false;
            }
        }
            
            
        if(flag!=2){//add query Q_o to final_query_list
            for(int l= no_of_queries;l>pos_i;l--)
            {
                final_query_list[l]=final_query_list[l-1];
            }
            final_query_list[pos_i]=Q_o;
            //Also update all slack times
        
        }
        flag=0;
        
        if(t_curr+calcDistance(final_query_list[pos_j],Q_d)>Q_wd_l)
        {
            //System.out.println("\n"+3);
            return false;
        }
        
        for(int h =pos_j +1;h<no_of_queries;h++)
        {
            a_p = calcDistance(taxi_location,input_query_lists[h][i].Q_o);
            a_d = calcDistance(taxi_location,input_query_lists[h][i].Q_d);
            
            Q_wp_l_h = calcDistance(final_query_list[0],input_query_lists[h][i].Q_o)+6;
            Q_wd_l_h = calcDistance(final_query_list[0],input_query_lists[h][i].Q_d)+6;
            
            
            if(Q_wp_l_h-a_p<0||Q_wd_l_h-a_d<0)
            {
                flag=2;//System.out.println("\n"+4);
                return false;
            }
        }
        
        if(flag!=2)
        {
            for(int l= no_of_queries;l>pos_j;l--)
            {
                final_query_list[l]=final_query_list[l-1];
            }
            
            final_query_list[pos_j]=Q_d;
            //Also update all slack times
        
        
        }
        
        return true;
    }
}

class Query{

int Q_o;
int Q_d;
int Q_wp_l;
int Q_wd_l;

    public Query(int Q_o, int Q_d, int Q_wp_l, int Q_wd_l) {
        this.Q_o = Q_o;
        this.Q_d = Q_d;
        this.Q_wp_l = Q_wp_l;
        this.Q_wd_l = Q_wd_l;
    }
    
    int retQ_wp_l (){return Q_wp_l;}
    int retQ_wd_l (){return Q_wd_l;}



}

class QueryElement{
int t_curr;
int Q_o;
int Q_d;

    public QueryElement(int t_curr, int Q_o, int Q_d) {
        this.t_curr = t_curr;
        this.Q_o = Q_o;
        this.Q_d = Q_d;
    }

    public QueryElement() {
    }
 }
