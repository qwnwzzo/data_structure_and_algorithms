## Java Version
```Java
public class Solution {
    public void quickSort(int[] array) {
        quickSort(array, 0, array.length - 1);
    }

    private void quickSort(int[] array, int left, int right){
        if(left >= right){
            return;
        }

        int pivot = array[left + (right - left) / 2];
        int index = partition(array, left, right, pivot);
        quickSort(array, left, index - 1);
        quickSort(array, index, right);
    }

    public int partition(int[] array, int left, int right, int pivot){
        while(left <= right){
            while(array[left] < pivot){
                left++;
            }

            while(array[right] > pivot){
                right--;
            }

            if(left <= right){
                swap(array, left, right);
                left++;
                right--;
            }
        }

        return left;
    }

    public void swap(int[] array, int i, int j){
        int temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }
}
```

## Python Version
```python
class Solution():
    def quick_sort(self, arr):
        self.quick_sort_helper(arr, 0, len(arr) - 1)

    def quick_sort_helper(self, arr, start, end):
        if start >= end:
            return

        pivot = arr[start + (end - start) / 2]
        index = self.partition(arr, start, end, pivot)

        self.quick_sort_helper(arr, start, index - 1)
        self.quick_sort_helper(arr, index, end)

    def partition(self, arr, start, end, pivot):
        while start <= end:
            while arr[start] < pivot:
                start += 1

            while arr[end] > pivot:
                end -= 1

            if start <= end:
                self.swap(arr, start, end)
                start += 1
                end -= 1

        return start

    def swap(self, arr, left, right):
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp
```