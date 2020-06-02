package com.jacektracz.java8.training.metreferences;

@FunctionalInterface
public interface TriFunction {

	public Employee create(int id,String orgName,double salary);
}
