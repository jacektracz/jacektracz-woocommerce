package com.jacektracz.java8.samples.concurrent;

import java.util.concurrent.TimeUnit;

public class JavaRunnableThreadDesignPattern {

    public static void main(String[] args) {
    }
   
    public static void executeRunnableInThread() {
        Runnable runnable = () -> {
            try {
                System.out.println("Foo " + Thread.currentThread().getName());
                Thread.sleep(1000);
                System.out.println("Bar " + Thread.currentThread().getName());
            }
            catch (InterruptedException e) {
                e.printStackTrace();
            }
        };

        Thread thread = new Thread(runnable);
        thread.start();
    }

    public static void executeRunnableInRunnable() {
        Runnable runnable = () -> {
            String threadName = Thread.currentThread().getName();
            System.out.println("Hello " + threadName);
        };

        runnable.run();
        System.out.println("Done!");
        
    }
}
