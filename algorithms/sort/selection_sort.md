## Java Version
```Java
public class Solution {
    public void selectionSort(int[] array){
        for(int i = 0; i < array.length; i++){
            int minValue = array[i];
            int minIndex = i;
            for(int j = i + 1; j < array.length; j++){
                if(array[j] < minValue){
                    minValue = array[j];
                    minIndex = j;
                }
            }

            if(array[i] > array[minIndex]){
                swap(array, i, minIndex);
            }
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
    def selection_sort(self, array):
        for i in range(len(array)):
            min_value = array[i]
            min_index = i
            for j in range(i + 1, len(array)):
                if array[j] < min_value:
                    min_value = array[j]
                    min_index = j

            if array[i] > min_value:
                array[i], array[min_index] = array[min_index], array[i]
```