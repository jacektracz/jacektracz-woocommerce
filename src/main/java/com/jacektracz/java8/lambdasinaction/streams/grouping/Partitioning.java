package com.jacektracz.java8.lambdasinaction.streams.grouping;

import java.util.*;

import static com.jacektracz.java8.lambdasinaction.streams.grouping.Car.carList;
import static java.util.Comparator.comparingInt;
import static java.util.stream.Collectors.*;

public class Partitioning {

    public static void main(String ... args) {
        System.out.println("Dishes partitioned by vegetarian: " + partitionByVegeterian());
        System.out.println("Vegetarian Dishes by type: " + vegetarianDishesByType());
        System.out.println("Most caloric dishes by vegetarian: " + mostCaloricPartitionedByVegetarian());
    }

    private static Map<Boolean, List<Car>> partitionByVegeterian() {
        return carList.stream().collect(partitioningBy(Car::isElectric));
    }

    private static Map<Boolean, Map<Car.Type, List<Car>>> vegetarianDishesByType() {
        return carList.stream().collect(partitioningBy(Car::isElectric, groupingBy(Car::getType)));
    }

    private static Object mostCaloricPartitionedByVegetarian() {
        return carList.stream().collect(
                partitioningBy(Car::isElectric,
                        collectingAndThen(
                                maxBy(comparingInt(Car::getHorsePower)),
                                Optional::get)));
    }
}

