package com.jacektracz.java8.samples.concurrent;

import java.util.Arrays;
import java.util.List;
import java.util.concurrent.Callable;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;
import java.util.concurrent.ScheduledExecutorService;
import java.util.concurrent.ScheduledFuture;
import java.util.concurrent.TimeUnit;

/**
 * 
 */
public class JavaExecutorCallableDesignPattern {

    public static void main(String[] args) throws InterruptedException, ExecutionException {
        
    	
    }

    public static void executeCallableListOfMethodsInvokeAny() throws InterruptedException, ExecutionException {
    	
    	System.out.println("executeCallableListOfMethodsInvokeAny-start");
        ExecutorService executor = Executors.newWorkStealingPool();

        List<Callable<String>> callables = Arrays.asList(
                callable("task1-executed-in-method", 2),
                callable("task2-executed-in-method", 1),
                callable("task3-executed-in-method", 3));

        String result = executor.invokeAny(callables);
        System.out.println(result);

        executor.shutdown();
    }
    
    public static void executeCallableListOfMethodsInvokeAll() throws InterruptedException, ExecutionException {
    	System.out.println("executeCallableListOfMethodsInvokeAll-start");
        ExecutorService executor = Executors.newWorkStealingPool();

        List<Callable<String>> callables = Arrays.asList(
                callable("task1-executed-in-method", 2),
                callable("task2-executed-in-method", 1),
                callable("task3-executed-in-method", 3));

        List<Future<String>> resultList = executor.invokeAll(callables);

        resultList.stream().forEach(s-> printLnFuture(s));
        
        for (int i = 0; i < resultList.size(); i++) {
            Future<String> future = resultList.get(i);
            try {
            	String result = future.get();                
            } catch (InterruptedException | ExecutionException e) {
                e.printStackTrace();
            }
        }
        
        executor.shutdown();
    }
    
    public static void printLnString(String s) {
    	System.out.println(s);
    }    
    
    public static void printLnFuture(Future<?> resolvedFuture) {
    	try 
    	{
    		printLnString("FutureInfo-start");
    		System.out.println(resolvedFuture);
    		printLnString("FutureInfo-end");
    		printLnString("Futureresult-start");
    		System.out.println(resolvedFuture.get());
    		printLnString("Futureresult-end");
    	}catch(Exception ex){
    		ex.printStackTrace();
    	}
    }
    
    public static Callable<String> callable(String result, long sleepSeconds) {
        return () -> {
            TimeUnit.SECONDS.sleep(sleepSeconds);
            return result;
        };
    }

    public static void executeCallableGetString() throws InterruptedException {
    	System.out.println("executeCallableGetString-start");
        ExecutorService executor = Executors.newWorkStealingPool();

        List<Callable<String>> callables = Arrays.asList(
                () -> "task1-result",
                () -> "task2-result",
                () -> "task3-result");

        executor.invokeAll(callables)
                .stream()
                .map(future -> {
                    try {
                        return future.get();
                    }
                    catch (Exception e) {
                        throw new IllegalStateException(e);
                    }
                })
                .forEach(System.out::println);

        executor.shutdown();
    }

    public static void executeLambaRunnableDelayed() {
    	System.out.println("executeLambaRunnableDelayed-start");
        ScheduledExecutorService executor = Executors.newScheduledThreadPool(1);

        Runnable task = () -> {
            try {
                TimeUnit.SECONDS.sleep(2);
                System.out.println("Scheduling: " + System.nanoTime());
            }
            catch (InterruptedException e) {
                System.err.println("task interrupted");
            }
        };

        executor.scheduleWithFixedDelay(task, 0, 1, TimeUnit.SECONDS);
    }

    public static void executeLambaRunnableAtFixedRate() {
    	System.out.println("executeLambaRunnableAtFixedRate-start");
        ScheduledExecutorService executor = Executors.newScheduledThreadPool(1);
        Runnable task = () -> System.out.println("Scheduling: " + System.nanoTime());
        int initialDelay = 0;
        int period = 1;
        executor.scheduleAtFixedRate(task, initialDelay, period, TimeUnit.SECONDS);
    }

    public static void executeRunnableScheduledFuture() throws InterruptedException {
    	 System.out.println("executeRunnableScheduledFuture-start");
    	 
        ScheduledExecutorService executor = Executors.newScheduledThreadPool(1);

        Runnable task = () -> System.out.println("Scheduling: " + System.nanoTime());
        int delay = 3;
        ScheduledFuture<?> future = executor.schedule(task, delay, TimeUnit.SECONDS);

        TimeUnit.MILLISECONDS.sleep(1337);

        long remainingDelay = future.getDelay(TimeUnit.MILLISECONDS);
        System.out.printf("Remaining Delay: %sms\n", remainingDelay);
    }

}
