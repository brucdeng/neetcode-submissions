class MedianFinder {
    int minLen;
    int maxLen;
    PriorityQueue<Integer> minHeap;
    PriorityQueue<Integer> maxHeap;
    public MedianFinder() {
        this.minLen = 0;
        this.maxLen = 0;
        this.minHeap = new PriorityQueue<>(); //larger nums
        this.maxHeap = new PriorityQueue<>((a,b) -> Integer.compare(b,a)); //smaller nums
    }
    
    public void addNum(int num) {
        if (this.minLen==this.maxLen) {
            if (this.minLen ==0 || num > this.minHeap.peek()) {
                this.minHeap.add(num);
                this.minLen++;
            } else {
                this.maxHeap.add(num);
                this.maxLen++;
            }
        } else if (this.minLen > this.maxLen) {
            if (num > this.minHeap.peek()) {
                this.minHeap.add(num);
                this.maxHeap.add(this.minHeap.poll());
                this.maxLen++;
            } else {
                this.maxHeap.add(num);
                this.maxLen++;
            }
        } else {
            if (num < this.maxHeap.peek()) {
                this.maxHeap.add(num);
                this.minHeap.add(this.maxHeap.poll());
                this.minLen++;
            } else {
                this.minHeap.add(num);
                this.minLen++;
            }
        }
    }
    
    public double findMedian() {
        if (this.minLen==this.maxLen) {
            return ((double) this.minHeap.peek() + (double) this.maxHeap.peek())/2;
        }
        return (this.minLen > this.maxLen) ? (double) this.minHeap.peek() : (double) this.maxHeap.peek();
    }
}
