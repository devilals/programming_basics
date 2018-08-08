import java.util.Stack;

class Node {
	int data;
	Node next;
	public Node()
	{
		data = 0;
		next = null;
	}
}

public class QueueUsingStacks {

	Stack<Integer> stack1 = new Stack<Integer>();
	Stack<Integer> stack2 = new Stack<Integer>();
	
	public void enQueue(int key)
	{
		stack1.push(key);
	}
	
	public int deQueue()
	{
		int prev;
		if(stack1.empty())
		{
			System.out.println("empty Queue\n");
			return 0;
		}
		
		prev = stack1.pop();
		while(!stack1.empty())
		{
			stack2.push(prev);
			prev = stack1.pop();
		}
		
		while(!stack2.empty())
		{
			stack1.push(stack2.pop());
		}
		return prev;
	}

	public static void main(String[] args)
	{
		QueueUsingStacks q = new QueueUsingStacks();		
		q.enQueue(11);
		q.enQueue(2);
		q.enQueue(3);
		q.enQueue(4);
		
		System.out.println("deQueued :" + q.deQueue());
		System.out.println("deQueued :" + q.deQueue());
		System.out.println("deQueued :" + q.deQueue());
	}

}
