/*
 * Copyright 2005 JBoss Inc
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.jacektracz.java8.lambdasinaction.dsl;

import java.util.List;
import java.util.Map;
import java.util.function.Function;
import java.util.stream.Collector;

import com.jacektracz.java8.lambdasinaction.streams.grouping.Car;

import static com.jacektracz.java8.lambdasinaction.dsl.Grouping.GroupingBuilder.groupOn;
import static com.jacektracz.java8.lambdasinaction.streams.grouping.Car.carList;
import static java.util.stream.Collectors.groupingBy;

public class Grouping {

    enum CaloricLevel { DIET, NORMAL, FAT };

    public static void main(String ... args) {
        System.out.println("Dishes grouped by type and caloric level: " + groupDishedByTypeAndCaloricLevel2());
        System.out.println("Dishes grouped by type and caloric level: " + groupDishedByTypeAndCaloricLevel3());
    }

    private static CaloricLevel getCaloricLevel( Car dish ) {
        if (dish.getHorsePower() <= 400) return CaloricLevel.DIET;
        else if (dish.getHorsePower() <= 700) return CaloricLevel.NORMAL;
        else return CaloricLevel.FAT;
    }

    private static Map<Car.Type, Map<CaloricLevel, List<Car>>> groupDishedByTypeAndCaloricLevel2() {
        return carList.stream().collect(
                twoLevelGroupingBy(Car::getType, dish -> getCaloricLevel( dish ) )
                                    );
    }

    public static <A, B, T> Collector<T, ?, Map<A, Map<B, List<T>>>> twoLevelGroupingBy(Function<? super T, ? extends A> f1, Function<? super T, ? extends B> f2) {
        return groupingBy(f1, groupingBy(f2));
    }

    private static Map<Car.Type, Map<CaloricLevel, List<Car>>> groupDishedByTypeAndCaloricLevel3() {
        Collector<? super Car, ?, Map<Car.Type, Map<CaloricLevel, List<Car>>>> c = groupOn( ( Car dish ) -> getCaloricLevel( dish ) ).after( Car::getType ).get();
        return carList.stream().collect( c );
    }

    public static class GroupingBuilder<T, D, K> {
        private final Collector<? super T, ?, Map<K, D>> collector;

        public GroupingBuilder( Collector<? super T, ?, Map<K, D>> collector ) {
            this.collector = collector;
        }

        public Collector<? super T, ?, Map<K, D>> get() {
            return collector;
        }

        public <J> GroupingBuilder<T, Map<K, D>, J> after(Function<? super T, ? extends J> classifier) {
            return new GroupingBuilder<>( groupingBy( classifier, collector ) );
        }

        public static <T, D, K> GroupingBuilder<T, List<T>, K> groupOn(Function<? super T, ? extends K> classifier) {
            return new GroupingBuilder<>( groupingBy( classifier )  );
        }
    }
}
