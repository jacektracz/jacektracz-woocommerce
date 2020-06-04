package com.jacektracz.java8.lambdasinaction.streams.grouping;

import java.util.*;
import java.util.function.*;

import static com.jacektracz.java8.lambdasinaction.streams.grouping.Car.carList;
import static java.util.stream.Collectors.*;

public class Summarizing {

    public static void main(String ... args) {
        System.out.println("Nr. of dishes: " + howManyDishes());
        System.out.println("The most caloric dish is: " + findMostCaloricDish());
        System.out.println("The most caloric dish is: " + findMostCaloricDishUsingComparator());
        System.out.println("Total calories in menu: " + calculateTotalCalories());
        System.out.println("Average calories in menu: " + calculateAverageCalories());
        System.out.println("Menu statistics: " + calculateMenuStatistics());
        System.out.println("Short menu: " + getShortMenu());
        System.out.println("Short menu comma separated: " + getShortMenuCommaSeparated());
    }


    private static long howManyDishes() {
        return carList.stream().collect(counting());
    }

    private static Car findMostCaloricDish() {
        return carList.stream().collect(reducing((d1, d2) -> d1.getHorsePower() > d2.getHorsePower() ? d1 : d2)).get();
    }

    private static Car findMostCaloricDishUsingComparator() {
        Comparator<Car> dishCaloriesComparator = Comparator.comparingInt(Car::getHorsePower);
        BinaryOperator<Car> moreCaloricOf = BinaryOperator.maxBy(dishCaloriesComparator);
        return carList.stream().collect(reducing(moreCaloricOf)).get();
    }

    private static int calculateTotalCalories() {
        return carList.stream().collect(summingInt(Car::getHorsePower));
    }

    private static Double calculateAverageCalories() {
        return carList.stream().collect(averagingInt(Car::getHorsePower));
    }

    private static IntSummaryStatistics calculateMenuStatistics() {
        return carList.stream().collect(summarizingInt(Car::getHorsePower));
    }

    private static String getShortMenu() {
        return carList.stream().map(Car::getName).collect(joining());
    }

    private static String getShortMenuCommaSeparated() {
        return carList.stream().map(Car::getName).collect(joining(", "));
    }
}
