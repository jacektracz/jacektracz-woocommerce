http://150.151.162.234:8080/source/xref/KGR_36_SP4/src/java/kgr-logsandstatus/kgr-logsandstatus-client/src/main/java/com/reuters/kgr/logsandstatus/client/NotificationConsumingSection.java

class Example {
35 *     private static Logger logger = LoggerFactory.getLogger(Example.class);
36 *     // this needs to be static since the calling methid ( main ) is static.
37 *     // When calling method is NOT static, it the code in call can acces all members,
38 *     // and even final local variables of caller method.
39 *     static int receiveCount = 0;
40 *
41 *     public static void main(String[] args) throws Exception {
42 *         logger.info(&quot;entering listening section&quot;);
43 *         // anonymous class #1 : the NotificationConsumingSection
44 *         new NotificationConsumingSection&lt;Object&gt;() {
45 *             &#064;Override
46 *             public Object call() throws Exception {
47 *
48 *                 logger.debug(&quot;entered listening section&quot;);
49 *
50 *                 logger.debug(&quot;setting up listener&quot;);
51 *                 startListening(
52 *                 // anonymous class #2 : the Notification Listener
53 *                         new Listener() {
54 *
55 *                             &#064;Override
56 *                             public void onNotification(TaskInfo taskInfo, Notification notif) {
57 *                                 // this is the code called when a notification is received
58 *                                 receiveCount++;
59 *                                 logger.debug(&quot;received notif {}  {} from ti {} &quot;, new Object[] { receiveCount, notif, taskInfo });
60 *                                 // all code here is triggered upon notifications reception
61 *                             }
62 *                         }, null,// task filter : null means any task
63 *                         null // notif kind filter : null means any notification class
64 *                 );
65 *                 logger.debug(&quot;listener is now ready &quot;);
66 *
67 *                 logger.debug(&quot;now do something else&quot;);
68 *                 // ... conceptually , this is the &quot;main&quot; of the listening code
69 *                 // ...
70 *                 // ... real work while listening
71 *                 // ...
72 *                 // ...
73 *
74 *                 logger.debug(&quot;exiting listening section&quot;);
75 *
76 *                 // no need to cancel listeners at exit of section, it is done by the NotificationConsumingSection class
77 *                 return null;// we return null as there is nothing interesting to return in this case.
78 *             }
79 *         };
80 *
81 *         logger.debug(&quot;exited listening section&quot;);
82 *
83 *     }
84 * }