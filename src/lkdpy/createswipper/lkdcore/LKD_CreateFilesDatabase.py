﻿import sys
import os
import logging
import shutil
from LKD_CopyFilesMd import *
from LKD_CatItem import *

#  C:\lkd\servers\installed\python27\python C:\lkd\ht\apps_w2_risk\app\src\apps_w2_w2\src\lkdpy\start_cpy.py

class LKD_CreateFilesDatabase:
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
                return self.get_cats_jhreact("")

        def get_generic_root(self,dd):
                # return self.get_root_espn()
                # return self.get_root_j8p()
                # return self.get_root_sbms("")
                # return self.get_root_pets("")
                # return self.get_root_fineract("")
                # return self.get_root_eureka_feign("")
                return self.get_root_jhreact("")

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



