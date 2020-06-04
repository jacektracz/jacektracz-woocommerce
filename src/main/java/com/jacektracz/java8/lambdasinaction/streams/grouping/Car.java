package com.jacektracz.java8.lambdasinaction.streams.grouping;

import java.util.*;

import static java.util.Arrays.asList;

public class Car {

    private final String name;
    private final boolean electric;
    private final int horsePower;
    private final Type type;

    public Car(String name, boolean vegetarian, int calories, Type type) {
        this.name = name;
        this.electric = vegetarian;
        this.horsePower = calories;
        this.type = type;
    }

    public String getName() {
        return name;
    }

    public boolean isElectric() {
        return electric;
    }

    public int getHorsePower() {
        return horsePower;
    }

    public Type getType() {
        return type;
    }

    public enum Type { COMBI, HATCHBACK, OTHER }

    @Override
    public String toString() {
        return name;
    }

    public static final List<Car> carList =
            asList( new Car("mercedes", false, 800, Car.Type.COMBI),
                    new Car("lexus", false, 700, Car.Type.COMBI),
                    new Car("tesla", true, 400, Car.Type.COMBI),
                    new Car("honda", true, 530, Car.Type.OTHER),
                    new Car("alfa romeo", true, 350, Car.Type.OTHER),
                    new Car("ferrari", true, 120, Car.Type.OTHER),
                    new Car("fiat", true, 550, Car.Type.OTHER),
                    new Car("lamborghini", false, 400, Car.Type.HATCHBACK),
                    new Car("bmw", false, 450, Car.Type.HATCHBACK));

    public static final Map<String, List<String>> carTags = new HashMap<>();

    static {
        carTags.put("mercedes", asList("prestige", "german"));
        carTags.put("lexus", asList("modern", "japan"));
        carTags.put("tesla", asList("sophisticated", "electric"));
        carTags.put("honda", asList("greasy", "fried"));
        carTags.put("lamborghini", asList("sportcar", "expensice"));
        carTags.put("bmw", asList("premium", "german"));
        
    }
}