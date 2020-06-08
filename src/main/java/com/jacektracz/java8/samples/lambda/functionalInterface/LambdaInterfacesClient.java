package com.jacektracz.java8.samples.lambda.functionalInterface;

/**
 * 
 */
public class LambdaInterfacesClient {

    static int outerStaticNum;

    int outerNum;

    void testScopes() {
        int num = 1;

        LambdaConverter.TypeConverter<Integer, String> stringConverter =
                (from) -> String.valueOf(from + num);

        String convert = stringConverter.convert(2);
        System.out.println(convert);    // 3

        LambdaConverter.TypeConverter<Integer, String> stringConverter2 = (from) -> {
            outerNum = 13;
            return String.valueOf(from);
        };
        
        System.out.println(stringConverter2.convert(24));
        
        String[] array = new String[1];
        LambdaConverter.TypeConverter<Integer, String> stringConverter3 = (from) -> {
            array[0] = "Hi there";
            return String.valueOf(from);
        };

        stringConverter3.convert(23);

        System.out.println(array[0]);
    }

    public static void main(String[] args) {
        new LambdaInterfacesClient().testScopes();
    }

}