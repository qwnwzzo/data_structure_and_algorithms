## Java Version
```Java
public class Solution {
    public void quickSort(int[] array) {
        quickSort(array, 0, array.length - 1);
    }

    private void quickSort(int[] array, int lo, int hi){
        if(lo >= hi){
            return;
        }

        int j = partition(array, lo, hi);
        quickSort(array, lo, j - 1);
        quickSort(array, j + 1, hi);
    }

    public int partition(int[] array, int lo, int hi){
        int i = lo;
        int j = hi + 1;
        int pivot = array[lo];
        while(true){
            while(array[++i] < pivot){
                if(i == hi){
                    break;
                }
            }

            while(array[--j] > pivot){
                if(j == lo){
                    break;
                }
            }

            if(i >= j){
                break;
            }

            swap(array, i, j);

        }

        swap(array, lo, j);
        return j;
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

    def quick_sort_helper(self, arr, lo, hi):
        if lo >= hi:
            return

        j = self.partition(arr, lo, hi)
        self.quick_sort_helper(arr, lo, j - 1)
        self.quick_sort_helper(arr, j + 1, hi)

    def partition(self, arr, lo, hi):
        i = lo
        j = hi + 1
        pivot = arr[lo]

        while(True){
            i += 1
            while(arr[i] < pivot){
                if(i == hi){
                    break
                }
                i += 1
            }

            j -= 1
            while(arr[j] > pivot){
                if(j == lo){
                    break
                }
                j -= 1
            }

            if(i >= j){
                break
            }

            arr[i], arr[j] = arr[j], arr[i]
        }

        arr[lo], arr[j] = arr[j], arr[lo]
        return j
```