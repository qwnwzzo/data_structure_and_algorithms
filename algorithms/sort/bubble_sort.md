## Java Version
```Java
public class Solution {
    public void bubbleSort(int[] array){
        boolean isSorted = false;
        int lastUnsorted = array.length - 1;
        while(!isSorted){
            isSorted = true;
            for(int i = 0; i < lastUnsorted; i++){
                if(array[i] > array[i + 1]){
                    swap(array, i, i + 1);
                    isSorted = false;
                }
            }

            lastUnsorted--;
        }

    }

    private void swap(int[] array, int i, int j){
        int temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }

}
```

## Python Version
```Python
class Solution:
    def bubble_sort(self, array):
        isSorted = False
        lastUnsorted = len(array) - 1
        while not isSorted:
            isSorted = True
            for i in range(0, lastUnsorted):
                if array[i] > array[i + 1]:
                    array[i], array[i + 1] = array[i + 1], array[i]
                    isSorted = False
                    
            lastUnsorted -= 1
```