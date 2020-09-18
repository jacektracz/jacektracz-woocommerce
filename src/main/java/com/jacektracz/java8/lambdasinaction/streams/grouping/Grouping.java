package com.jacektracz.java8.lambdasinaction.streams.grouping;

import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.Stream;

import static com.jacektracz.java8.lambdasinaction.streams.grouping.Car.carTags;
import static com.jacektracz.java8.lambdasinaction.streams.grouping.Car.carList;
import static java.util.stream.Collectors.*;

public class Grouping {

    enum HorsePowerLevel { WEAK, NORMAL, STRONG };

    public static void main(String ... args) {
        executeExamples();
    }
    
    public static void executeExamples() {
	    System.out.println("Cars grouped by type: " + groupCarsByType());
	    System.out.println("Car names grouped by type: " + groupCarNamesByType());
	    //System.out.println("Car tags grouped by type: " + groupCarTagsByType());
	    System.out.println("HorsePower Cars grouped by type: " + groupHorsePowerCarsByType());
	    System.out.println("Cars grouped by HorsePower level: " + groupCarsByHorsePowerLevel());
	    System.out.println("Cars grouped by type and HorsePower level: " + groupCaredByTypeAndHorsePowerLevel());
	    System.out.println("Count Cars in groups: " + countCarsInGroups());
	    System.out.println("Most HorsePower Cars by type: " + mostHorsePowerCarsByType());
	    System.out.println("Most HorsePower Cars by type: " + mostHorsePowerCarsByTypeWithoutOprionals());
	    System.out.println("Sum HorsePower by type: " + sumCaloriesByType());
	    System.out.println("HorsePower levels by type: " + HorsePowerLevelsByType());
	
	}
    private static Map<Car.Type, List<Car>> groupCarsByType() {
        return carList.stream().collect(groupingBy(Car::getType));
    }

    private static Map<Car.Type, List<String>> groupCarNamesByType() {
        return carList.stream().collect(groupingBy(Car::getType, mapping(Car::getName, toList())));
    }

    private static Map<Car.Type, Set<Object>> groupCarTagsByType() {    	
        return null;//carList.stream().collect(groupingBy(Car::getType, Collectors.flatMapping(Car -> carTags.get( Car.getName() ).stream(), toSet())));        
    }

    private static Map<Car.Type, List<Car>> groupHorsePowerCarsByType() {
    	
    	return carList.stream().filter(Car -> Car.getHorsePower() > 500).collect(groupingBy(Car::getType));

    }

    private static Map<HorsePowerLevel, List<Car>> groupCarsByHorsePowerLevel() {
        return carList.stream().collect(
                groupingBy(Car -> {
                    if (Car.getHorsePower() <= 400) return HorsePowerLevel.WEAK;
                    else if (Car.getHorsePower() <= 700) return HorsePowerLevel.NORMAL;
                    else return HorsePowerLevel.STRONG;
                } ));
    }

    private static Map<Car.Type, Map<HorsePowerLevel, List<Car>>> groupCaredByTypeAndHorsePowerLevel() {
        return carList.stream().collect(
                groupingBy(Car::getType,
                        groupingBy((Car Car) -> {
                            if (Car.getHorsePower() <= 400) return HorsePowerLevel.WEAK;
                            else if (Car.getHorsePower() <= 700) return HorsePowerLevel.NORMAL;
                            else return HorsePowerLevel.STRONG;
                        } )
                )
        );
    }

    private static Map<Car.Type, Long> countCarsInGroups() {
        return carList.stream().collect(groupingBy(Car::getType, counting()));
    }

    private static Map<Car.Type, Optional<Car>> mostHorsePowerCarsByType() {
        return carList.stream().collect(
                groupingBy(Car::getType,
                        reducing((Car d1, Car d2) -> d1.getHorsePower() > d2.getHorsePower() ? d1 : d2)));
    }

    private static Map<Car.Type, Car> mostHorsePowerCarsByTypeWithoutOprionals() {
        return carList.stream().collect(
                groupingBy(Car::getType,
                        collectingAndThen(
                                reducing((d1, d2) -> d1.getHorsePower() > d2.getHorsePower() ? d1 : d2),
                                Optional::get)));
    }

    private static Map<Car.Type, Integer> sumCaloriesByType() {
        return carList.stream().collect(groupingBy(Car::getType,
                summingInt(Car::getHorsePower)));
    }

    private static Map<Car.Type, Set<HorsePowerLevel>> HorsePowerLevelsByType() {
        return carList.stream().collect(
                groupingBy(Car::getType, mapping(
                        Car -> { if (Car.getHorsePower() <= 400) return HorsePowerLevel.WEAK;
                        else if (Car.getHorsePower() <= 700) return HorsePowerLevel.NORMAL;
                        else return HorsePowerLevel.STRONG; },
                        toSet() )));
    }
    

    public static void flatMappingExample() {
    	/*
        List<Integer> list = Stream.of(List.of(1, 2, 3, 4), List.of(5, 6, 7, 8))
                                   .collect(
                                           Collectors.flatMapping(
                                                   l -> l.stream()
                                                         .filter(i -> i % 2 == 0),
                                                   Collectors.toList()
                                           )
                                   );
        System.out.println(list);
        */
        
    } 
   
}
