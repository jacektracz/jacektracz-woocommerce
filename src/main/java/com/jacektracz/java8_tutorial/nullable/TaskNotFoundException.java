package com.jacektracz.java8_tutorial.nullable;

public class TaskNotFoundException extends RuntimeException {
    public TaskNotFoundException(String id) {
        super("No task found for id: " + id);
    }
}
