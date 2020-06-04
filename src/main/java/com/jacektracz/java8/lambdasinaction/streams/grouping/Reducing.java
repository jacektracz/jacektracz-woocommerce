package com.jacektracz.java8.lambdasinaction.streams.grouping;

import static com.jacektracz.java8.lambdasinaction.streams.grouping.Car.carList;
import static java.util.stream.Collectors.*;

public class Reducing {

    public static void main(String ... args) {
        System.out.println("Total calories in menu: " + calculateTotalCalories());
        System.out.println("Total calories in menu: " + calculateTotalCaloriesWithMethodReference());
        System.out.println("Total calories in menu: " + calculateTotalCaloriesWithoutCollectors());
        System.out.println("Total calories in menu: " + calculateTotalCaloriesUsingSum());
    }

    private static int calculateTotalCalories() {
        return carList.stream().collect(reducing(0, Car::getHorsePower, (Integer i, Integer j) -> i + j));
    }

    private static int calculateTotalCaloriesWithMethodReference() {
        return carList.stream().collect(reducing(0, Car::getHorsePower, Integer::sum));
    }

    private static int calculateTotalCaloriesWithoutCollectors() {
        return carList.stream().map(Car::getHorsePower).reduce(Integer::sum).get();
    }

    private static int calculateTotalCaloriesUsingSum() {
        return carList.stream().mapToInt(Car::getHorsePower).sum();
    }
}