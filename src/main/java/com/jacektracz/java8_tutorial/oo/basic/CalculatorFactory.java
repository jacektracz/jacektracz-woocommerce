package com.jacektracz.java8_tutorial.oo.basic;

public abstract class CalculatorFactory {

    public static Calculator getInstance() {
        return new BasicCalculator();
    }
}
