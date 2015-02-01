package findgivensum;

public class Tree{
	Tree left;
	Tree right;
	int value;
	public Tree(int value){
		this.value = value;
	}
	public Tree(){}
	
	public void addTree(int newValue){
		if(newValue != this.value){
			Tree side;
			if(newValue < this.value){
				side = this.right;
			}
			else {
				side = this.left;
			}
			if(side == null){
				side = new Tree(newValue);
			}
			else{
				side.addTree(newValue);
			}
		}
	}
	
	public void addAll(int[] values){
		for(int i: values){
			this.addTree(i);
		}
	}
}