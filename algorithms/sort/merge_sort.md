## Java Version
```Java
public class Solution {
    public void mergeSort(int[] array) {
        int[] temp = new int[array.length];
        mergeSort(array, 0, array.length - 1, temp);
    }

    private void mergeSort(int[] array, int start, int end, int[] temp){
        if(start >= end){
            return;
        }

        int mid = start + (end - start) / 2;
        mergeSort(array, start, mid, temp);
        mergeSort(array, mid + 1, end, temp);
        merge(array, start, mid, end, temp);
        
    }

    private void merge(int[] array, int start, int mid, int end, int[] temp){
        int left = start;
        int right = mid + 1;
        int index = start;

        while(left <= mid && right <= end){
            if(array[left] < array[right]){
                temp[index++] = array[left++];
            }else{
                temp[index++] = array[right++];
            }
        }

        while(left <= mid){
            temp[index++] = array[left++];
        }

        while(right <= end){
            temp[index++] = array[right++];
        }

        for(int i = start; i <= end; i++){
            array[i] = temp[i];
        }

    }
    
}
```

## Python Version
```python
class Solution:
    def mergeSort(self, array):
        temp = [None] * len(array)
        self.mergeSortHelper(array, 0, len(array) - 1, temp)

    def mergeSortHelper(self, array, start, end, temp):
        if start >= end:
            return

        mid = start + (end - start) / 2
        self.mergeSortHelper(array, start, mid, temp)
        self.mergeSortHelper(array, mid + 1, end, temp)
        self.merge(array, start, mid, end, temp)

    def merge(self, array, start, mid, end, temp):
        left = start
        right = mid + 1
        index = start
        while left <= mid and right <= end:
            if array[left] < array[right]:
                temp[index] = array[left]
                index += 1
                left += 1
            else:
                temp[index] = array[right]
                index += 1
                right += 1

        while left <= mid:
            temp[index] = array[left]
            index += 1
            left += 1

        while right <= end:
            temp[index] = array[right]
            index += 1
            right += 1

        for i in range(start, end + 1):
            array[i] = temp[i]
```