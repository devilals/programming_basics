class Node{
	int data;
	Node next;
	public Node ()
	{
		data = 0;
		next = null;
	}
}

public class LinkedList extends Node {
	Node Head;
	
//	public LinkedList()
//	{
//		
//	}
	public void deleteNode(int key)
	{
		System.out.println("deleteNode method :\n");
		Node temp = Head, prev = null;
		if(temp == null)
			return;
		if(temp.data == key)
		{
			Head = temp.next;
			return;
		}
		//prev = temp;
		while(temp.next !=null)
		{
			System.out.println(temp.data + " " + temp.next.data);
			if(temp.next.data == key)
			{
				temp.next = temp.next.next;
				return;
			}
			//prev = temp;
			temp = temp.next;

		}
		return;
	}
	public void addNode(int key)
	{
		Node new_node = new Node();
		new_node.next = Head;
		new_node.data = key;
		Head = new_node;
	}

	public void reverseList()
	{
		System.out.println("Reverse list called\n");
		if(Head == null)
			return;
		if(Head.next == null)
			return;
		Node current, prev, next;
		prev = null;
		current = next = Head;
		
		while(current != null)
		{
			next = current.next;
			current.next = prev;
			prev = current;

			current = next;
		}
		Head = prev;
	}
	public void printList()
	{
		System.out.println("current list is:\n");
		Node temp = Head;
		while(temp != null)
		{
			System.out.println(temp.data+" ");
			temp = temp.next;
		}
		
	}

	public static void main(String[] args)
	{
		LinkedList lList = new LinkedList();
		lList.addNode(1);
		lList.addNode(2);
		lList.addNode(3);
		lList.addNode(4);
		lList.addNode(5);
		lList.addNode(6);
	
		lList.printList();
		lList.deleteNode(4);
		lList.printList();
		
		lList.reverseList();
		lList.printList();

	}
}

