class MinStack
{
public:
    MinStack()
    {
    }

    void push(int val)
    {
        if (store.empty() || val <= min.top())
            min.push(val);

        store.push(val);
    }

    void pop()
    {
        if (store.top() == min.top())
            min.pop();
        store.pop();
    }

    int top()
    {
        return store.top();
    }

    int getMin()
    {
        return min.top();
    }

private:
    stack<int> store, min;
};
/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */
