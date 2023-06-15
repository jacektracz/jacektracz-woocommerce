        def set_dirs_sequential_imgs_raw(self):
                self.xx_dbg("LKD_CreateImages::" 
                        + "set_dirs_sequential_imgs::in::")
                self.m_root_sequential_ids_src = "C:\\lkd\\ht\\apps_ctx\\1\\" 
                        + "Lakida-Knowledge-Base-Tech-Episodes-Topics\\" 
                        + "Lakida-Knowledge-Base-Tech-Episodes-Resources\\" 
                        + "Lakida-Knowledge-Base-Tech-Episodes\\Kubernetes-Resources\\"
                self.m_root_sequential_ids_src = "Installing-Ethereum-On-Kubernetes"

                self.m_root_sequential_ids_dst = "C:\\lkd\\ht\\apps_portal\\lkduni\\" 
                        + "app-4\\src\\modules\\mod_ep_articles\\" 
                        + "content_cats\\" 
                        + "content_markdown\\" 
                        + "content_by_groups\\cat__8000\\" 
                        + "cat__000\\cat__00\\cat__8000\\" 
                        + "content_idx_0\\" 
                        + "imgs_seq_dst\\"

                srv_handler = LKD_MdFilesUtils("")
                dd_active_cat_id = 15850
                dd_file_idx = 0
                self.m_root_sequential_ids_dst = srv_handler.get_root_for_groups(  
                        dd_active_cat_id , 
                        dd_file_idx)

                self.m_root_sequential_ids_dst  = self.m_root_sequential_ids_dst  
                        + "\\content_idx_0\\imgs"

                self.xx_dbg("LKD_CreateImages::" 
                        + "set_dirs_sequential_imgs::src::" 
                        + self.m_root_sequential_ids_src)

                self.xx_dbg("LKD_CreateImages::" 
                        + "set_dirs_sequential_imgs::det::" 
                        + self.m_root_sequential_ids_dst)

                self.xx_dbg("LKD_CreateImages::" 
                        + "set_dirs_sequential_imgs::out::")

