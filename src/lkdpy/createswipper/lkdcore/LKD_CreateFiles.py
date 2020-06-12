import sys
import os
import logging
import shutil
from LKD_CopyFilesMd import *

#  C:\lkd\servers\installed\python27\python C:\lkd\ht\apps_w2_risk\app\src\apps_w2_w2\src\lkdpy\start_cpy.py

class LKD_CatItem:
        def __init__(self, pcatid, psrc_project_relative_path):

                self.catid = pcatid
                self.src_project_relative_path = psrc_project_relative_path
                self.src_javafile_full_path = ""
                self.src_javafile_name = ""
                self.dest_java_flat_dir_path = ""

class LKD_CreateFiles:

        def __init__(self,spar):                                
                self.xx_dbg("LKD_CopyFiles::__init__::in::")
                self.m_src = "C:/lkd/ht/apps_java8_in_action/app/src/jacek-tracz-java-design-patterns"
                self.m_dst = "services_s3"
                self.m_root_src = ""
                self.m_root_dst = ""
                self.m_test_mode = 0
                #self.m_override_mode = False
                self.m_override_mode = True
                self.m_ds = "/"
                self.xx_dbg("LKD_CopyFiles::__init__::out::")
               
        
        def prepare_object(self):
                self.xx_dbg("LKD_CopyFiles::prepare_object::in::")
                        
                self.xx_dbg("LKD_CopyFiles::prepare_object::out::")

        #def get_generic_cats_items(self,dd)
        #        return self.get_cats_espn("")

        #def get_generic_root(self,dd)
        #        return self.get_root_espn()

        def execute_main(self):

                self.xx_dbg("LKD_CopyFiles::execute_main::in::")

                paths = self.get_generic_cats_items("")

                for path in paths:
                        root_scr_path = self.get_generic_root("")
                        src_path = root_scr_path + "/" + path.src_project_relative_path + "/src"
                        self.read_directory_subdirs_flat(
                                src_path
                                , path.catid)

                self.xx_dbg("LKD_CopyFiles::execute_main::out::")

        def create_dir(self, dir_path):

                if os.path.isdir(dir_path):
                        self.xx_dbg("[dir_exists_no_err]" + dir_path)
                else:
                        os.makedirs(dir_path)
                        self.xx_print("dir-created" + dir_path )


        def read_directory_subdirs_flat(self, psrc_path_project, pcatid):
                self.xx_dbg("LKD_CopyFiles::read_directory_subdirs_flat::in::")
                
                print psrc_path_project

                if(os.path.isdir(psrc_path_project) == False):
                        return

                print "execute path"

                dd_cxatpath = LKD_CopyFilesMd("")

                rootpath = dd_cxatpath.get_root_for_groups(pcatid, "0")

                self.xx_print(rootpath)

                dest_java_flat_dir_path = rootpath + "/content_idx_0/javafiles/flat" 

                dest_java_root_idx_0_dir_path = rootpath + "/content_idx_0"

                self.xx_print(dest_java_flat_dir_path)

                self.create_dir(dest_java_flat_dir_path)

                java_files = self.get_files_recur(
                                psrc_path_project
                                , pcatid
                                ,       dest_java_flat_dir_path)

                self.copy_javafiles(java_files)

                self.create_javafiles_md(java_files ,dest_java_root_idx_0_dir_path)

                self.xx_dbg("LKD_CopyFiles::read_directory_subdirs_flat::out::")

        def get_print_files_recur(self,psrc_path_project):
                for x in os.listdir(psrc_path_project):
                        if os.path.isfile(x): print 'f-', x
                        elif os.path.isdir(x): print 'd-', x
                        elif os.path.islink(x): print 'l-', x
                        else: print '---', x

        def copy_javafiles(self, file_items):
                for file_item in file_items:
                        src_fpath = file_item.src_javafile_full_path
                        dest_fpath = file_item.dest_java_flat_dir_path + "/" + file_item.src_javafile_name
                        self.xx_dbg("copy-from:" + src_fpath)
                        self.xx_dbg("copy-to:" + dest_fpath)

                        shutil.copy(src_fpath, dest_fpath)

        def create_javafiles_md(self, file_items , dest_java_root_idx_0_dir_path):
                ii = 0
                for file_item in file_items:
                        src_fpath = file_item.src_javafile_full_path
                        dest_fpath = file_item.dest_java_flat_dir_path + "/" + "content__java_files.md"

                        dest_root_fpath = dest_java_root_idx_0_dir_path + "/" + "content__java_files.md"

                        self.xx_dbg("copy-from:" + src_fpath)
                        self.xx_dbg("copy-to:" + dest_fpath)    
                        file_header = "### Source File: " + file_item.src_javafile_name                        

                        if (ii == 1):                                
                                self.create_empty_file(src_fpath, dest_fpath , file_header)
                                self.create_empty_file(src_fpath, dest_root_fpath , file_header)

                        self.copy_lines_from_file(src_fpath, dest_fpath , file_header)

                        self.copy_lines_from_file(src_fpath, dest_root_fpath , file_header)

                        ii = ii + 1


        def get_files_recur(self, psrc_path_project, pcatid, pdest_java_flat_dir_path):
                fjavafiles = []
                for root,d_names,f_names in os.walk(psrc_path_project):
	                for f in f_names:
                                dd = LKD_CatItem(pcatid, psrc_path_project)
                                dd.catid = pcatid
                                dd.src_project_relative_path = psrc_path_project
                                dd.src_javafile_full_path = os.path.join(root, f)
                                dd.src_javafile_name = f
                                dd.dest_java_flat_dir_path = pdest_java_flat_dir_path
		                fjavafiles.append(dd)

                return fjavafiles

        def create_empty_file(self, filename_src, filename_dest, pfileheader):
                lout = []
                with open(filename_dest, "w") as f:
                        f.writelines(lout)

        def copy_lines_from_file(self, filename_src, filename_dest, pfileheader):
                self.xx_dbg("[METHOD_IN]" + "[inplace_change]")

                self.xx_dbg("src_file_to_copy:" + filename_src)
                self.xx_dbg("filename_dest:" + filename_dest)


                # Safely write the changed content, if found in the file
                lout = []
                with open(filename_src, "r") as f:
                        lines = f.readlines()                         
                        lout.append("\r\n")
                        lout.append("\r\n")
                        lout.append(pfileheader)
                        lout.append("\r\n")
                        lout.append("\r\n")
                        lout.append("```Java")
                        lout.append("\r\n")
                        for line in lines:
                                lout.append(line)
                        lout.append("\r\n")
                        lout.append("```")

                with open(filename_dest, "a") as f:
                        f.writelines(lout)

                self.xx_dbg("[METHOD_OUT]" + "[inplace_change]")

        def read_directory_subdirs_only(self, psrc_path_project):
                #self.xx_dbg("LKD_CopyFiles::read_directory_subdirs_flat::in::")
                print psrc_path_project

                if(os.path.isdir(psrc_path_project) == False):
                        return

                print "execute path"

                for x in os.listdir(psrc_path_project):
                        if os.path.isdir(x): 
                                print x

                #self.xx_dbg("LKD_CopyFiles::read_directory_subdirs_flat::out::")

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

        def get_root_j8p(self):
                root_src = "C:/lkd/ht/apps_java8_in_action/app/src"
                root_src = "C:/lkd/ht/apps_jhipster_cassandra/app"
                return root_src

        def get_cats_j8p(self, psrc_path_project):
                cats = []
                # cats.append(self.get_item(5459,"java-8-jacektracz-tutorial"))
                cats.append(self.get_item(5461,"jhipster-sample-app-cassandra"))
                return cats

        def get_generic_cats_items(self,dd):
                # return self.get_cats_espn("")
                return self.get_cats_j8p("")

        def get_generic_root(self,dd):
                # return self.get_root_espn()
                return self.get_root_j8p()

        def get_item(self, id,title):
                dd = LKD_CatItem(id,title)
                return dd

        def xx_dbg(self, tt):
                "" ""
                print (tt)

        def xx_print(self, tt):
                "" ""
                print (tt)

       

        def read_directory_subdirs(self):

                self.xx_dbg("LKD_CopyFiles::read_directory_subdirs::in::")
                folders = []
                for r, d, f in os.walk(path):
                        for folder in d:
                                folders.append(os.path.join(r, folder))

                for f in folders:
                        print(f)

                self.xx_dbg("LKD_CopyFiles::read_directory_subdirs::out::")
