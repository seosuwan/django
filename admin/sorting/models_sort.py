from dataclasses import dataclass


@dataclass
class Sorting(object):

    random_arr: []

    @property
    def random_arr(self) -> []: return self._random_arr
    @random_arr.setter
    def random_arr(self, random_arr): self._random_arr = random_arr

    def bubble_sort(self):
        arr = self.random_arr
        n = len(arr) # 배열길이를 뽑는다
        for i in range(n - 1): #
            for j in range(n - i - 1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr


    def merge_sort(self):
        pass

    @staticmethod
    def quick_sort(param : []):
        arr = param
        if len(arr) < 2:
            return arr
        pivot = len(arr) // 2
        arr1, arr2, arr3 = [], [], []
        for value in arr:
            if value < arr[pivot]:
                arr1.append(value)
            elif value > arr[pivot]:
                arr3.append(value)
            else:
                arr2.append(value)
        return Sorting.quick_sort(arr1) + Sorting.quick_sort(arr2) + Sorting.quick_sort(arr3)


