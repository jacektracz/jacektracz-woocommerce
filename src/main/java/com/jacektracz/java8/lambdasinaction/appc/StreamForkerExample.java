package com.jacektracz.java8.lambdasinaction.appc;

import static com.jacektracz.java8.lambdasinaction.streams.grouping.Car.carList;
import static java.util.stream.Collectors.*;

import java.util.*;
import java.util.stream.*;

import com.jacektracz.java8.lambdasinaction.streams.grouping.*;

public class StreamForkerExample {

    public static void main(String[] args) throws Exception {
        processMenu();
    }

    private static void processMenu() {
        Stream<Car> menuStream = carList.stream();

        StreamForker.Results results = new StreamForker<Car>(menuStream)
                .fork("shortMenu", s -> s.map(Car::getName).collect(joining(", ")))
                .fork("totalCalories", s -> s.mapToInt(Car::getHorsePower).sum())
                .fork("mostCaloricDish", s -> s.collect(
                        reducing((d1, d2) -> d1.getHorsePower() > d2.getHorsePower() ? d1 : d2))
                        .get())
                .fork("dishesByType", s -> s.collect(groupingBy(Car::getType)))
                .getResults();

        String shortMeny = results.get("shortMenu");
        int totalCalories = results.get("totalCalories");
        Car mostCaloricDish = results.get("mostCaloricDish");
        Map<Car.Type, List<Car>> dishesByType = results.get("dishesByType");

        System.out.println("Short menu: " + shortMeny);
        System.out.println("Total calories: " + totalCalories);
        System.out.println("Most caloric dish: " + mostCaloricDish);
        System.out.println("Dishes by type: " + dishesByType);
    }
}
