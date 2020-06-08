package com.jacektracz.java8_tutorial.functionalInterfaces;

import java.util.UUID;
import java.util.function.Consumer;
import java.util.function.Function;
import java.util.function.Predicate;
import java.util.function.Supplier;

public class Example3_Functionalnterfaces {

    public static void main(String[] args) {

        Predicate<String> nameStartWithS = name -> name.startsWith("s");
        nameStartWithS.test("start 1");
        
        Consumer<String> sendEmail = message -> System.out.println("Sending email >> " + message);
        sendEmail.accept("Email Body");
        
        Function<String, Integer> stringToLength = name -> name.length();
        stringToLength.apply("Get Length");
        
        Supplier<String> uuidSupplier = () -> UUID.randomUUID().toString();
        uuidSupplier.get();
        
    }
}
