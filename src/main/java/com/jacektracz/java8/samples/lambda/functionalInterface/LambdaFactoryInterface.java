package com.jacektracz.java8.samples.lambda.functionalInterface;

import com.jacektracz.java8.samples.lambda.Person;

/**
 * 
 */
public class LambdaFactoryInterface {

    static class StringUtil {
        String startsWith(String s) {
            return String.valueOf(s.charAt(0));
        }
    }

    interface FactoryInterface<P extends Person> {
        P create(String firstName, String lastName);
    }

    public static void main(String[] args) {

        // constructor reference

        FactoryInterface<Person> personFactory = Person::new;
        Person person = personFactory.create("Peter", "Parker");
        System.out.println(person);   
    }
}
