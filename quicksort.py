class QuickSort():
    def __init__(self, array):
        self.array = array

    def quicksort(self):
        self._quicksort_recursive(0, len(self.array)-1)
        
    def _partition(self, left_index, right_index):
        # pivot will always be the last element in the array
        pivot_index = right_index

        # define pointers
        # left pointer is pointing to the beginning of the array
        # right pointer is pointing one place before the pivot
        right_index = pivot_index - 1
    
        while True:
            # Step 1. Left pointer continously moves on cell to the right until
            # it reaches a value that is greater than or equal to the pivot, and then stops.
            while not (self.array[left_index] >= self.array[pivot_index]):
                left_index += 1

            # Step 2. Right pointer continously moves one cell to the left until it
            # reaches a value that is less than or equal to the pivot, and then stops.
            # The right pointer will also stop if it reaches the beginning of the array.
            while not (self.array[right_index] <= self.array[pivot_index]) and\
                not (right_index == 0):
                right_index -= 1

            # Step 3. Once the right pointer has stopped, we reach a crossroads.
            # If the  left pointer has reached (or  gone beyond) the right pointer, we move on to Step 4.
            if not (left_index >= right_index):
                # Still Step 3. Swap the valures that the left and right pointers are pointing to.
                self.array[left_index], self.array[right_index] = self.array[right_index], self.array[left_index]
                left_index += 1
                # Repeat Steps 1, 2, and 3 again.
            else:
                # Step 4. Finally, swap the pivot with the value that the left pointer is currently pointing to.
                self.array[left_index], self.array[pivot_index] = self.array[pivot_index], self.array[left_index]
                # return statement breaks the infinite loop
                return left_index

    def _quicksort_recursive(self, left_index, right_index):
        # Base case: the subarray has 0 or 1 elements
        if right_index - left_index <= 0:
            return

        # Partition the range of elements and grab the index of the pivot:
        pivot_index = self._partition(left_index, right_index)

        # Recursively call this quicksort method on whatever is to the left of the pivot
        self._quicksort_recursive(left_index, pivot_index - 1)

        # Recursively call this quicksort method on whatever is to the right of the pivot
        self._quicksort_recursive(pivot_index + 1, right_index)
