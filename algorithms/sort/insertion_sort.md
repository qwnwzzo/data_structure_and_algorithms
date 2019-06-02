## Java Version
```Java
class Solution{
    public void insertionSort(int[] array){
        for(int i = 1; i < array.length; i++){
            int currentValue = array[i];
            int position = i;
            while(position > 0 && array[position - 1] > currentValue){
                array[position] = array[position - 1];
                position--;
            }
            
            array[position] = currentValue;
        }
    }
}
```

## Python Version
```python
class Solution:
    def insertion_sort(self, array):
        for i in range(1, len(array)):
            current_value = array[i]
            position = i
            while position > 0 and array[position - 1] > current_value:
                array[position] = array[position - 1]
                position -= 1

            array[position] = current_value
```