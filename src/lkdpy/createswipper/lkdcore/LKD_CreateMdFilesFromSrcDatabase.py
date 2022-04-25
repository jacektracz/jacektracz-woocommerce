import sys
import os
import logging
import shutil
from LKD_CopyFilesMd import *
from LKD_CatItem import *

#  C:\lkd\servers\installed\python27\python C:\lkd\ht\apps_w2_risk\app\src\apps_w2_w2\src\lkdpy\start_cpy.py
# C:\lkd\servers\installed\python27\python C:\lkd\ht\apps_w2_risk\app\src\apps_w2_w2\src\lkdpy\start_cpy.py perform-src-files
# select "cats.append(self.get_item(",id,",","\"",title,"\"","))" from joo2_categories where parent_id = 11178

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
                title = title.strip()
                title = title.replace(" ","-")
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
                # return self.get_cats_rl_37("")
                # return self.get_cats_pro_5("")
                # return self.get_cats_jpa2_ch3("")
                # return self.get_cats_jpa2_ch4("")
                # return self.get_cats_jpa2_ch5("")
                # return self.get_cats_jpa2_ch6("")
                # return self.get_cats_jpa2_ch7("")
                # return self.get_cats_jpa2_ch8("")
                # return self.get_cats_jpa2_ch9("")
                # return self.get_cats_spring_ecomm("")
                # return self.get_cats_java_algho_dt("")
                # return self.get_cats_java_algho_science("")
                # return self.get_cats_eugen("")
                #return self.get_cats_springboot_examples("")
                return self.get_cats_java_8_jacektracz_tutorial("")

# C:\lkd\servers\installed\python27\python C:\lkd\ht\apps_w2_risk\app\src\apps_w2_w2\src\lkdpy\start_cpy.py perform-src-files

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
                # return self.get_root_rl_37("")
                # return self.get_root_pro_5("")
                # return self.get_root_jpa2_ch3("")
                # return self.get_root_jpa2_ch4("")
                # return self.get_root_jpa2_ch5("")
                # return self.get_root_jpa2_ch6("")
                # return self.get_root_jpa2_ch7("")
                # return self.get_root_jpa2_ch8("")
                # return self.get_root_jpa2_ch9("")
                # return self.get_root_spring_ecomm("")
                # return self.get_root_java_algho_dt("")
                # return self.get_root_java_algho_science("")
                # return self.get_root_eugen("")
                # return self.get_root_etherneum_lkdg("")
                # return self.get_root_springboot_examples("")
                return self.get_root_java_8_jacektracz_tutorial("")


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
                cats.append(self.get_item(9470,"Actor-Critic-Example"))
                cats.append(self.get_item(9471,"ARS-Examplears"))
                cats.append(self.get_item(9472,"DQN-Example"))
                cats.append(self.get_item(9473,"Dynamic-Programming-Example"))
                cats.append(self.get_item(9474,"PPO-Example"))
                cats.append(self.get_item(9475,"PQ-Example"))
                cats.append(self.get_item(9476,"Q-Learning-Example"))
                cats.append(self.get_item(9477,"Rainbow-DQN-Example"))
                return cats

        def get_root_pro_5(self, dd):
                root_src = "C:/lkd/ht/apps_spring_pro/app/src/pro-spring-5"
                return root_src

        def get_cats_pro_5__(self, psrc_path_project):
                cats = []
                #cats.append(self.get_item(11121, "chapter02"))

                return cats

        def get_cats_pro_5(self, psrc_path_project):
                cats = []
                #cats.append(self.get_item(11121, "chapter02"))
                cats.append(self.get_item(11122, "chapter03"))
                cats.append(self.get_item(11123, "chapter04"))
                cats.append(self.get_item(11124, "chapter05"))
                cats.append(self.get_item(11125, "chapter05-aspectj-aspects"))
                cats.append(self.get_item(11126, "chapter06"))
                cats.append(self.get_item(11127, "chapter07"))
                cats.append(self.get_item(11128, "chapter08"))
                cats.append(self.get_item(11129, "chapter09"))
                cats.append(self.get_item(11130, "chapter10"))
                cats.append(self.get_item(11131, "chapter11"))
                cats.append(self.get_item(11132, "chapter12"))
                cats.append(self.get_item(11133, "chapter13"))
                cats.append(self.get_item(11134, "chapter14"))
                cats.append(self.get_item(11135, "chapter15"))
                cats.append(self.get_item(11136, "chapter16"))
                cats.append(self.get_item(11137, "chapter17"))                

                return cats

        def get_root_jpa2_ch4(self, dd):
                root_src = "C:/lkd/ht/apps_spring_pro_jpa_2/app/src/pro-jpa-2/examples/Chapter4"
                return root_src

        def get_cats_jpa2_ch4_test(self, psrc_path_project):
                cats = []
                cats.append(self.get_item(	11179	,	"01-fieldAccess	"	))
                return cats

        def get_cats_jpa2_ch4(self, psrc_path_project):
                cats = []
                #cats.append(self.get_item(	11179	,	"01-fieldAccess	"	))
                cats.append(self.get_item(	11180	,	"02-propertyAccess	"	))
                cats.append(self.get_item(	11181	,	"03-mixedAccess	"	))
                cats.append(self.get_item(	11182	,	"04-customTableSchema	"	))
                cats.append(self.get_item(	11183	,	"05-customColumnMapping	"	))
                cats.append(self.get_item(	11184	,	"06-lobMapping	"	))
                cats.append(self.get_item(	11185	,	"07-enumMapping	"	))
                cats.append(self.get_item(	11186	,	"08-temporalMapping	"	))
                cats.append(self.get_item(	11187	,	"09-transientMapping	"	))
                cats.append(self.get_item(	11188	,	"10-autoIdGeneration	"	))
                cats.append(self.get_item(	11189	,	"11-tableIdGeneration	"	))
                cats.append(self.get_item(	11190	,	"12-sequenceIdGeneration	"	))
                cats.append(self.get_item(	11191	,	"13-dbIdentityIdGeneration	"	))
                cats.append(self.get_item(	11192	,	"14-manyToOne	"	))
                cats.append(self.get_item(	11193	,	"15-joinColumn	"	))
                cats.append(self.get_item(	11194	,	"16-oneToOneUnidirectional	"	))
                cats.append(self.get_item(	11195	,	"17-oneToOneBidirectional	"	))
                cats.append(self.get_item(	11196	,	"18-oneToOnePkMapping	"	))
                cats.append(self.get_item(	11197	,	"19-oneToManyBidirectional	"	))
                cats.append(self.get_item(	11198	,	"20-oneToManyTargetEntity	"	))
                cats.append(self.get_item(	11199	,	"21-manyToManyBidirectional	"	))
                cats.append(self.get_item(	11200	,	"22-manyToManyJoinTable	"	))
                cats.append(self.get_item(	11201	,	"23-oneToManyUnidirectional	"	))
                cats.append(self.get_item(	11202	,	"24-oneToOneLazy	"	))
                cats.append(self.get_item(	11203	,	"25-embeddedObjects	"	))
                cats.append(self.get_item(	11204	,	"26-sharingEmbeddedObjects	"	))
                return cats

        def get_root_jpa2_ch5(self, dd):
                root_src = "C:/lkd/ht/apps_spring_pro_jpa_2/app/src/pro-jpa-2/examples/Chapter5"
                return root_src

        def get_cats_jpa2_ch5(self, psrc_path_project):
                cats = []                
                cats.append(self.get_item(	11206	,	"1-elementCollection	"	))
                cats.append(self.get_item(	11207	,	"10-embeddableKeyMapping	"	))
                cats.append(self.get_item(	11208	,	"11-manyToManyEmbeddableKeyOverride	"	))
                cats.append(self.get_item(	11209	,	"12-elementCollectionMapKeyEntity	"	))
                cats.append(self.get_item(	11210	,	"13-untypedMaps	"	))
                cats.append(self.get_item(	11211	,	"2-overrideCollectionTableColumn	"	))
                cats.append(self.get_item(	11212	,	"3-oneToManyList	"	))
                cats.append(self.get_item(	11213	,	"4-persistentlyOrderedList	"	))
                cats.append(self.get_item(	11214	,	"5-elementCollectionStringMap	"	))
                cats.append(self.get_item(	11215	,	"6-elementCollectionEnumMap	"	))
                cats.append(self.get_item(	11216	,	"7-oneToManyMap	"	))
                cats.append(self.get_item(	11217	,	"8-manyToManyMap	"	))
                cats.append(self.get_item(	11218	,	"9-oneToManyEntityAttributeKey	"	))
                return cats

        def get_root_jpa2_ch6(self, dd):
                root_src = "C:/lkd/ht/apps_spring_pro_jpa_2/app/src/pro-jpa-2/examples/Chapter6"
                return root_src

        def get_cats_jpa2_ch6(self, psrc_path_project):
                cats = []                

                cats.append(self.get_item(	11220	,	"01 txScopedEmExample	"	))
                cats.append(self.get_item(	11221	,	"02 extendedEmExample1	"	))
                cats.append(self.get_item(	11222	,	"03 extendedEmExample2	"	))
                cats.append(self.get_item(	11223	,	"04 extendedEmExample3	"	))
                cats.append(self.get_item(	11224	,	"05 applicationManagedSE	"	))
                cats.append(self.get_item(	11225	,	"06 applicationManagedEE	"	))
                cats.append(self.get_item(	11226	,	"07 txScopedPersistenceContext	"	))
                cats.append(self.get_item(	11227	,	"08 extendedPersistenceContext	"	))
                cats.append(self.get_item(	11228	,	"09 persistenceContextCollision	"	))
                cats.append(self.get_item(	11229	,	"10 persistenceContextInheritance	"	))
                cats.append(self.get_item(	11230	,	"11 applicationManagedJTA	"	))
                cats.append(self.get_item(	11231	,	"12 sharingApplicationManagedJTA	"	))
                cats.append(self.get_item(	11232	,	"13 resourceLocalTxSE	"	))
                cats.append(self.get_item(	11233	,	"14 resourceLocalTxEE	"	))
                cats.append(self.get_item(	11234	,	"15 persistingWithRelationships	"	))
                cats.append(self.get_item(	11235	,	"16 persistingWithRelationshipsUsingGetReference	"	))
                cats.append(self.get_item(	11236	,	"17 removingWithRelationships	"	))
                cats.append(self.get_item(	11237	,	"18 persistingWithRelationshipsCascade	"	))
                cats.append(self.get_item(	11238	,	"19 removingWithRelationshipsCascade	"	))
                cats.append(self.get_item(	11239	,	"20 mergingDetachedEntities	"	))
                cats.append(self.get_item(	11240	,	"21 detachmentWithTriggeredLazyLoading	"	))
                cats.append(self.get_item(	11241	,	"22 detachmentWithEagerLoading	"	))
                cats.append(self.get_item(	11242	,	"23 noDetachmentSingleTx	"	))
                cats.append(self.get_item(	11243	,	"24 noDetachmentAppManagedEm	"	))
                cats.append(self.get_item(	11244	,	"25 noDetachmentSFSBAndExtendedEm	"	))
                cats.append(self.get_item(	11245	,	"26 editSessionExample	"	))
                return cats

        def get_root_jpa2_ch7(self, dd):
                root_src = "C:/lkd/ht/apps_spring_pro_jpa_2/app/src/pro-jpa-2/examples/Chapter7"
                return root_src

        def get_cats_jpa2_ch7(self, psrc_path_project):
                cats = []                
                cats.append(self.get_item(	11247	,	"01 dynamicQueryExample	"	))
                cats.append(self.get_item(	11248	,	"02 namedQueryExample	"	))
                cats.append(self.get_item(	11249	,	"03 paramTypesExample	"	))
                cats.append(self.get_item(	11250	,	"04 executingQueriesExample	"	))
                cats.append(self.get_item(	11251	,	"05 queryResultsExample	"	))
                cats.append(self.get_item(	11252	,	"06 queryPagingExample	"	))
                cats.append(self.get_item(	11253	,	"07 messageBoardExample	"	))
                cats.append(self.get_item(	11254	,	"08 bulkQueryExample	"	))
                cats.append(self.get_item(	11255	,	"09 queryHintsExample	"	))
                return cats

        def get_root_jpa2_ch8(self, dd):
                root_src = "C:/lkd/ht/apps_spring_pro_jpa_2/app/src/pro-jpa-2/examples/Chapter8"
                return root_src

        def get_cats_jpa2_ch8(self, psrc_path_project):
                cats = []                
                cats.append(self.get_item(	11257	,	"jpqlExamples	"	))
                return cats

        def get_root_jpa2_ch9(self, dd):
                root_src = "C:/lkd/ht/apps_spring_pro_jpa_2/app/src/pro-jpa-2/examples/Chapter9"
                return root_src

        def get_cats_jpa2_ch9(self, psrc_path_project):
                cats = []                
                cats.append(self.get_item(	11259	,	"01 employeeSearchService	"	))
                cats.append(self.get_item(	11260	,	"02 predicateConjunction	"	))
                cats.append(self.get_item(	11261	,	"03 empSearchSubQuery	"	))
                cats.append(self.get_item(	11262	,	"04 metamodelStronglyTyped	"	))
                cats.append(self.get_item(	11263	,	"05 canonicalMetamodel	"	))
                return cats

        def get_root_jpa2_ch3(self, dd):
                root_src = "C:/lkd/ht/apps_spring_pro_jpa_2/app/src/pro-jpa-2/examples/Chapter3"
                return root_src

        def get_cats_jpa2_ch3(self, psrc_path_project):
                cats = []                
                cats.append(self.get_item(	11162	,	"01 slsbExample	"	))
                cats.append(self.get_item(	11163	,	"02 slsbLifecycleExample	"	))
                cats.append(self.get_item(	11164	,	"03 slsbRemoteExample	"	))
                cats.append(self.get_item(	11165	,	"04 sfsbExample	"	))
                cats.append(self.get_item(	11166	,	"05 sfsbLifecycleExample	"	))
                cats.append(self.get_item(	11167	,	"06 singletonBean	"	))
                cats.append(self.get_item(	11168	,	"07 mdbExample	"	))
                cats.append(self.get_item(	11169	,	"08 servletExample	"	))
                cats.append(self.get_item(	11170	,	"09 dependencyLookup	"	))
                cats.append(self.get_item(	11171	,	"10 ejbContextLookup	"	))
                cats.append(self.get_item(	11172	,	"11 fieldInjection	"	))
                cats.append(self.get_item(	11173	,	"12 setterInjection	"	))
                cats.append(self.get_item(	11174	,	"13 bmtExample	"	))
                cats.append(self.get_item(	11175	,	"14 cmtExample	"	))
                cats.append(self.get_item(	11176	,	"15 userTxExample	"	))
                cats.append(self.get_item(	11177	,	"16 employeeService	"	))
                return cats

        # select "cats.append(self.get_item(",id,",","\"",title,"\"","))" from joo2_categories where parent_id = 11178

        def get_root_spring_ecomm(self, dd):
                root_src = "C:/lkd/ht/apps_spring_micr_practical/app/src/practical-microservices-architectural-patterns/Christudas_Ch18_Source/ch18/ch18-01/Ax2-Ecom-With-Security"
                return root_src

# C:\lkd\ht\apps_spring_micr_practical\app\src\practical-microservices-architectural-patterns\Christudas_Ch18_Source\ch18\ch18-01\Ax2-Ecom-With-Security
        def get_cats_spring_ecomm(self, psrc_path_project):
                cats = []                
                cats.append(self.get_item(	11749	,"Ecom-cart"	))
                cats.append(self.get_item(	11750	,"Ecom-common"	))
                cats.append(self.get_item(	11751	,"Ecom-config"	))
                cats.append(self.get_item(	11752	,"Ecom-core"	))
                cats.append(self.get_item(	11753	,"Ecom-delivery"	))
                cats.append(self.get_item(	11754	,"Ecom-gateway"	))
                cats.append(self.get_item(	11755	,"Ecom-history"	))
                cats.append(self.get_item(	11756	,"Ecom-product"	))
                cats.append(self.get_item(	11757	,"Ecom-registry"	))
                cats.append(self.get_item(	11758	,"Ecom-security"	))
                cats.append(self.get_item(	11759	,"Ecom-shipping"	))
                cats.append(self.get_item(	11760	,"Ecom-user"	))
                cats.append(self.get_item(	11761	,"Ecom-web"	))        
                return cats


        def get_root_java_algho_dt(self, dd):
                root_src = "C:/lkd/ht/apps_spring_algorithms/app/src/Algorithms-1/src/main/java/com/williamfiset/algorithms/datastructures"
                return root_src

        def get_cats_java_algho_dt(self, psrc_path_project):
                cats = []                
                cats.append(self.get_item(	11771	,	"balancedtree"	))
                cats.append(self.get_item(	11772	,	"binarysearchtree"	))
                cats.append(self.get_item(	11773	,	"bloomfilter"	))
                cats.append(self.get_item(	11774	,	"dynamicarray"	))
                cats.append(self.get_item(	11775	,	"fenwicktree"	))
                cats.append(self.get_item(	11776	,	"fibonacciheap"	))
                cats.append(self.get_item(	11777	,	"hashtable"	))
                cats.append(self.get_item(	11778	,	"linkedlist"	))
                cats.append(self.get_item(	11779	,	"priorityqueue"	))
                cats.append(self.get_item(	11780	,	"quadtree"	))
                cats.append(self.get_item(	11781	,	"queue"	))
                cats.append(self.get_item(	11782	,	"segmenttree"	))
                cats.append(self.get_item(	11783	,	"set"	))
                cats.append(self.get_item(	11784	,	"skiplist"	))
                cats.append(self.get_item(	11785	,	"sparsetable"	))
                cats.append(self.get_item(	11786	,	"stack"	))
                cats.append(self.get_item(	11787	,	"suffixarray"	))
                cats.append(self.get_item(	11788	,	"trie"	))
                cats.append(self.get_item(	11789	,	"unionfind"	))
                cats.append(self.get_item(	11790	,	"utils"	))
                return cats

        def get_root_java_algho_science(self, dd):
                root_src = "C:/lkd/ht/apps_spring_algorithms/app/src/Algorithms-1/src/main/java/com/williamfiset/algorithms"
                return root_src

        def get_cats_java_algho_science(self, psrc_path_project):
                cats = []                
                cats.append(self.get_item(	11792	,	"ai"	))
                cats.append(self.get_item(	11793	,	"dp"	))
                cats.append(self.get_item(	11794	,	"geometry"	))
                cats.append(self.get_item(	11795	,	"graphtheory"	))
                cats.append(self.get_item(	11796	,	"linearalgebra"	))
                cats.append(self.get_item(	11797	,	"math"	))
                cats.append(self.get_item(	11798	,	"other"	))
                cats.append(self.get_item(	11799	,	"search"	))
                cats.append(self.get_item(	11800	,	"sorting"	))
                cats.append(self.get_item(	11801	,	"strings"	))
                cats.append(self.get_item(	11802	,	"utils"	))
                return cats

        def get_root_eugen(self, dd):
                root_src = "C:/lkd/ht/apps_spring_eugen/app/src/tutorials"
                return root_src

        def get_cats_eugen(self, psrc_path_project):
                cats = []                

                cats.append(self.get_item(	12051	,	"	akka-http	"	))
                cats.append(self.get_item(	12052	,	"	akka-streams	"	))
                cats.append(self.get_item(	12053	,	"	algorithms-genetic	"	))
                cats.append(self.get_item(	12054	,	"	algorithms-miscellaneous-1	"	))
                cats.append(self.get_item(	12055	,	"	algorithms-miscellaneous-2	"	))
                cats.append(self.get_item(	12056	,	"	algorithms-miscellaneous-3	"	))
                cats.append(self.get_item(	12057	,	"	algorithms-miscellaneous-4	"	))
                cats.append(self.get_item(	12058	,	"	algorithms-miscellaneous-5	"	))
                cats.append(self.get_item(	12059	,	"	algorithms-miscellaneous-6	"	))
                cats.append(self.get_item(	12060	,	"	algorithms-searching	"	))
                cats.append(self.get_item(	12061	,	"	algorithms-sorting	"	))
                cats.append(self.get_item(	12062	,	"	algorithms-sorting-2	"	))
                cats.append(self.get_item(	12063	,	"	animal-sniffer-mvn-plugin	"	))
                cats.append(self.get_item(	12064	,	"	annotations	"	))
                cats.append(self.get_item(	12065	,	"	antlr	"	))
                cats.append(self.get_item(	12066	,	"	apache-cxf	"	))
                cats.append(self.get_item(	12067	,	"	apache-libraries	"	))
                cats.append(self.get_item(	12068	,	"	apache-olingo	"	))
                cats.append(self.get_item(	12069	,	"	apache-poi	"	))
                cats.append(self.get_item(	12070	,	"	apache-rocketmq	"	))
                cats.append(self.get_item(	12071	,	"	apache-shiro	"	))
                cats.append(self.get_item(	12072	,	"	apache-spark	"	))
                cats.append(self.get_item(	12073	,	"	apache-tapestry	"	))
                cats.append(self.get_item(	12074	,	"	apache-thrift	"	))
                cats.append(self.get_item(	12075	,	"	apache-tika	"	))
                cats.append(self.get_item(	12076	,	"	apache-velocity	"	))
                cats.append(self.get_item(	12077	,	"	asciidoctor	"	))
                cats.append(self.get_item(	12078	,	"	asm	"	))
                cats.append(self.get_item(	12079	,	"	atomikos	"	))
                cats.append(self.get_item(	12080	,	"	atomix	"	))
                cats.append(self.get_item(	12081	,	"	aws	"	))
                cats.append(self.get_item(	12082	,	"	aws-app-sync	"	))
                cats.append(self.get_item(	12083	,	"	aws-lambda	"	))
                cats.append(self.get_item(	12084	,	"	aws-reactive	"	))
                cats.append(self.get_item(	12085	,	"	axon	"	))
                cats.append(self.get_item(	12086	,	"	azure	"	))
                cats.append(self.get_item(	12087	,	"	bazel	"	))
                cats.append(self.get_item(	12088	,	"	blade	"	))
                cats.append(self.get_item(	12089	,	"	bootique	"	))
                cats.append(self.get_item(	12090	,	"	cas	"	))
                cats.append(self.get_item(	12091	,	"	cdi	"	))
                cats.append(self.get_item(	12092	,	"	checker-plugin	"	))
                cats.append(self.get_item(	12093	,	"	clojure	"	))
                cats.append(self.get_item(	12094	,	"	cloud-foundry-uaa	"	))
                cats.append(self.get_item(	12095	,	"	code-generation	"	))
                cats.append(self.get_item(	12096	,	"	core-groovy	"	))
                cats.append(self.get_item(	12097	,	"	core-groovy-2	"	))
                cats.append(self.get_item(	12098	,	"	core-groovy-collections	"	))
                cats.append(self.get_item(	12099	,	"	core-groovy-strings	"	))
                cats.append(self.get_item(	12100	,	"	core-java-modules	"	))
                cats.append(self.get_item(	12101	,	"	couchbase	"	))
                cats.append(self.get_item(	12102	,	"	custom-pmd	"	))
                cats.append(self.get_item(	12103	,	"	dagger	"	))
                cats.append(self.get_item(	12104	,	"	data-structures	"	))
                cats.append(self.get_item(	12105	,	"	ddd	"	))
                cats.append(self.get_item(	12106	,	"	ddd-modules	"	))
                cats.append(self.get_item(	12107	,	"	deeplearning4j	"	))
                cats.append(self.get_item(	12108	,	"	discord4j	"	))
                cats.append(self.get_item(	12109	,	"	disruptor	"	))
                cats.append(self.get_item(	12110	,	"	docker	"	))
                cats.append(self.get_item(	12111	,	"	dozer	"	))
                cats.append(self.get_item(	12112	,	"	drools	"	))
                cats.append(self.get_item(	12113	,	"	dropwizard	"	))
                cats.append(self.get_item(	12114	,	"	dubbo	"	))
                cats.append(self.get_item(	12115	,	"	eclipse	"	))
                cats.append(self.get_item(	12116	,	"	ethereum	"	))
                cats.append(self.get_item(	12117	,	"	feign	"	))
                cats.append(self.get_item(	12118	,	"	flyway-cdi-extension	"	))
                cats.append(self.get_item(	12119	,	"	geotools	"	))
                cats.append(self.get_item(	12120	,	"	google-cloud	"	))
                cats.append(self.get_item(	12121	,	"	google-web-toolkit	"	))
                cats.append(self.get_item(	12122	,	"	gradle	"	))
                cats.append(self.get_item(	12123	,	"	gradle-5	"	))
                cats.append(self.get_item(	12124	,	"	gradle-6	"	))
                cats.append(self.get_item(	12125	,	"	grails	"	))
                cats.append(self.get_item(	12126	,	"	graphql	"	))
                cats.append(self.get_item(	12127	,	"	grpc	"	))
                cats.append(self.get_item(	12128	,	"	gson	"	))
                cats.append(self.get_item(	12129	,	"	guava-modules	"	))
                cats.append(self.get_item(	12130	,	"	guest	"	))
                cats.append(self.get_item(	12131	,	"	guice	"	))
                cats.append(self.get_item(	12132	,	"	hazelcast	"	))
                cats.append(self.get_item(	12133	,	"	helidon	"	))
                cats.append(self.get_item(	12134	,	"	httpclient	"	))
                cats.append(self.get_item(	12135	,	"	httpclient-2	"	))
                cats.append(self.get_item(	12136	,	"	httpclient-simple	"	))
                cats.append(self.get_item(	12137	,	"	hystrix	"	))
                cats.append(self.get_item(	12138	,	"	image-processing	"	))
                cats.append(self.get_item(	12139	,	"	immutables	"	))
                cats.append(self.get_item(	12140	,	"	intelliJ	"	))
                cats.append(self.get_item(	12141	,	"	jackson-modules	"	))
                cats.append(self.get_item(	12142	,	"	jackson-simple	"	))
                cats.append(self.get_item(	12143	,	"	java-blockchain	"	))
                cats.append(self.get_item(	12144	,	"	java-collections-conversions	"	))
                cats.append(self.get_item(	12145	,	"	java-collections-conversions-2	"	))
                cats.append(self.get_item(	12146	,	"	java-collections-maps-3	"	))
                cats.append(self.get_item(	12147	,	"	java-ee-8-security-api	"	))
                cats.append(self.get_item(	12148	,	"	java-jdi	"	))
                cats.append(self.get_item(	12149	,	"	java-lite	"	))
                cats.append(self.get_item(	12150	,	"	java-native	"	))
                cats.append(self.get_item(	12151	,	"	java-numbers	"	))
                cats.append(self.get_item(	12152	,	"	java-numbers-2	"	))
                cats.append(self.get_item(	12153	,	"	java-numbers-3	"	))
                cats.append(self.get_item(	12154	,	"	java-numbers-4	"	))
                cats.append(self.get_item(	12155	,	"	java-rmi	"	))
                cats.append(self.get_item(	12156	,	"	java-spi	"	))
                cats.append(self.get_item(	12157	,	"	java-vavr-stream	"	))
                cats.append(self.get_item(	12158	,	"	java-websocket	"	))
                cats.append(self.get_item(	12159	,	"	javafx	"	))
                cats.append(self.get_item(	12160	,	"	javax-servlets	"	))
                cats.append(self.get_item(	12161	,	"	javaxval	"	))
                cats.append(self.get_item(	12162	,	"	jaxb	"	))
                cats.append(self.get_item(	12163	,	"	jee-7	"	))
                cats.append(self.get_item(	12164	,	"	jee-7-security	"	))
                cats.append(self.get_item(	12165	,	"	jenkins	"	))
                cats.append(self.get_item(	12166	,	"	jersey	"	))
                cats.append(self.get_item(	12167	,	"	jgit	"	))
                cats.append(self.get_item(	12168	,	"	jgroups	"	))
                cats.append(self.get_item(	12169	,	"	jhipster	"	))
                cats.append(self.get_item(	12170	,	"	jhipster-5	"	))
                cats.append(self.get_item(	12171	,	"	jib	"	))
                cats.append(self.get_item(	12172	,	"	jjwt	"	))
                cats.append(self.get_item(	12173	,	"	jmeter	"	))
                cats.append(self.get_item(	12174	,	"	jmh	"	))
                cats.append(self.get_item(	12175	,	"	jooby	"	))
                cats.append(self.get_item(	12176	,	"	jsf	"	))
                cats.append(self.get_item(	12177	,	"	json	"	))
                cats.append(self.get_item(	12178	,	"	json-2	"	))
                cats.append(self.get_item(	12179	,	"	json-path	"	))
                cats.append(self.get_item(	12180	,	"	jsoup	"	))
                cats.append(self.get_item(	12181	,	"	jta	"	))
                cats.append(self.get_item(	12182	,	"	jws	"	))
                cats.append(self.get_item(	12183	,	"	kaniko	"	))
                cats.append(self.get_item(	12184	,	"	lagom	"	))
                cats.append(self.get_item(	12185	,	"	language-interop	"	))
                cats.append(self.get_item(	12186	,	"	libraries	"	))
                cats.append(self.get_item(	12187	,	"	libraries-2	"	))
                cats.append(self.get_item(	12188	,	"	libraries-3	"	))
                cats.append(self.get_item(	12189	,	"	libraries-4	"	))
                cats.append(self.get_item(	12190	,	"	libraries-5	"	))
                cats.append(self.get_item(	12191	,	"	libraries-6	"	))
                cats.append(self.get_item(	12192	,	"	libraries-apache-commons	"	))
                cats.append(self.get_item(	12193	,	"	libraries-apache-commons-collections	"	))
                cats.append(self.get_item(	12194	,	"	libraries-apache-commons-io	"	))
                cats.append(self.get_item(	12195	,	"	libraries-concurrency	"	))
                cats.append(self.get_item(	12196	,	"	libraries-data	"	))
                cats.append(self.get_item(	12197	,	"	libraries-data-2	"	))
                cats.append(self.get_item(	12198	,	"	libraries-data-db	"	))
                cats.append(self.get_item(	12199	,	"	libraries-data-io	"	))
                cats.append(self.get_item(	12200	,	"	libraries-http	"	))
                cats.append(self.get_item(	12201	,	"	libraries-http-2	"	))
                cats.append(self.get_item(	12202	,	"	libraries-io	"	))
                cats.append(self.get_item(	12203	,	"	libraries-primitive	"	))
                cats.append(self.get_item(	12204	,	"	libraries-rpc	"	))
                cats.append(self.get_item(	12205	,	"	libraries-security	"	))
                cats.append(self.get_item(	12206	,	"	libraries-server	"	))
                cats.append(self.get_item(	12207	,	"	libraries-server-2	"	))
                cats.append(self.get_item(	12208	,	"	libraries-testing	"	))
                cats.append(self.get_item(	12209	,	"	linkrest	"	))
                cats.append(self.get_item(	12210	,	"	linux-bash	"	))
                cats.append(self.get_item(	12211	,	"	logging-modules	"	))
                cats.append(self.get_item(	12212	,	"	lombok	"	))
                cats.append(self.get_item(	12213	,	"	lombok-custom	"	))
                cats.append(self.get_item(	12214	,	"	lucene	"	))
                cats.append(self.get_item(	12215	,	"	mapstruct	"	))
                cats.append(self.get_item(	12216	,	"	maven-archetype	"	))
                cats.append(self.get_item(	12217	,	"	maven-modules	"	))
                cats.append(self.get_item(	12218	,	"	maven-polyglot	"	))
                cats.append(self.get_item(	12219	,	"	mesos-marathon	"	))
                cats.append(self.get_item(	12220	,	"	metrics	"	))
                cats.append(self.get_item(	12221	,	"	micronaut	"	))
                cats.append(self.get_item(	12222	,	"	microprofile	"	))
                cats.append(self.get_item(	12223	,	"	msf4j	"	))
                cats.append(self.get_item(	12224	,	"	muleesb	"	))
                cats.append(self.get_item(	12225	,	"	mustache	"	))
                cats.append(self.get_item(	12226	,	"	mybatis	"	))
                cats.append(self.get_item(	12227	,	"	netflix-modules	"	))
                cats.append(self.get_item(	12228	,	"	netty	"	))
                cats.append(self.get_item(	12229	,	"	ninja	"	))
                cats.append(self.get_item(	12230	,	"	oauth2-framework-impl	"	))
                cats.append(self.get_item(	12231	,	"	open-liberty	"	))
                cats.append(self.get_item(	12232	,	"	optaplanner	"	))
                cats.append(self.get_item(	12233	,	"	orika	"	))
                cats.append(self.get_item(	12234	,	"	osgi	"	))
                cats.append(self.get_item(	12235	,	"	parent-boot-1	"	))
                cats.append(self.get_item(	12236	,	"	parent-boot-2	"	))
                cats.append(self.get_item(	12237	,	"	parent-java	"	))
                cats.append(self.get_item(	12238	,	"	parent-spring-4	"	))
                cats.append(self.get_item(	12239	,	"	parent-spring-5	"	))
                cats.append(self.get_item(	12240	,	"	patterns	"	))
                cats.append(self.get_item(	12241	,	"	pdf	"	))
                cats.append(self.get_item(	12242	,	"	performance-tests	"	))
                cats.append(self.get_item(	12243	,	"	persistence-modules	"	))
                cats.append(self.get_item(	12244	,	"	play-framework	"	))
                cats.append(self.get_item(	12245	,	"	pmd	"	))
                cats.append(self.get_item(	12246	,	"	podman	"	))
                cats.append(self.get_item(	12247	,	"	protobuffer	"	))
                cats.append(self.get_item(	12248	,	"	quarkus	"	))
                cats.append(self.get_item(	12249	,	"	quarkus-extension	"	))
                cats.append(self.get_item(	12250	,	"	rabbitmq	"	))
                cats.append(self.get_item(	12251	,	"	raml	"	))
                cats.append(self.get_item(	12252	,	"	ratpack	"	))
                cats.append(self.get_item(	12253	,	"	reactive-systems	"	))
                cats.append(self.get_item(	12254	,	"	reactor-core	"	))
                cats.append(self.get_item(	12255	,	"	resteasy	"	))
                cats.append(self.get_item(	12256	,	"	restx	"	))
                cats.append(self.get_item(	12257	,	"	rsocket	"	))
                cats.append(self.get_item(	12258	,	"	rule-engines	"	))
                cats.append(self.get_item(	12259	,	"	rxjava-core	"	))
                cats.append(self.get_item(	12260	,	"	rxjava-libraries	"	))
                cats.append(self.get_item(	12261	,	"	rxjava-observables	"	))
                cats.append(self.get_item(	12262	,	"	rxjava-operators	"	))
                cats.append(self.get_item(	12263	,	"	saas	"	))
                cats.append(self.get_item(	12264	,	"	slack	"	))
                cats.append(self.get_item(	12265	,	"	software-security	"	))
                cats.append(self.get_item(	12266	,	"	spark-java	"	))
                cats.append(self.get_item(	12267	,	"	spf4j	"	))
                cats.append(self.get_item(	12268	,	"	spring-4	"	))
                cats.append(self.get_item(	12269	,	"	spring-5	"	))
                cats.append(self.get_item(	12270	,	"	spring-5-data-reactive	"	))
                cats.append(self.get_item(	12271	,	"	spring-5-reactive	"	))
                cats.append(self.get_item(	12272	,	"	spring-5-reactive-2	"	))
                cats.append(self.get_item(	12273	,	"	spring-5-reactive-client	"	))
                cats.append(self.get_item(	12274	,	"	spring-5-reactive-oauth	"	))
                cats.append(self.get_item(	12275	,	"	spring-5-reactive-security	"	))
                cats.append(self.get_item(	12276	,	"	spring-5-webflux	"	))
                cats.append(self.get_item(	12277	,	"	spring-activiti	"	))
                cats.append(self.get_item(	12278	,	"	spring-akka	"	))
                cats.append(self.get_item(	12279	,	"	spring-amqp	"	))
                cats.append(self.get_item(	12280	,	"	spring-aop	"	))
                cats.append(self.get_item(	12281	,	"	spring-apache-camel	"	))
                cats.append(self.get_item(	12282	,	"	spring-batch	"	))
                cats.append(self.get_item(	12283	,	"	spring-batch-2	"	))
                cats.append(self.get_item(	12284	,	"	spring-bom	"	))
                cats.append(self.get_item(	12285	,	"	spring-boot-modules	"	))
                cats.append(self.get_item(	12286	,	"	spring-boot-rest	"	))
                cats.append(self.get_item(	12287	,	"	spring-caching	"	))
                cats.append(self.get_item(	12288	,	"	spring-cloud	"	))
                cats.append(self.get_item(	12289	,	"	spring-cloud-bus	"	))
                cats.append(self.get_item(	12290	,	"	spring-cloud-cli	"	))
                cats.append(self.get_item(	12291	,	"	spring-cloud-data-flow	"	))
                cats.append(self.get_item(	12292	,	"	spring-core	"	))
                cats.append(self.get_item(	12293	,	"	spring-core-2	"	))
                cats.append(self.get_item(	12294	,	"	spring-core-3	"	))
                cats.append(self.get_item(	12295	,	"	spring-core-4	"	))
                cats.append(self.get_item(	12296	,	"	spring-core-5	"	))
                cats.append(self.get_item(	12297	,	"	spring-cucumber	"	))
                cats.append(self.get_item(	12298	,	"	spring-data-rest	"	))
                cats.append(self.get_item(	12299	,	"	spring-data-rest-querydsl	"	))
                cats.append(self.get_item(	12300	,	"	spring-di	"	))
                cats.append(self.get_item(	12301	,	"	spring-di-2	"	))
                cats.append(self.get_item(	12302	,	"	spring-drools	"	))
                cats.append(self.get_item(	12303	,	"	spring-ejb	"	))
                cats.append(self.get_item(	12304	,	"	spring-exceptions	"	))
                cats.append(self.get_item(	12305	,	"	spring-freemarker	"	))
                cats.append(self.get_item(	12306	,	"	spring-integration	"	))
                cats.append(self.get_item(	12307	,	"	spring-jenkins-pipeline	"	))
                cats.append(self.get_item(	12308	,	"	spring-jersey	"	))
                cats.append(self.get_item(	12309	,	"	spring-jinq	"	))
                cats.append(self.get_item(	12310	,	"	spring-jms	"	))
                cats.append(self.get_item(	12311	,	"	spring-kafka	"	))
                cats.append(self.get_item(	12312	,	"	spring-katharsis	"	))
                cats.append(self.get_item(	12313	,	"	spring-mobile	"	))
                cats.append(self.get_item(	12314	,	"	spring-mockito	"	))
                cats.append(self.get_item(	12315	,	"	spring-protobuf	"	))
                cats.append(self.get_item(	12316	,	"	spring-quartz	"	))
                cats.append(self.get_item(	12317	,	"	spring-reactor	"	))
                cats.append(self.get_item(	12318	,	"	spring-remoting	"	))
                cats.append(self.get_item(	12319	,	"	spring-roo	"	))
                cats.append(self.get_item(	12320	,	"	spring-scheduling	"	))
                cats.append(self.get_item(	12321	,	"	spring-security-modules	"	))
                cats.append(self.get_item(	12322	,	"	spring-shell	"	))
                cats.append(self.get_item(	12323	,	"	spring-sleuth	"	))
                cats.append(self.get_item(	12324	,	"	spring-soap	"	))
                cats.append(self.get_item(	12325	,	"	spring-spel	"	))
                cats.append(self.get_item(	12326	,	"	spring-state-machine	"	))
                cats.append(self.get_item(	12327	,	"	spring-static-resources	"	))
                cats.append(self.get_item(	12328	,	"	spring-swagger-codegen	"	))
                cats.append(self.get_item(	12329	,	"	spring-threads	"	))
                cats.append(self.get_item(	12330	,	"	spring-vault	"	))
                cats.append(self.get_item(	12331	,	"	spring-vertx	"	))
                cats.append(self.get_item(	12332	,	"	spring-web-modules	"	))
                cats.append(self.get_item(	12333	,	"	spring-webflux-amqp	"	))
                cats.append(self.get_item(	12334	,	"	spring-webflux-threads	"	))
                cats.append(self.get_item(	12335	,	"	spring-websockets	"	))
                cats.append(self.get_item(	12336	,	"	static-analysis	"	))
                cats.append(self.get_item(	12337	,	"	stripe	"	))
                cats.append(self.get_item(	12338	,	"	structurizr	"	))
                cats.append(self.get_item(	12339	,	"	struts-2	"	))
                cats.append(self.get_item(	12340	,	"	tensorflow-java	"	))
                cats.append(self.get_item(	12341	,	"	terraform	"	))
                cats.append(self.get_item(	12342	,	"	testing-modules	"	))
                cats.append(self.get_item(	12343	,	"	twilio	"	))
                cats.append(self.get_item(	12344	,	"	twitter4j	"	))
                cats.append(self.get_item(	12345	,	"	undertow	"	))
                cats.append(self.get_item(	12346	,	"	vaadin	"	))
                cats.append(self.get_item(	12347	,	"	vavr	"	))
                cats.append(self.get_item(	12348	,	"	vavr-2	"	))
                cats.append(self.get_item(	12349	,	"	vertx	"	))
                cats.append(self.get_item(	12350	,	"	vertx-and-rxjava	"	))
                cats.append(self.get_item(	12351	,	"	video-tutorials	"	))
                cats.append(self.get_item(	12352	,	"	vraptor	"	))
                cats.append(self.get_item(	12353	,	"	webrtc	"	))
                cats.append(self.get_item(	12354	,	"	wicket	"	))
                cats.append(self.get_item(	12355	,	"	wildfly	"	))
                cats.append(self.get_item(	12356	,	"	xml	"	))
                cats.append(self.get_item(	12357	,	"	xstream	"	))
                return cats


        def get_root_etherneum_lkdg(self, dd):
                root_src = "C:/lkd/ht/apps_ether_currency/app/src/lakida_ether_currency/"
                return root_src

        def get_cats_etherneum_lkdg(self, psrc_path_project):
                cats = []
                cats.append(self.get_item(12483	,"truffle424"	))
                return cats

        def get_root_springboot_examples(self, dd):
                root_src = "C:/lkd/ht/apps_springboot_tutorial/src/app/springboot_tutorial/"
                return root_src

        def get_cats_springboot_examples(self, psrc_path_project):
                cats = []
                return cats
                # cats.append(self.get_item(	15963	,	"login-registration-springboot-hibernate-jsp-auth"))                
                #cats.append(self.get_item(	15964	,	"registration-login-springboot-security-thymeleaf"))                
                # cats.append(self.get_item(	15965	,	"spring-aop-advice-examples"))
                
                #cats.append(self.get_item(	15966	,	"spring-boot-crud-rest"))
                #cats.append(self.get_item(	15967	,	"spring-propertysource-example"))
                #cats.append(self.get_item(	15968	,	"springboot-angular8-helloworld-example"))
                #cats.append(self.get_item(	15969	,	"springboot-async-example"))
                #cats.append(self.get_item(	15970	,	"springboot-crud-hibernate-example"))
                #cats.append(self.get_item(	15971	,	"springboot-crud-rest-api-validation"))
                #cats.append(self.get_item(	15972	,	"springboot-hibernate-composite-key-demo"))
                #cats.append(self.get_item(	15973	,	"springboot-hibernate-many-to-many-mapping"))
                
                cats.append(self.get_item(	15974	,	"springboot-hibernate-one-many-mapping"))
                cats.append(self.get_item(	15975	,	"springboot-hibernate-one-one-mapping"))
                cats.append(self.get_item(	15976	,	"springboot-jms"))
                cats.append(self.get_item(	15977	,	"springboot-jpa-one-to-one-example"))
                cats.append(self.get_item(	15978	,	"springboot-jsp-hello-world-example"))
                cats.append(self.get_item(	15979	,	"springboot-mongodb-crud"))
                cats.append(self.get_item(	15980	,	"springboot-multiple-datasources"))
                cats.append(self.get_item(	15981	,	"springboot-stomp-websocket"))
                cats.append(self.get_item(	15982	,	"springboot-testing-examples"))
                cats.append(self.get_item(	15983	,	"springboot-thymeleaf-hello-world-example"))
                cats.append(self.get_item(	15984	,	"springboot-thymeleaf-security-demo"))
                cats.append(self.get_item(	15985	,	"springboot-upload-download-file-database"))
                cats.append(self.get_item(	15986	,	"springboot-upload-download-file-rest-api-example"))
                cats.append(self.get_item(	15987	,	"springboot2-annotation-config"))
                cats.append(self.get_item(	15988	,	"springboot2-externalizing-conf-properties"))
                cats.append(self.get_item(	15989	,	"springboot2-freemarker-example"))
                cats.append(self.get_item(	15990	,	"springboot2-java-config"))
                cats.append(self.get_item(	15991	,	"springboot2-jdbc-crud-mysql-example"))
                cats.append(self.get_item(	15992	,	"springboot2-jms-activemq"))
                cats.append(self.get_item(	15993	,	"springboot2-jpa-auditing"))
                cats.append(self.get_item(	15994	,	"springboot2-jpa-crud-example"))
                cats.append(self.get_item(	15995	,	"springboot2-jpa-h2-crud-example"))
                cats.append(self.get_item(	15996	,	"springboot2-jpa-swagger2"))
                cats.append(self.get_item(	15997	,	"springboot2-junit5-example"))
                cats.append(self.get_item(	15998	,	"springboot2-logging"))
                cats.append(self.get_item(	15999	,	"springboot2-mssql-jpa-hibernate-crud-example"))
                cats.append(self.get_item(	16000	,	"springboot2-mybatis-mysql-example"))
                cats.append(self.get_item(	16001	,	"springboot2-postgresql-jpa-hibernate-crud-example"))
                cats.append(self.get_item(	16002	,	"springboot2-springaop-example"))
                cats.append(self.get_item(	16003	,	"springboot2-webapp-jsp"))
                cats.append(self.get_item(	16004	,	"springboot2-webapp-jsp-WAR"))
                cats.append(self.get_item(	16005	,	"springboot2-webapp-thymeleaf"))
                cats.append(self.get_item(	16006	,	"springboot2-xml-config"))
                return cats

        def get_root_springboot_examples(self, dd):
                root_src = "C:/lkd/ht/apps_springboot_tutorial/src/app/springboot_tutorial/"
                return root_src

        def get_root_java_8_jacektracz_tutorial(self, dd):
                root_src = "C:/lkd/ht/apps_java8_in_action/app/src/"
                return root_src

        def get_cats_java_8_jacektracz_tutorial(self, psrc_path_project):
                cats = []
               
                cats.append(self.get_item(	16013	,	"java-8-jacektracz-tutorial"))
                return cats


# C:\lkd\servers\installed\python27\python C:\lkd\ht\apps_w2_risk\app\src\apps_w2_w2\src\lkdpy\start_cpy.py perform-src-files
