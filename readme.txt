The "queue" structure is used in the question 2.
Step 1. Queue the total people by using the "for" loop.
Step 2. Check the queue is empty or not by isemptyq(). 
        By using the "while" loop, while the queue is not empty, start counting from 2nd people.
Step 3. Based on the feature of queue "FIFO", that means people who queue is in the front, by dequeue(),
        they skip and move at the end of the same queue for the next count by enqueue().
Step 4. Each counting starts counting from 2nd people with using each "for" loop. 
        If people count not equal to m, they move at the end of the same queue. 
        Otherwise, eliminating the person.
Step 5. At the end of each "for" loop, go back step 2 until all people are eliminated.