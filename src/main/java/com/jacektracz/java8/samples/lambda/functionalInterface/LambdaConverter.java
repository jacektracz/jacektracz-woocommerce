package com.jacektracz.java8.samples.lambda.functionalInterface;

/**
 * 
 */
public class LambdaConverter {

    @FunctionalInterface
    public static interface TypeConverter<F, T> {
        T convert(F from);
    }

    static class StringUtil {
        String startsWith(String s) {
            return String.valueOf(s.charAt(0));
        }
    }

    public static void main(String[] args) {
        TypeConverter<String, Integer> integerConverter1 = (from) -> Integer.valueOf(from);
        Integer converted1 = integerConverter1.convert("123");
        System.out.println(converted1);   // result: 123


        // method reference

        TypeConverter<String, Integer> integerConverter2 = Integer::valueOf;
        Integer converted2 = integerConverter2.convert("123");
        System.out.println(converted2);   // result: 123


        StringUtil something = new StringUtil();

        TypeConverter<String, String> stringConverter = something::startsWith;
        String converted3 = stringConverter.convert("Java");
        System.out.println(converted3);    // result J

        // constructor reference

    }
}
