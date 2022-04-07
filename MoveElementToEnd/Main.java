import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;

class Program {
	public static List<Integer> moveElementToEnd(List<Integer> array, int toMove) {
		int i = 0;
		int j = array.size() - 1;

		while(i < j) {
			while (i < j && array.get(j) == toMove) {
				j--;
			}

			if(array.get(i) == toMove) {
				int temp = array.get(j);
				array.set(j, array.get(i));
				array.set(i, temp);
			}

			i++;
		}

		return array;
	}
}

public class Main {
	public static void main(String[] args) {
		List<Integer> array = new ArrayList<Integer>(Arrays.asList(2, 1, 2, 2, 2, 3, 4, 2));
		int toMove = 2;
		List<Integer> result = Program.moveElementToEnd(array, toMove);

//		StringBuilder bldr = new StringBuilder();
		for(Integer i : result) {
			System.out.print(i + ", ");
		}
	}
}
