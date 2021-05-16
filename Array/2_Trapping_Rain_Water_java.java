# https://leetcode.com/problems/trapping-rain-water

import java.util.*;

class Solution {
    public int trap(int[] arr) {
        // Integer[] arr = {4,2,0,3,2,5};
		
        // List<Integer> av =  new ArrayList<Integer>(Arrays.asList(arr));
		// Collections.reverse(av);
        // System.out.println(new ArrayList<Integer>(Arrays.asList(arr)));
        // List<Integer> av = Arrays.asList(arr);
        int[] travelled = new int[arr.length];
        int op = 0;
        op = test(arr, travelled); 
        
        
        
        reverse(travelled, travelled.length);
        reverse(arr, arr.length);
        
        op = op + test(arr, travelled); 
			// System.out.println(" ");

		//  System.out.println(" ");
		// for (int i = 0; i < travelled.length; i++) {
		// 	System.out.print(travelled[i]);
		// 	System.out.print(" ");
		// }
		// System.out.println(" ");
        // + test((Integer[]) av.toArray());
		// return waterCount;
        return op;
		
    }
    
    public void reverse(int a[], int n)
    {
        int i, k, t;
        for (i = 0; i < n / 2; i++) {
            t = a[i];
            a[i] = a[n - i - 1];
            a[n - i - 1] = t;
        }
  
        // /*printing the reversed array*/
        // System.out.println("Reversed array is: \n");
        // for (k = 0; k < n; k++) {
        //     System.out.println(a[k]);
        }
    
    public int test(int[] arr, int[] travelled){
        for (int i = 0; i < arr.length; i++) {
			System.out.print(arr[i]);
			System.out.print(" ");
		}
        Integer[] rightBig = new Integer[arr.length];
		// Integer[] leftBig = new Integer[arr.length];


		// List<Integer> opList =  new ArrayList<>();
		
		Stack<Integer> stk = new Stack<Integer>();
//		stk.push(arr[arr.length-1]);
//		rightBig[rightBig.length-1] = -1;
		
		for (int i = arr.length-1; i >= 0; i--) {
			
//			2,5,9,3,1,12,6,8,7
				while(true) {
					if (stk.size()==0) {
						stk.push(arr[i]);
						rightBig[i] = -1;
						break;
					}
					else if (arr[i] > stk.peek()) {
						stk.pop();
					}
					else if (arr[i] <= stk.peek()) {
						rightBig[i] = stk.peek();
						stk.push(arr[i]);
						break;
					}
				}
		}
		
// stk.clear();
// for (int i = 0; i < arr.length; i++) {
			
// //			2,5,9,3,1,12,6,8,7
// //			2
// //			-1
// 				while(true) {
// 					if (stk.size()==0) {
// 						stk.push(arr[i]);
// 						leftBig[i] = -1;
// 						break;
// 					}
// 					else if (arr[i] >= stk.peek()) {
// 						stk.pop();
// 					}
// 					else if (arr[i] < stk.peek()) {
// 						leftBig[i] = stk.peek();
// 						stk.push(arr[i]);
// 						break;
// 					}
// 				}
// 		}
			
// 		for (int i = 0; i < arr.length; i++) {
// 			System.out.print(arr[i]);
// 			System.out.print(" ");
// 		}
// 		System.out.println();
// 		for (int i = 0; i < rightBig.length; i++) {
// 			System.out.print(rightBig[i]);
// 			System.out.print(" ");
// 		}
// 		System.out.println();
// 		for (int i = 0; i < leftBig.length; i++) {
// 			System.out.print(leftBig[i]);
// 			System.out.print(" ");
// 		}
		
		
		
		
// 		System.out.println();
// 		System.out.println("total water");
		
		int waterCount = 0;
		int pos = 0;
		while(true) {
			if (pos == rightBig.length)
				break;
			
			// System.out.println(arr[pos] + " " + rightBig[pos] );

			
			if (rightBig[pos] != -1) {
				
				int nextBig = rightBig[pos];
				int current = arr[pos];
				
				// System.out.println(" current: "+current+" nextBig: "+nextBig);
				
				while(true) {
					pos++;
					if (nextBig == arr[pos])
						break;
                    if (travelled[pos] == 0 || travelled[pos]<( current - arr[pos])){
                        waterCount = waterCount + current - arr[pos] - travelled[pos];

                        travelled[pos] = current - arr[pos];
                    }
					
					
				}
			}
			else
				pos++;
				

//			pos++;
		}
		return waterCount;
    }
}
