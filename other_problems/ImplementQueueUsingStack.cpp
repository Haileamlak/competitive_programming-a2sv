
class MyQueue
{
public:
    MyQueue()
    {
    }

    void push(int x)
    {
        store.push_back(x);
    }

    int pop()
    {
        int temp = store.front();
        store.pop_front();
        return temp;
    }

    int peek()
    {
        return store.front();
    }

    bool empty()
    {
        return store.empty();
    }

private:
    deque<int> store;
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */
