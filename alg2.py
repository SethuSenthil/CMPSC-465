Algorithm medianTracker(array):
    maxHeap <- empty max heap (to store smaller elements)
    minHeap <- empty min heap (to store larger elements)

    # Procedure to add a number to the heaps and balance them
    Procedure addNumber(n):
        if maxHeap is empty:
            # If maxHeap is empty, add the first element
            insert n into maxHeap
        else if size(maxHeap) == size(minHeap):
            # If both heaps have the same size, choose where to insert based on the next number
            if n < minHeap.peek():
                # If the number is smaller than the smallest in minHeap, insert into maxHeap
                insert n into maxHeap
            else:
                # If the number is larger, insert into minHeap and balance by moving the smallest to maxHeap
                insert n into minHeap
                insert -minHeap.pop() into maxHeap
        else if size(maxHeap) > size(minHeap):
            # If maxHeap has more elements, choose where to insert based on the next number
            if n > -maxHeap.peek():
                # If the number is larger than the largest in maxHeap, insert into minHeap
                insert -n into minHeap
            else:
                # If the number is smaller, insert into maxHeap and balance by moving the largest to minHeap
                insert -n into maxHeap
                insert -maxHeap.pop() into minHeap

    # Procedure to calculate and return the current median
    Procedure getMedian():
        if maxHeap is empty:
            # If maxHeap is empty, return 0 as there is no median
            return 0
        else if size(maxHeap) == size(minHeap):
            # If both heaps have the same size, return the average of their tops as the median
            return (-maxHeap.peek() + minHeap.peek()) / 2.0
        else:
            # If maxHeap has more elements, return the top of maxHeap as the median
            return -maxHeap.peek()