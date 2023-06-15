class LKD_CatItem:

        def __init__(self, pcatid, psrc_project_relative_path):

                self.catid = pcatid
                self.src_project_relative_path = psrc_project_relative_path
                self.src_javafile_full_path = ""
                self.src_javafile_name = ""
                self.dest_java_flat_dir_path = ""

        def getCatId( self ):
                return self.catid

        def getShortDirName( self ):
                return self.src_project_relative_path