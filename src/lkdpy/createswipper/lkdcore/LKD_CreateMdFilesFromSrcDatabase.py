import sys
import os
import logging
import shutil
from LKD_CopyFilesMd import *
from LKD_CatItem import *

#  C:\lkd\servers\installed\python27\python C:\lkd\ht\apps_w2_risk\app\src\apps_w2_w2\src\lkdpy\start_cpy.py

class LKD_CreateMdFilesFromSrcDatabase:
        def __init__(self):                                
                self.m_initialized = 1

        def xx_dbg(self, tt):
                "" ""
                print (tt)

        def xx_print(self, tt):
                "" ""
                print (tt)       

        def get_item(self, id,title):
                dd = LKD_CatItem(id,title)
                return dd

        def get_generic_cats_items(self,dd):
                # return self.get_cats_espn("")
                # return self.get_cats_j8p("")
                # return self.get_cats_sbms("")
                # return self.get_cats_spring_pets("")
                # return self.get_cats_fineract("")
                # return self.get_cats_eureka_feign("")
                # return self.get_cats_jhreact("")
                # return self.get_cats_activemq("")
                # return self.get_cats_hibspring("")
                # return self.get_cats_blockchain_web("")
                # return self.get_cats_blockchain_corda("")
                # return self.get_cats_blockchain_python_pow("")
                # return self.get_cats_dl_keras("")
                # return self.get_cats_dl_neural("")
                return self.get_cats_rl_37("")

        def get_generic_root(self,dd):
                # return self.get_root_espn()
                # return self.get_root_j8p()
                # return self.get_root_sbms("")
                # return self.get_root_pets("")
                # return self.get_root_fineract("")
                # return self.get_root_eureka_feign("")
                # return self.get_root_jhreact("")
                # return self.get_root_activemq("")
                # return self.get_root_hibspring("")
                # return self.get_root_blockchain_web("")
                # return self.get_root_blockchain_corda("")
                # return self.get_root_blockchain_python_pow("")
                # return self.get_root_dl_keras("")
                # return self.get_root_dl_neural("")
                return self.get_root_rl_37("")


        def get_root_jhreact(self, dd):
                root_src = "C:/lkd/ht/apps_sb/app/src/"
                return root_src


        def get_cats_jhreact(self, psrc_path_project):
                cats = []
                # cats.append(self.get_item(5459,"java-8-jacektracz-tutorial"))
                cats.append(self.get_item(5532,"lkd-spring-boot-react-app"))
                return cats


        def create_cats_titles(self, psrc_path_project):
                cats = []                                
                cats.append(self.get_item(5343,"Abstract Document"))
                cats.append(self.get_item(5344,"Abstract Factory"))
                cats.append(self.get_item(5345,"Adapter"))
                cats.append(self.get_item(5346,"Aggregator Microservices"))
                cats.append(self.get_item(5347,"Api Gateway"))
                cats.append(self.get_item(5348,"Async Method Invocation"))
                cats.append(self.get_item(5349,"Balking"))
                cats.append(self.get_item(5350,"Bridge"))
                cats.append(self.get_item(5351,"Builder"))
                cats.append(self.get_item(5352,"Business Delegate"))
                cats.append(self.get_item(5353,"Caching"))
                cats.append(self.get_item(5354,"Callback"))
                cats.append(self.get_item(5355,"Chain"))
                cats.append(self.get_item(5356,"Command"))
                cats.append(self.get_item(5357,"Composite"))
                cats.append(self.get_item(5358,"Converter"))
                cats.append(self.get_item(5359,"Cqrs"))
                cats.append(self.get_item(5360,"Dao"))
                cats.append(self.get_item(5361,"Data Bus"))
                cats.append(self.get_item(5362,"Data Mapper"))
                cats.append(self.get_item(5363,"Data Transfer Object"))
                cats.append(self.get_item(5364,"Decorator"))
                cats.append(self.get_item(5365,"Delegation"))
                cats.append(self.get_item(5366,"Dependency Injection"))
                cats.append(self.get_item(5367,"Double Checked Locking"))
                cats.append(self.get_item(5368,"Double Dispatch"))
                cats.append(self.get_item(5369,"Eip Aggregator"))
                cats.append(self.get_item(5370,"Eip Splitter"))
                cats.append(self.get_item(5371,"Eip Wire Tap"))
                cats.append(self.get_item(5372,"Event Aggregator"))
                cats.append(self.get_item(5373,"Event Asynchronous"))
                cats.append(self.get_item(5374,"Event Driven Architecture"))
                cats.append(self.get_item(5375,"Event Queue"))
                cats.append(self.get_item(5376,"Event Sourcing"))
                cats.append(self.get_item(5377,"Execute Around"))
                cats.append(self.get_item(5378,"Extension Objects"))
                cats.append(self.get_item(5379,"Facade"))
                cats.append(self.get_item(5380,"Factory Kit"))
                cats.append(self.get_item(5381,"Factory Method"))
                cats.append(self.get_item(5382,"Feature Toggle"))
                cats.append(self.get_item(5383,"Fluentinterface"))
                cats.append(self.get_item(5384,"Flux"))
                cats.append(self.get_item(5385,"Flyweight"))
                cats.append(self.get_item(5386,"Front Controller"))
                cats.append(self.get_item(5387,"Guarded Suspension"))
                cats.append(self.get_item(5388,"Half Sync Half Async"))
                cats.append(self.get_item(5389,"Hexagonal"))
                cats.append(self.get_item(5390,"Intercepting Filter"))
                cats.append(self.get_item(5391,"Interpreter"))
                cats.append(self.get_item(5392,"Iterator"))
                cats.append(self.get_item(5393,"Layers"))
                cats.append(self.get_item(5394,"Lazy Loading"))
                cats.append(self.get_item(5395,"Marker"))
                cats.append(self.get_item(5396,"Mediator"))
                cats.append(self.get_item(5397,"Memento"))
                cats.append(self.get_item(5398,"Message Channel"))
                cats.append(self.get_item(5399,"Model View Controller"))
                cats.append(self.get_item(5400,"Model View Presenter"))
                cats.append(self.get_item(5401,"Module"))
                cats.append(self.get_item(5402,"Monad"))
                cats.append(self.get_item(5403,"Monostate"))
                cats.append(self.get_item(5404,"Multiton"))
                cats.append(self.get_item(5405,"Mute Idiom"))
                cats.append(self.get_item(5406,"Mutex"))
                cats.append(self.get_item(5407,"Naked Objects"))
                cats.append(self.get_item(5408,"Null Object"))
                cats.append(self.get_item(5409,"Object Mother"))
                cats.append(self.get_item(5410,"Object Pool"))
                cats.append(self.get_item(5411,"Observer"))
                cats.append(self.get_item(5412,"Page Object"))
                cats.append(self.get_item(5413,"Partial Response"))
                cats.append(self.get_item(5414,"Poison Pill"))
                cats.append(self.get_item(5415,"Private Class Data"))
                cats.append(self.get_item(5416,"Producer Consumer"))
                cats.append(self.get_item(5417,"Promise"))
                cats.append(self.get_item(5418,"Property"))
                cats.append(self.get_item(5419,"Prototype"))
                cats.append(self.get_item(5420,"Proxy"))
                cats.append(self.get_item(5421,"Publish Subscribe"))
                cats.append(self.get_item(5422,"Queue Load Leveling"))
                cats.append(self.get_item(5423,"Reactor"))
                cats.append(self.get_item(5424,"Reader Writer Lock"))
                cats.append(self.get_item(5425,"Repository"))
                cats.append(self.get_item(5426,"Resource Acquisition Is Initialization"))
                cats.append(self.get_item(5427,"Retry"))
                cats.append(self.get_item(5428,"Semaphore"))
                cats.append(self.get_item(5429,"Servant"))
                cats.append(self.get_item(5430,"Service Layer"))
                cats.append(self.get_item(5431,"Service Locator"))
                cats.append(self.get_item(5432,"Singleton"))
                cats.append(self.get_item(5433,"Specification"))
                cats.append(self.get_item(5434,"State"))
                cats.append(self.get_item(5435,"Step Builder"))
                cats.append(self.get_item(5436,"Strategy"))
                cats.append(self.get_item(5437,"Template Method"))
                cats.append(self.get_item(5438,"Thread Pool"))
                cats.append(self.get_item(5439,"Throttling"))
                cats.append(self.get_item(5440,"Tls"))
                cats.append(self.get_item(5441,"Tolerant Reader"))
                cats.append(self.get_item(5442,"Trampoline"))
                cats.append(self.get_item(5443,"Twin"))
                cats.append(self.get_item(5444,"Unit Of Work"))
                cats.append(self.get_item(5445,"Value Object"))
                cats.append(self.get_item(5446,"Visitor"))
                return cats


        def create_cats_path(self, psrc_path_project):
                cats = []
                cats.append(self.get_item(5343,"abstract-document"))
                cats.append(self.get_item(5344,"abstract-factory"))
                cats.append(self.get_item(5345,"adapter"))
                cats.append(self.get_item(5346,"aggregator-microservices"))
                cats.append(self.get_item(5347,"api-gateway"))
                cats.append(self.get_item(5348,"async-method-invocation"))
                cats.append(self.get_item(5349,"balking"))
                cats.append(self.get_item(5350,"bridge"))
                cats.append(self.get_item(5351,"builder"))
                cats.append(self.get_item(5352,"business-delegate"))
                cats.append(self.get_item(5353,"caching"))
                cats.append(self.get_item(5354,"callback"))
                cats.append(self.get_item(5355,"chain"))
                cats.append(self.get_item(5356,"command"))
                cats.append(self.get_item(5357,"composite"))
                cats.append(self.get_item(5358,"converter"))
                cats.append(self.get_item(5359,"cqrs"))
                cats.append(self.get_item(5360,"dao"))
                cats.append(self.get_item(5361,"data-bus"))
                cats.append(self.get_item(5362,"data-mapper"))
                cats.append(self.get_item(5363,"data-transfer-object"))
                cats.append(self.get_item(5364,"decorator"))
                cats.append(self.get_item(5365,"delegation"))
                cats.append(self.get_item(5366,"dependency-injection"))
                cats.append(self.get_item(5367,"double-checked-locking"))
                cats.append(self.get_item(5368,"double-dispatch"))
                cats.append(self.get_item(5369,"eip-aggregator"))
                cats.append(self.get_item(5370,"eip-splitter"))
                cats.append(self.get_item(5371,"eip-wire-tap"))
                cats.append(self.get_item(5372,"event-aggregator"))
                cats.append(self.get_item(5373,"event-asynchronous"))
                cats.append(self.get_item(5374,"event-driven-architecture"))
                cats.append(self.get_item(5375,"event-queue"))
                cats.append(self.get_item(5376,"event-sourcing"))
                cats.append(self.get_item(5377,"execute-around"))
                cats.append(self.get_item(5378,"extension-objects"))
                cats.append(self.get_item(5379,"facade"))
                cats.append(self.get_item(5380,"factory-kit"))
                cats.append(self.get_item(5381,"factory-method"))
                cats.append(self.get_item(5382,"feature-toggle"))
                cats.append(self.get_item(5383,"fluentinterface"))
                cats.append(self.get_item(5384,"flux"))
                cats.append(self.get_item(5385,"flyweight"))
                cats.append(self.get_item(5386,"front-controller"))
                cats.append(self.get_item(5387,"guarded-suspension"))
                cats.append(self.get_item(5388,"half-sync-half-async"))
                cats.append(self.get_item(5389,"hexagonal"))
                cats.append(self.get_item(5390,"intercepting-filter"))
                cats.append(self.get_item(5391,"interpreter"))
                cats.append(self.get_item(5392,"iterator"))
                cats.append(self.get_item(5393,"layers"))
                cats.append(self.get_item(5394,"lazy-loading"))
                cats.append(self.get_item(5395,"marker"))
                cats.append(self.get_item(5396,"mediator"))
                cats.append(self.get_item(5397,"memento"))
                cats.append(self.get_item(5398,"message-channel"))
                cats.append(self.get_item(5399,"model-view-controller"))
                cats.append(self.get_item(5400,"model-view-presenter"))
                cats.append(self.get_item(5401,"module"))
                cats.append(self.get_item(5402,"monad"))
                cats.append(self.get_item(5403,"monostate"))
                cats.append(self.get_item(5404,"multiton"))
                cats.append(self.get_item(5405,"mute-idiom"))
                cats.append(self.get_item(5406,"mutex"))
                cats.append(self.get_item(5407,"naked-objects"))
                cats.append(self.get_item(5408,"null-object"))
                cats.append(self.get_item(5409,"object-mother"))
                cats.append(self.get_item(5410,"object-pool"))
                cats.append(self.get_item(5411,"observer"))
                cats.append(self.get_item(5412,"page-object"))
                cats.append(self.get_item(5413,"partial-response"))
                cats.append(self.get_item(5414,"poison-pill"))
                cats.append(self.get_item(5415,"private-class-data"))
                cats.append(self.get_item(5416,"producer-consumer"))
                cats.append(self.get_item(5417,"promise"))
                cats.append(self.get_item(5418,"property"))
                cats.append(self.get_item(5419,"prototype"))
                cats.append(self.get_item(5420,"proxy"))
                cats.append(self.get_item(5421,"publish-subscribe"))
                cats.append(self.get_item(5422,"queue-load-leveling"))
                cats.append(self.get_item(5423,"reactor"))
                cats.append(self.get_item(5424,"reader-writer-lock"))
                cats.append(self.get_item(5425,"repository"))
                cats.append(self.get_item(5426,"resource-acquisition-is-initialization"))
                cats.append(self.get_item(5427,"retry"))
                cats.append(self.get_item(5428,"semaphore"))
                cats.append(self.get_item(5429,"servant"))
                cats.append(self.get_item(5430,"service-layer"))
                cats.append(self.get_item(5431,"service-locator"))
                cats.append(self.get_item(5432,"singleton"))
                cats.append(self.get_item(5433,"specification"))
                cats.append(self.get_item(5434,"state"))
                cats.append(self.get_item(5435,"step-builder"))
                cats.append(self.get_item(5436,"strategy"))
                cats.append(self.get_item(5437,"template-method"))
                cats.append(self.get_item(5438,"thread-pool"))
                cats.append(self.get_item(5439,"throttling"))
                cats.append(self.get_item(5440,"tls"))
                cats.append(self.get_item(5441,"tolerant-reader"))
                cats.append(self.get_item(5442,"trampoline"))
                cats.append(self.get_item(5443,"twin"))
                cats.append(self.get_item(5444,"unit-of-work"))
                cats.append(self.get_item(5445,"value-object"))
                cats.append(self.get_item(5446,"visitor"))
                return cats

        def get_root_espn(self):
                root_src = "C:/lkd/ht/apps_micro_resillent_sap/app/src/cloud-espm-cloud-native"
                return root_src

        def get_cats_espn(self, psrc_path_project):
                cats = []
                cats.append(self.get_item(5449,"benchmark"))
                cats.append(self.get_item(5450,"commons"))
                cats.append(self.get_item(5451,"customer-service"))
                cats.append(self.get_item(5452,"documentation"))
                cats.append(self.get_item(5453,"gateway"))
                cats.append(self.get_item(5454,"product-service"))
                cats.append(self.get_item(5455,"sale-service"))
                cats.append(self.get_item(5456,"tax-service"))
                cats.append(self.get_item(5457,"worker"))                
                return cats

        # C:\lkd\ht\apps_java8_in_action\app\src

        def get_cats_sbms(self, psrc_path_project):
                cats = []
                cats.append(self.get_item(5464,"catalog-service"))
                cats.append(self.get_item(5465,"config"))
                cats.append(self.get_item(5466,"config-server"))
                cats.append(self.get_item(5467,"hystrix-dashboard"))
                cats.append(self.get_item(5468,"inventory-service"))
                cats.append(self.get_item(5469,"master-project-files"))
                cats.append(self.get_item(5470,"oauth2-server"))
                cats.append(self.get_item(5471,"order-service"))
                cats.append(self.get_item(5472,"service-registry"))
                cats.append(self.get_item(5473,"shoppingcart-ui"))
                cats.append(self.get_item(5474,"zipkin-server"))
                return cats

        def get_cats_spring_pets(self, psrc_path_project):
                cats = []
                cats.append(self.get_item(5477,"cat-service"))
                cats.append(self.get_item(5478,"dog-service"))
                cats.append(self.get_item(5479,"pet-api"))
                cats.append(self.get_item(5480,"pet-config"))
                cats.append(self.get_item(5481,"pet-dashboard"))
                cats.append(self.get_item(5482,"pet-eureka"))
                cats.append(self.get_item(5483,"pet-food"))
                cats.append(self.get_item(5484,"pet_profiles config"))
                return cats

        def get_root_eureka_feign(self, dd):
                root_src = "C:/lkd/ht/apps_eurekafeign/app/src"
                return root_src

        def get_cats_eureka_feign(self, psrc_path_project):
                cats = []
                cats.append(self.get_item(5524,"jacektracz-feign-eureka"))
                return cats



        def get_root_activemq(self,dd):
                root_src = "C:/lkd/ht/apps_spring_activemq_examples/app/src/activemq-examples-2"
                return root_src

        def get_cats_activemq_test(self, psrc_path_project):
                cats = []

                cats.append(self.get_item(5545, "activemq-karaf"))
                return cats

        def get_cats_activemq(self, psrc_path_project):
                cats = []

                cats.append(self.get_item(5545, "activemq-all"))
                cats.append(self.get_item(5546, "activemq-amqp"))
                cats.append(self.get_item(5547, "activemq-blueprint"))
                cats.append(self.get_item(5548, "activemq-broker"))
                cats.append(self.get_item(5549, "activemq-camel"))
                cats.append(self.get_item(5550, "activemq-client"))
                cats.append(self.get_item(5551, "activemq-console"))
                cats.append(self.get_item(5552, "activemq-fileserver"))
                cats.append(self.get_item(5553, "activemq-http"))
                cats.append(self.get_item(5554, "activemq-itests-spring31"))
                cats.append(self.get_item(5555, "activemq-jaas"))
                cats.append(self.get_item(5556, "activemq-jdbc-store"))
                cats.append(self.get_item(5557, "activemq-jms-pool"))
                cats.append(self.get_item(5558, "activemq-kahadb-store"))
                cats.append(self.get_item(5559, "activemq-karaf"))
                cats.append(self.get_item(5560, "activemq-karaf-itest"))
                cats.append(self.get_item(5561, "activemq-leveldb-store"))
                cats.append(self.get_item(5562, "activemq-log4j-appender"))
                cats.append(self.get_item(5563, "activemq-mqtt"))
                cats.append(self.get_item(5564, "activemq-openwire-generator"))
                cats.append(self.get_item(5565, "activemq-openwire-legacy"))
                cats.append(self.get_item(5566, "activemq-osgi"))
                cats.append(self.get_item(5567, "activemq-partition"))
                cats.append(self.get_item(5568, "activemq-pool"))
                cats.append(self.get_item(5569, "activemq-ra"))
                cats.append(self.get_item(5570, "activemq-rar"))
                cats.append(self.get_item(5571, "activemq-run"))
                cats.append(self.get_item(5572, "activemq-runtime-config"))
                cats.append(self.get_item(5573, "activemq-shiro"))
                cats.append(self.get_item(5574, "activemq-spring"))
                cats.append(self.get_item(5575, "activemq-stomp"))
                cats.append(self.get_item(5576, "activemq-tooling"))
                cats.append(self.get_item(5577, "activemq-unit-tests"))
                cats.append(self.get_item(5578, "activemq-web"))
                cats.append(self.get_item(5579, "activemq-web-console"))
                cats.append(self.get_item(5580, "activemq-web-demo"))
                
                return cats

        def get_root_hibspring(self,dd):
                root_src = "C:/lkd/ht/apps_spring_hibernate_spring/app/src/Hibernate-SpringBoot"
                return root_src



        def get_cats_hibspring(self, psrc_path_project):
                acats = []

                #acats.append(self.get_item(5582,"springboot-hiberante-examples"))
                acats.append(self.get_item(5583,"hibernatespringbootassigneduuid"))
                acats.append(self.get_item(5584,"hibernatespringbootassignsequentialnumber"))
                acats.append(self.get_item(5585,"hibernatespringbootattributelazyloadingbasic"))
                acats.append(self.get_item(5586,"hibernatespringbootattributelazyloadingdefaultvalues"))
                acats.append(self.get_item(5587,"hibernatespringbootattributelazyloadingjacksonserialization"))
                acats.append(self.get_item(5588,"hibernatespringbootaudit"))
                acats.append(self.get_item(5589,"hibernatespringbootautogeneratortype"))
                acats.append(self.get_item(5590,"hibernatespringbootautouuid"))
                acats.append(self.get_item(5591,"hibernatespringbootavoidentityindtoviaconstructor"))
                acats.append(self.get_item(5592,"hibernatespringbootbatchdeletecascadedelete"))
                acats.append(self.get_item(5593,"hibernatespringbootbatchdeleteorphanremoval"))
                acats.append(self.get_item(5594,"hibernatespringbootbatchdeletesingleentity"))
                acats.append(self.get_item(5595,"hibernatespringbootbatchingandserial"))
                acats.append(self.get_item(5596,"hibernatespringbootbatchinsertorder"))
                acats.append(self.get_item(5597,"hibernatespringbootbatchinsertorderbatchpertransaction"))
                acats.append(self.get_item(5598,"hibernatespringbootbatchinsertscompletablefuture"))
                acats.append(self.get_item(5599,"hibernatespringbootbatchinsertscompletablefuturereturngivenlist"))
                acats.append(self.get_item(5600,"hibernatespringbootbatchinsertscompletablefuturereturnlist"))
                acats.append(self.get_item(5601,"hibernatespringbootbatchinsertsentitymanager"))
                acats.append(self.get_item(5602,"hibernatespringbootbatchinsertsentitymanagerbatchpertransaction"))
                acats.append(self.get_item(5603,"hibernatespringbootbatchinsertsentitymanagerviajpacontext"))
                acats.append(self.get_item(5604,"hibernatespringbootbatchinsertsjparepository"))
                acats.append(self.get_item(5605,"hibernatespringbootbatchinsertsspringstyle"))
                acats.append(self.get_item(5606,"hibernatespringbootbatchinsertsspringstylebatchpertransaction"))
                acats.append(self.get_item(5607,"hibernatespringbootbatchinsertsviasession"))
                acats.append(self.get_item(5608,"hibernatespringbootbatchinsertsviasessionpertransaction"))
                acats.append(self.get_item(5609,"hibernatespringbootbatchjsonfileforkjoin"))
                acats.append(self.get_item(5610,"hibernatespringbootbatchupdateorder"))
                acats.append(self.get_item(5611,"hibernatespringbootbatchupdateordersingleentity"))
                acats.append(self.get_item(5612,"hibernatespringbootbulkupdates"))
                acats.append(self.get_item(5613,"hibernatespringbootcalculatepropertyformula"))
                acats.append(self.get_item(5614,"hibernatespringbootcalculatepropertygenerated"))
                acats.append(self.get_item(5615,"hibernatespringbootcalculatepropertypostload"))
                acats.append(self.get_item(5616,"hibernatespringbootcallstoredprocedurejdbctemplate"))
                acats.append(self.get_item(5617,"hibernatespringbootcallstoredprocedurejdbctemplatebeanpropertyrowmapper"))
                acats.append(self.get_item(5618,"hibernatespringbootcallstoredprocedurenativecall"))
                acats.append(self.get_item(5619,"hibernatespringbootcallstoredprocedurereturnresultset"))
                acats.append(self.get_item(5620,"hibernatespringbootcallstoredprocedurereturnvalue"))
                acats.append(self.get_item(5621,"hibernatespringbootcascadechildremoval"))
                acats.append(self.get_item(5622,"hibernatespringbootchooseonlyoneassociation"))
                acats.append(self.get_item(5623,"hibernatespringbootcloneentity"))
                acats.append(self.get_item(5624,"hibernatespringbootcompositekeyembeddable"))
                acats.append(self.get_item(5625,"hibernatespringbootcompositekeyembeddablemaprel"))
                acats.append(self.get_item(5626,"hibernatespringbootcompositekeyidclass"))
                acats.append(self.get_item(5627,"hibernatespringbootcountsqlstatements"))
                acats.append(self.get_item(5628,"hibernatespringbootcustomsequencegenerator"))
                acats.append(self.get_item(5629,"hibernatespringbootdatabasetriggers"))
                acats.append(self.get_item(5630,"hibernatespringbootdatabaseview"))
                acats.append(self.get_item(5631,"hibernatespringbootdatabaseviewupdateinsertdelete"))
                acats.append(self.get_item(5632,"hibernatespringbootdatabaseviewwithcheckoption"))
                acats.append(self.get_item(5633,"hibernatespringbootdatasourcebuilderbonecpkickoff"))
                acats.append(self.get_item(5634,"hibernatespringbootdatasourcebuilderc3p0kickoff"))
                acats.append(self.get_item(5635,"hibernatespringbootdatasourcebuilderdbcp2kickoff"))
                acats.append(self.get_item(5636,"hibernatespringbootdatasourcebuilderhikaricpkickoff"))
                acats.append(self.get_item(5637,"hibernatespringbootdatasourcebuilderproghikaricpkickoff"))
                acats.append(self.get_item(5638,"hibernatespringbootdatasourcebuildertomcatkickoff"))
                acats.append(self.get_item(5639,"hibernatespringbootdatasourcebuilderviburdbcpkickoff"))
                acats.append(self.get_item(5640,"hibernatespringbootdatasourceproxy"))
                acats.append(self.get_item(5641,"hibernatespringbootdelayconnection"))
                acats.append(self.get_item(5642,"hibernatespringbootdenserankfunction"))
                acats.append(self.get_item(5643,"hibernatespringbootderivedcountanddelete"))
                acats.append(self.get_item(5644,"hibernatespringbootdirectfetching"))
                acats.append(self.get_item(5645,"hibernatespringbootdomainevents"))
                acats.append(self.get_item(5646,"hibernatespringbootdtoblazeentityview"))
                acats.append(self.get_item(5647,"hibernatespringbootdtoconstructor"))
                acats.append(self.get_item(5648,"hibernatespringbootdtoconstructorexpression"))
                acats.append(self.get_item(5649,"hibernatespringbootdtocustomresulttransformer"))
                acats.append(self.get_item(5650,"hibernatespringbootdtoelementcollection"))
                acats.append(self.get_item(5651,"hibernatespringbootdtoentityviaprojection"))
                acats.append(self.get_item(5652,"hibernatespringbootdtoentityviaprojectionnoassociation"))
                acats.append(self.get_item(5653,"hibernatespringbootdtorecordconstructor"))
                acats.append(self.get_item(5654,"hibernatespringbootdtorecordconstructorexpression"))
                acats.append(self.get_item(5655,"hibernatespringbootdtorecordjbctemplate"))
                acats.append(self.get_item(5656,"hibernatespringbootdtorecordresulttransformer"))
                acats.append(self.get_item(5657,"hibernatespringbootdtoresulttransformer"))
                acats.append(self.get_item(5658,"hibernatespringbootdtoresulttransformerjpql"))
                acats.append(self.get_item(5659,"hibernatespringbootdtospringprojectionannotatednamednativequery"))
                acats.append(self.get_item(5660,"hibernatespringbootdtospringprojectionannotatednamedquery"))
                acats.append(self.get_item(5661,"hibernatespringbootdtospringprojectionormxmlnamednativequery"))
                acats.append(self.get_item(5662,"hibernatespringbootdtospringprojectionormxmlnamedquery"))
                acats.append(self.get_item(5663,"hibernatespringbootdtospringprojectionpropertiesnamednativequery"))
                acats.append(self.get_item(5664,"hibernatespringbootdtospringprojectionpropertiesnamedquery"))
                acats.append(self.get_item(5665,"hibernatespringbootdtosqlresultsetmapping"))
                acats.append(self.get_item(5666,"hibernatespringbootdtosqlresultsetmappingandnamednativequery"))
                acats.append(self.get_item(5667,"hibernatespringbootdtosqlresultsetmappingandnamednativequery2"))
                acats.append(self.get_item(5668,"hibernatespringbootdtosqlresultsetmappingandnamednativequeryentity"))
                acats.append(self.get_item(5669,"hibernatespringbootdtosqlresultsetmappingandnamednativequeryentity2"))
                acats.append(self.get_item(5670,"hibernatespringbootdtosqlresultsetmappingnamednativequeryormxml"))
                acats.append(self.get_item(5671,"hibernatespringbootdtotupleandjpql"))
                acats.append(self.get_item(5672,"hibernatespringbootdtotupleandsql"))
                acats.append(self.get_item(5673,"hibernatespringbootdtounrelatedentities"))
                acats.append(self.get_item(5674,"hibernatespringbootdtoviaclassbasedprojections"))
                acats.append(self.get_item(5675,"hibernatespringbootdtoviacrossjoins"))
                acats.append(self.get_item(5676,"hibernatespringbootdtoviafulljoins"))
                acats.append(self.get_item(5677,"hibernatespringbootdtoviafulljoinsmysql"))
                acats.append(self.get_item(5678,"hibernatespringbootdtoviafullouterexcludingjoins"))
                acats.append(self.get_item(5679,"hibernatespringbootdtoviainnerjoins"))
                acats.append(self.get_item(5680,"hibernatespringbootdtovialeftexcludingjoins"))
                acats.append(self.get_item(5681,"hibernatespringbootdtovialeftjoins"))
                acats.append(self.get_item(5682,"hibernatespringbootdtoviaprojections"))
                acats.append(self.get_item(5683,"hibernatespringbootdtoviaprojectionsandjpql"))
                acats.append(self.get_item(5684,"hibernatespringbootdtoviaprojectionsandvirtualproperties"))
                acats.append(self.get_item(5685,"hibernatespringbootdtoviaprojectionsintefaceinrepo"))
                acats.append(self.get_item(5686,"hibernatespringbootdtoviarightexcludingjoins"))
                acats.append(self.get_item(5687,"hibernatespringbootdtoviarightjoins"))
                acats.append(self.get_item(5688,"hibernatespringbootdtoviasqlresultsetmappingem"))
                acats.append(self.get_item(5689,"hibernatespringbootdynamicprojection"))
                acats.append(self.get_item(5690,"hibernatespringbootdynamicprojectionclass"))
                acats.append(self.get_item(5691,"hibernatespringbootdynamicupdate"))
                acats.append(self.get_item(5692,"hibernatespringbootelementcollectionjoinfetch"))
                acats.append(self.get_item(5693,"hibernatespringbootelementcollectionnoordercolumn"))
                acats.append(self.get_item(5694,"hibernatespringbootelementcollectionwithordercolumn"))
                acats.append(self.get_item(5695,"hibernatespringbootenabledirtytracking"))
                acats.append(self.get_item(5696,"hibernatespringbootenablelazyloadnotrans"))
                acats.append(self.get_item(5697,"hibernatespringbootentitygraphattributepaths"))
                acats.append(self.get_item(5698,"hibernatespringbootentitylistener"))
                acats.append(self.get_item(5699,"hibernatespringbootenumattributeconverter"))
                acats.append(self.get_item(5700,"hibernatespringbootenumpostgresqlcustomtype"))
                acats.append(self.get_item(5701,"hibernatespringbootenumpostgresqlhibernatetypes"))
                acats.append(self.get_item(5702,"hibernatespringbootenumstringint"))
                acats.append(self.get_item(5703,"hibernatespringbootenvers"))
                acats.append(self.get_item(5704,"hibernatespringbootenversschemasql"))
                acats.append(self.get_item(5705,"hibernatespringbootexampleapi"))
                acats.append(self.get_item(5706,"hibernatespringbootfetchjoinandqueries"))
                acats.append(self.get_item(5707,"hibernatespringbootfilterassociation"))
                acats.append(self.get_item(5708,"hibernatespringbootfluentapiadditionalmethods"))
                acats.append(self.get_item(5709,"hibernatespringbootfluentapionsetters"))
                acats.append(self.get_item(5710,"hibernatespringbootflywaymysqldatabase"))
                acats.append(self.get_item(5711,"hibernatespringbootflywaymysqlprog"))
                acats.append(self.get_item(5712,"hibernatespringbootflywaymysqlquick"))
                acats.append(self.get_item(5713,"hibernatespringbootflywaymysqltwodatabases"))
                acats.append(self.get_item(5714,"hibernatespringbootflywaypostgresqlprog"))
                acats.append(self.get_item(5715,"hibernatespringbootflywaypostgresqlquick"))
                acats.append(self.get_item(5716,"hibernatespringbootflywaypostgresqlschema"))
                acats.append(self.get_item(5717,"hibernatespringbootflywaypostgresqltwoschemas"))
                acats.append(self.get_item(5718,"hibernatespringbootflywaytwovendors"))
                acats.append(self.get_item(5719,"hibernatespringboothhh000104"))
                acats.append(self.get_item(5720,"hibernatespringboothibernateslcehcachekickoff"))
                acats.append(self.get_item(5721,"hibernatespringboothikaricppropertieskickoff"))
                acats.append(self.get_item(5722,"hibernatespringboothilo"))
                acats.append(self.get_item(5723,"hibernatespringboothiloissue"))
                acats.append(self.get_item(5724,"hibernatespringboothintpassdistinctthrough"))
                acats.append(self.get_item(5725,"hibernatespringboothttplongconversationdetachedentity"))
                acats.append(self.get_item(5726,"hibernatespringbootimmutableentity"))
                acats.append(self.get_item(5727,"hibernatespringbootinlistpadding"))
                acats.append(self.get_item(5728,"hibernatespringbootinspectpersistentcontext"))
                acats.append(self.get_item(5729,"hibernatespringbootjacksonhibernate5module"))
                acats.append(self.get_item(5730,"hibernatespringbootjoindtoallfields"))
                acats.append(self.get_item(5731,"hibernatespringbootjoinedandstrategy"))
                acats.append(self.get_item(5732,"hibernatespringbootjoinedandvisitor"))
                acats.append(self.get_item(5733,"hibernatespringbootjoinfetch"))
                acats.append(self.get_item(5734,"hibernatespringbootjoinfetchpageable"))
                acats.append(self.get_item(5735,"hibernatespringbootjoinformula"))
                acats.append(self.get_item(5736,"hibernatespringbootjoinpagination"))
                acats.append(self.get_item(5737,"hibernatespringbootjointableinheritance"))
                acats.append(self.get_item(5738,"hibernatespringbootjointablerepositoryinheritance"))
                acats.append(self.get_item(5739,"hibernatespringbootjoinvsjoinfetch"))
                acats.append(self.get_item(5740,"hibernatespringbootjpacallbacks"))
                acats.append(self.get_item(5741,"hibernatespringbootjpqlfunction"))
                acats.append(self.get_item(5742,"hibernatespringbootjpqlfunctionsparams"))
                acats.append(self.get_item(5743,"hibernatespringbootjsontomysql"))
                acats.append(self.get_item(5744,"hibernatespringbootjsontopostgresql"))
                acats.append(self.get_item(5745,"hibernatespringbootjustmanytoone"))
                acats.append(self.get_item(5746,"hibernatespringbootkeysetpagination"))
                acats.append(self.get_item(5747,"hibernatespringbootkeysetpaginationnextpage"))
                acats.append(self.get_item(5748,"hibernatespringbootleftjoinfetch"))
                acats.append(self.get_item(5749,"hibernatespringbootlimitresultsizeviaquerycreator"))
                acats.append(self.get_item(5750,"hibernatespringbootlistdtooffsetpagination"))
                acats.append(self.get_item(5751,"hibernatespringbootlistdtooffsetpaginationwf"))
                acats.append(self.get_item(5752,"hibernatespringbootlistentityoffsetpaginationextracolumn"))
                acats.append(self.get_item(5753,"hibernatespringbootlistentityoffsetpaginationextracolumnwf"))
                acats.append(self.get_item(5754,"hibernatespringbootlistentityoffsetpaginationprojection"))
                acats.append(self.get_item(5755,"hibernatespringbootloadbatchassociation"))
                acats.append(self.get_item(5756,"hibernatespringbootloadmultipleids"))
                acats.append(self.get_item(5757,"hibernatespringbootloadmultipleidsspecification"))
                acats.append(self.get_item(5758,"hibernatespringbootlog4j2viewbindingparameters"))
                acats.append(self.get_item(5759,"hibernatespringbootlog4jdbcviewbindingparameters"))
                acats.append(self.get_item(5760,"hibernatespringbootlogbindingparametersmysql"))
                acats.append(self.get_item(5761,"hibernatespringbootlogslowqueries"))
                acats.append(self.get_item(5762,"hibernatespringbootlogslowqueries545"))
                acats.append(self.get_item(5763,"hibernatespringbootlogtraceviewbindingparameters"))
                acats.append(self.get_item(5764,"hibernatespringbootlombokequalsandhashcode"))
                acats.append(self.get_item(5765,"hibernatespringbootmanytomanybidirectional"))
                acats.append(self.get_item(5766,"hibernatespringbootmanytomanybidirectionallistvsset"))
                acats.append(self.get_item(5767,"hibernatespringbootmanytomanysetandorderby"))
                acats.append(self.get_item(5768,"hibernatespringbootmapbooleantoyesno"))
                acats.append(self.get_item(5769,"hibernatespringbootmappedsuperclass"))
                acats.append(self.get_item(5770,"hibernatespringbootmappedsuperclassrepository"))
                acats.append(self.get_item(5771,"hibernatespringbootmappinglobtobytestring"))
                acats.append(self.get_item(5772,"hibernatespringbootmappinglobtoclobandblob"))
                acats.append(self.get_item(5773,"hibernatespringbootmatchentitiestotablestwoschemas"))
                acats.append(self.get_item(5774,"hibernatespringbootmergecollections"))
                acats.append(self.get_item(5775,"hibernatespringbootmysqlskiplocked"))
                acats.append(self.get_item(5776,"hibernatespringbootnamedentitygraph"))
                acats.append(self.get_item(5777,"hibernatespringbootnamedentitygraphbasicattrs"))
                acats.append(self.get_item(5778,"hibernatespringbootnamedqueriesinormxml"))
                acats.append(self.get_item(5779,"hibernatespringbootnamedqueriesinpropertiesfile"))
                acats.append(self.get_item(5780,"hibernatespringbootnamedqueriesviaannotations"))
                acats.append(self.get_item(5781,"hibernatespringbootnamedsubgraph"))
                acats.append(self.get_item(5782,"hibernatespringbootnaturalid"))
                acats.append(self.get_item(5783,"hibernatespringbootnaturalidcache"))
                acats.append(self.get_item(5784,"hibernatespringbootnaturalidimpl"))
                acats.append(self.get_item(5785,"hibernatespringbootnestedvsvirtualprojection"))
                acats.append(self.get_item(5786,"hibernatespringbootntillefunction"))
                acats.append(self.get_item(5787,"hibernatespringbootoffsetpagination"))
                acats.append(self.get_item(5788,"hibernatespringbootonetomanybidirectional"))
                acats.append(self.get_item(5789,"hibernatespringbootonetomanyunidirectional"))
                acats.append(self.get_item(5790,"hibernatespringbootonetoonemapsid"))
                acats.append(self.get_item(5791,"hibernatespringbootoptimisticforceincrement"))
                acats.append(self.get_item(5792,"hibernatespringbootoptional"))
                acats.append(self.get_item(5793,"hibernatespringbootorderbyrandom"))
                acats.append(self.get_item(5794,"hibernatespringbootp6spy"))
                acats.append(self.get_item(5795,"hibernatespringbootpagedtooffsetpagination"))
                acats.append(self.get_item(5796,"hibernatespringbootpagedtooffsetpaginationwf"))
                acats.append(self.get_item(5797,"hibernatespringbootpageentityoffsetpaginationextracolumn"))
                acats.append(self.get_item(5798,"hibernatespringbootpageentityoffsetpaginationextracolumnwf"))
                acats.append(self.get_item(5799,"hibernatespringbootpageentityoffsetpaginationprojection"))
                acats.append(self.get_item(5800,"hibernatespringbootpaginationrownumber"))
                acats.append(self.get_item(5801,"hibernatespringbootparentchildseparatequeries"))
                acats.append(self.get_item(5802,"hibernatespringbootpesimisticforceincrement"))
                acats.append(self.get_item(5803,"hibernatespringbootpessimisticlocks"))
                acats.append(self.get_item(5804,"hibernatespringbootpessimisticlocksdelinsupd"))
                acats.append(self.get_item(5805,"hibernatespringbootpooled"))
                acats.append(self.get_item(5806,"hibernatespringbootpooledlo"))
                acats.append(self.get_item(5807,"hibernatespringbootpopulatingchildviaproxy"))
                acats.append(self.get_item(5808,"hibernatespringbootpostcommit"))
                acats.append(self.get_item(5809,"hibernatespringbootpostgressqlskiplocked"))
                acats.append(self.get_item(5810,"hibernatespringbootprojectionandcollections"))
                acats.append(self.get_item(5811,"hibernatespringbootpropertyexpressions"))
                acats.append(self.get_item(5812,"hibernatespringbootqueryfetching"))
                acats.append(self.get_item(5813,"hibernatespringbootqueryplancache"))
                acats.append(self.get_item(5814,"hibernatespringbootrankfunction"))
                acats.append(self.get_item(5815,"hibernatespringbootreadonlyqueries"))
                acats.append(self.get_item(5816,"hibernatespringbootredundantsave"))
                acats.append(self.get_item(5817,"hibernatespringbootreferencenaturalid"))
                acats.append(self.get_item(5818,"hibernatespringbootrepointercept"))
                acats.append(self.get_item(5819,"hibernatespringbootresultsetmap"))
                acats.append(self.get_item(5820,"hibernatespringbootretryversionedoptimisticlocking"))
                acats.append(self.get_item(5821,"hibernatespringbootretryversionedoptimisticlockingtt"))
                acats.append(self.get_item(5822,"hibernatespringbootretryversionlessoptimisticlocking"))
                acats.append(self.get_item(5823,"hibernatespringbootretryversionlessoptimisticlockingtt"))
                acats.append(self.get_item(5824,"hibernatespringbootreturngeneratedkeys"))
                acats.append(self.get_item(5825,"hibernatespringbootreuseprojection"))
                acats.append(self.get_item(5826,"hibernatespringbootsaveandmerge"))
                acats.append(self.get_item(5827,"hibernatespringbootschemageneration"))
                acats.append(self.get_item(5828,"hibernatespringbootschemasql"))
                acats.append(self.get_item(5829,"hibernatespringbootsearchviaspecifications"))
                acats.append(self.get_item(5830,"hibernatespringbootsessionrepeatablereads"))
                acats.append(self.get_item(5831,"hibernatespringbootsimulatenplus1"))
                acats.append(self.get_item(5832,"hibernatespringbootsimulateversionedoptimisticlocking"))
                acats.append(self.get_item(5833,"hibernatespringbootsimulateversionlessoptimisticlocking"))
                acats.append(self.get_item(5834,"hibernatespringbootsingletableinheritance"))
                acats.append(self.get_item(5835,"hibernatespringbootsingletablerepositoryinheritance"))
                acats.append(self.get_item(5836,"hibernatespringbootsliceallcriteriabuilder"))
                acats.append(self.get_item(5837,"hibernatespringbootsliceallcriteriabuilderandsort"))
                acats.append(self.get_item(5838,"hibernatespringbootsliceallcriteriabuildersimplejparepository"))
                acats.append(self.get_item(5839,"hibernatespringbootsliceallcriteriabuildersortandspecification"))
                acats.append(self.get_item(5840,"hibernatespringbootsliceallcriteriabuildersortandspecificationandqueryhints"))
                acats.append(self.get_item(5841,"hibernatespringbootsliceallsimplesql"))
                acats.append(self.get_item(5842,"hibernatespringbootsliceallviafetchall"))
                acats.append(self.get_item(5843,"hibernatespringbootsoftdeletes"))
                acats.append(self.get_item(5844,"hibernatespringbootsoftdeletesspringstyle"))
                acats.append(self.get_item(5845,"hibernatespringbootspecificationqueryfetchjoins"))
                acats.append(self.get_item(5846,"hibernatespringbootspecificsubclassfrominheritance"))
                acats.append(self.get_item(5847,"hibernatespringbootspringcacheehcachekickoff"))
                acats.append(self.get_item(5848,"hibernatespringbootstreamable"))
                acats.append(self.get_item(5849,"hibernatespringbootstreamandmysql"))
                acats.append(self.get_item(5850,"hibernatespringbootsubentities"))
                acats.append(self.get_item(5851,"hibernatespringbootsubqueryinwhere"))
                acats.append(self.get_item(5852,"hibernatespringbootsubselect"))
                acats.append(self.get_item(5853,"hibernatespringbootsuppresslazyinitinopensessioninview"))
                acats.append(self.get_item(5854,"hibernatespringboottableperclassinheritance"))
                acats.append(self.get_item(5855,"hibernatespringboottableperclassrepositoryinheritance"))
                acats.append(self.get_item(5856,"hibernatespringboottablesmetadata"))
                acats.append(self.get_item(5857,"hibernatespringboottimestampgeneration"))
                acats.append(self.get_item(5858,"hibernatespringboottopnrowspergroup"))
                acats.append(self.get_item(5859,"hibernatespringboottransactionalinrepository"))
                acats.append(self.get_item(5860,"hibernatespringboottransactionalreadonlymeaning"))
                acats.append(self.get_item(5861,"hibernatespringboottransactioncallback"))
                acats.append(self.get_item(5862,"hibernatespringboottransactionid"))
                acats.append(self.get_item(5863,"hibernatespringboottransactionpropagation"))
                acats.append(self.get_item(5864,"hibernatespringboottransactiontimeout"))
                acats.append(self.get_item(5865,"hibernatespringboottwodatasourcebuilderkickoff"))
                acats.append(self.get_item(5866,"hibernatespringbootunproxyaproxy"))
                acats.append(self.get_item(5867,"hibernatespringbootutctimezone"))
                acats.append(self.get_item(5868,"hibernatespringbootuuid2"))
                acats.append(self.get_item(5869,"hibernatespringbootversionedoptimisticlockinganddettachedentity"))
                acats.append(self.get_item(5870,"hibernatespringbootwhytransactionalisignored"))
                acats.append(self.get_item(5871,"hibernatespringbootwrappertypestreamable"))
                acats.append(self.get_item(5872,"hibernatespringbootyearmonth"))
                acats.append(self.get_item(5873,"javaee"))
                return acats;  

        def get_root_fineract(self,dd):
                root_src = "C:/lkd/ht/apps_fineract_apache/apa"
                return root_src

        def get_cats_fineract(self, psrc_path_project):
                cats = []

                cats.append(self.get_item(5487,"fineract-cn-accounting"))
                cats.append(self.get_item(5488,"fineract-cn-anubis"))
                cats.append(self.get_item(5489,"fineract-cn-api"))
                cats.append(self.get_item(5490,"fineract-cn-async"))
                cats.append(self.get_item(5491,"fineract-cn-cassandra"))
                cats.append(self.get_item(5492,"fineract-cn-cheques"))
                cats.append(self.get_item(5493,"fineract-cn-command"))
                cats.append(self.get_item(5494,"fineract-cn-crypto"))
                cats.append(self.get_item(5495,"fineract-cn-customer"))
                cats.append(self.get_item(5496,"fineract-cn-data-jpa"))
                cats.append(self.get_item(5497,"fineract-cn-default-setup"))
                cats.append(self.get_item(5498,"fineract-cn-demo-server"))
                cats.append(self.get_item(5499,"fineract-cn-deposit-account-management"))
                cats.append(self.get_item(5500,"fineract-cn-docker-compose"))
                cats.append(self.get_item(5501,"fineract-cn-fims-e2e"))
                cats.append(self.get_item(5502,"fineract-cn-fims-web-app"))
                cats.append(self.get_item(5503,"fineract-cn-group"))
                cats.append(self.get_item(5504,"fineract-cn-group-finance"))
                cats.append(self.get_item(5505,"fineract-cn-identity"))
                cats.append(self.get_item(5506,"fineract-cn-lang"))
                cats.append(self.get_item(5507,"fineract-cn-mariadb"))
                cats.append(self.get_item(5508,"fineract-cn-mobile"))
                cats.append(self.get_item(5509,"fineract-cn-notifications"))
                cats.append(self.get_item(5510,"fineract-cn-office"))
                cats.append(self.get_item(5511,"fineract-cn-payroll"))
                cats.append(self.get_item(5512,"fineract-cn-permitted-feign-client"))
                cats.append(self.get_item(5513,"fineract-cn-portfolio"))
                cats.append(self.get_item(5514,"fineract-cn-postgresql"))
                cats.append(self.get_item(5515,"fineract-cn-provisioner"))
                cats.append(self.get_item(5516,"fineract-cn-reporting"))
                cats.append(self.get_item(5517,"fineract-cn-rhythm"))
                cats.append(self.get_item(5518,"fineract-cn-service-starter"))
                cats.append(self.get_item(5519,"fineract-cn-stellar-bridge"))
                cats.append(self.get_item(5520,"fineract-cn-teller"))
                cats.append(self.get_item(5521,"fineract-cn-template"))
                cats.append(self.get_item(5522,"fineract-cn-test"))
                return cats

        def get_root_j8p(self):
                root_src = "C:/lkd/ht/apps_java8_in_action/app/src"
                root_src = "C:/lkd/ht/apps_jhipster_cassandra/app"                
                return root_src

        def get_cats_j8p(self, psrc_path_project):
                cats = []
                # cats.append(self.get_item(5459,"java-8-jacektracz-tutorial"))
                cats.append(self.get_item(5461,"jhipster-sample-app-cassandra"))
                return cats


        def get_root_sbms(self,dd):
                root_src = "C:/lkd/ht/apps_springmicroseries/app/src/spring-boot-microservices-series"
                return root_src

        def get_root_pets(self,dd):
                root_src = "C:/lkd/ht/apps_springcloudpet/app/src/jacektracz-cloud-spring-pet"
                return root_src


        def get_cats_blockchain_web(self, psrc_path_project):
                cats = []
                cats.append(self.get_item(6083,"blockchain-demo"))
                return cats

        def get_root_blockchain_web(self, dd):
                root_src = "C:/lkd/ht/apps_blockchain_demo/app/src"
                return root_src

        # 
        def get_cats_blockchain_corda(self, psrc_path_project):
                cats = []
                cats.append(self.get_item(6084,"corda"))
                return cats

        def get_root_blockchain_corda(self, dd):
                root_src = "C:/lkd/ht/apps_corda/app/src"
                return root_src


        def get_cats_blockchain_python_pow(self, psrc_path_project):
                cats = []
                cats.append(self.get_item(6085,"blockchain"))
                return cats

        def get_root_blockchain_python_pow(self, dd):
                root_src = "C:/lkd/ht/apps_blockchain_pythonpow/app/src"
                return root_src


        def get_cats_dl_keras(self, psrc_path_project):
                cats = []                
                cats.append(self.get_item(8177,	"Deep-Learning-Course"))
                cats.append(self.get_item(8178,	"Deep-Learning-in-Python"))
                cats.append(self.get_item(8179,	"Easy-Deep-Learning-With-Keras"))
                cats.append(self.get_item(8180,	"Image-Recognition"))
                cats.append(self.get_item(8181,	"Image-Recognition-2"))
                cats.append(self.get_item(8182,	"Keras-Examples"))
                return cats

        def get_root_dl_keras(self, dd):
                root_src = "C:/lkd/ht/apps_dl_keras_course/app/src"
                return root_src


        def get_root_dl_neural(self, dd):
                root_src = "C:/lkd/ht/apps_dl_keras_course/app/src"
                return root_src

        def get_cats_dl_neural(self, psrc_path_project):
                cats = []                
                cats.append(self.get_item(8267,	"neural-networks-and-deep-learning"))
                return cats


        def get_root_rl_37(self, dd):
                root_src = "C:/lkd/ht/apps_rl_move37/app/src/Reinforcement-Learning-Code-Examples"
                return root_src

       def get_cats_rl_37(self, psrc_path_project):
                cats = []
                cats.append(self.get_item(9470,"Actor-Critic-Example")
                cats.append(self.get_item(9471,"ARS-Examplears")
                cats.append(self.get_item(9472,"DQN-Example")
                cats.append(self.get_item(9473,"Dynamic-Programming-Example")
                cats.append(self.get_item(9474,"PPO-Example")
                cats.append(self.get_item(9475,"PQ-Example")
                cats.append(self.get_item(9476,"Q-Learning-Example")
                cats.append(self.get_item(9477,"Rainbow-DQN-Example")
                return cats