/*
Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:

void push(int x) Pushes element x to the top of the stack.
int pop() Removes the element on the top of the stack and returns it.
int top() Returns the element on the top of the stack.
boolean empty() Returns true if the stack is empty, false otherwise.
Notes:

You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.
 */

class MyStack {
        queue<int> q1;
        queue<int> q2;
        bool isOne;
public:
    MyStack(){
        q1 = queue<int>();
        q2 = queue<int>();
        isOne = true;
        
    }
    
    void push(int x) {
        if(isOne)
            q1.push(x);
        else 
            q2.push(x);
    }
    
    int pop() {
        if(isOne){
            isOne = false;
            moveElemsFrom(&q1, &q2);
            int x = q1.front();
            q1.pop();
            return x;
        }
        else {
            isOne = true;
            moveElemsFrom(&q2, &q1); 
            int x = q2.front();
            q2.pop();
            return x;
        }
        return 0;
        
    }
    
    int top() {
        if(isOne){
            isOne = false;

            moveElemsFrom(&q1, &q2);

            int x = q1.front();
            q2.push(q1.front());
            q1.pop();

            return x;
        }
        else {
            isOne = false;
            
            moveElemsFrom(&q2, &q1);

            int x = q2.front();
            q1.push(q2.front());
            q2.pop();\

            return x;
        }
        return 0;
    }
    
    bool empty() {
        return q1.empty() && q2.empty();
    }

    //helper function
    void moveElemsFrom(queue<int>* q1, queue<int>* q2){
        while(q1->size() > 1){
            q2->push(q1->front());
            q1->pop();
        }
    }
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack* obj = new MyStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * bool param_4 = obj->empty();
 */
