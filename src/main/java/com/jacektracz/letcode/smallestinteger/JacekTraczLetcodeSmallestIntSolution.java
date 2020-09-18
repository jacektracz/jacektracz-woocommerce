package com.jacektracz.letcode.smallestinteger;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;



public class JacekTraczLetcodeSmallestIntSolution {

	
	public int solution2 (int[] params) {
		List<Integer> ints = new ArrayList<>();
		for(int aa : params){
			ints.add(aa);
		}
		
		List<Integer> intsSorted = ints.stream().sorted((Integer first, Integer second) -> first - second ).collect(Collectors.toList());		
		Integer outcome = findMatched(intsSorted);
		return outcome;
	}
	
	public int findMatched (List<Integer> intsSorted) {
		Integer previous = -1;
		int outcome = 0;
		for(Integer dd_int : intsSorted) {
			if(previous ==  -1) {
				previous = dd_int;
				continue;
			}
			if(dd_int - previous >1) {
				outcome = previous+1;
				break;
			}
			previous = dd_int;
		}
		return outcome;		
	}
	
	public int solution (int[] params) {
		
		List<Integer> ints = new ArrayList<>();
		for(int aa : params){
			ints.add(aa);
		}
		Collections.sort(ints, (Integer first, Integer second) -> first - second  );
		
		Integer previous = -1;
		int outcome = 0;
		for(Integer dd_int : ints) {
			if(previous ==  -1) {
				previous = dd_int;
				continue;
			}
			if(dd_int - previous >1) {
				outcome = previous+1;
				break;
			}
			previous = dd_int;
		}
		return outcome;
	}
	
}
